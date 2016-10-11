// -*- C++ -*-
//
// Package:    QWSC
// Class:      QWSC
// 
/**\class QWSC QWSC.cc QWAna/QWSC/src/QWSC.cc

Description: [one line class summary]

Implementation:
[Notes on implementation]
*/
//
// Original Author:  Quan Wang
//         Created:  05/23/2014
// $Id: QWSC.cc,v 1.0 2014/05/23 15:56:58 qwang Exp $
//
//


// system include files
#include <memory>
#include <algorithm>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include <DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h>
#include <DataFormats/ParticleFlowCandidate/interface/PFCandidate.h>
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/HeavyIonEvent/interface/EvtPlane.h"
#include "TH1.h"
#include "TH2.h"
#include "TNtuple.h"
#include "TComplex.h"
#include <complex>


#include "QWAna/QWSC/interface/QWSC.h"


using namespace std;

//#ifdef QW_DEBUG
//
// constructors and destructor
//
QWSC::QWSC(const edm::ParameterSet& iConfig)
	:
	trackEta_( iConfig.getUntrackedParameter<edm::InputTag>("trackEta") ),
	trackPt_( iConfig.getUntrackedParameter<edm::InputTag>("trackPt") ),
	trackPhi_( iConfig.getUntrackedParameter<edm::InputTag>("trackPhi") ),
	trackWeight_( iConfig.getUntrackedParameter<edm::InputTag>("trackWeight") ),
	vertexTag_( iConfig.getUntrackedParameter<edm::InputTag>("vertex") ),
	centralityTag_( iConfig.getUntrackedParameter<edm::InputTag>("centrality") ),
	NoffTag( iConfig.getUntrackedParameter<edm::InputTag>("Noff", std::string("NA")) ),
	harmonics_( iConfig.getUntrackedParameter<std::vector<int> >("harmonics") ),
{
	//now do what ever initialization is needed
	minvz_ = iConfig.getUntrackedParameter<double>("minvz", -15.);
	maxvz_ = iConfig.getUntrackedParameter<double>("maxvz", 15.);

	mineta_ = iConfig.getUntrackedParameter<double>("mineta", -2.4);
	maxeta_ = iConfig.getUntrackedParameter<double>("maxeta", 2.4);

	minpt_ = iConfig.getUntrackedParameter<double>("minpt", 0.3);
	maxpt_ = iConfig.getUntrackedParameter<double>("maxpt", 0.3);

	bCent_ = iConfig.getUntrackedParameter<bool>("bCent", false);

	cmode_ = iConfig.getUntrackedParameter<int>("cmode", 1);
	nvtx_ = iConfig.getUntrackedParameter<int>("nvtx", 100);

	consumes<reco::VertexCollection>(vertexTag_);
	consumes<std::vector<double> >(trackEta_);
	consumes<std::vector<double> >(trackPt_);
	consumes<std::vector<double> >(trackPhi_);
	consumes<std::vector<double> >(trackWeight_);

	gNoff = 0;
	gMult = 0;

	//
	edm::Service<TFileService> fs;

	trV = fs->make<TTree>("trV", "trV");
	trV->Branch("Noff", &gNoff, "Noff/I");
	trV->Branch("Mult", &gMult, "Mult/I");

	trV->Branch("rQ", &rQ, "rQ/D");
	trV->Branch("iQ", &iQ, "iQ/D");
	trV->Branch("wQ", &wQ, "wQ/D");

	initQ();
}


QWSC::~QWSC()
{

	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

void
QWSC::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	using namespace edm;
	using namespace reco;

	Handle<std::vector<double> >	hEta;
	Handle<std::vector<double> >	hPt;
	Handle<std::vector<double> >	hPhi;
	Handle<std::vector<double> >	hWeight;

	iEvent.getByLable(trackEta_,	hEta);
	iEvent.getByLable(trackPt_,	hPi);
	iEvent.getByLable(trackPhi_,	hPhi);
	iEvent.getByLable(trackWeight_, hWeight);

	int sz = hEta->size();
	if ( sz == 0 ) {
		cout << " --> sz = 0 empty event" << endl;
	}
	if ( sz != hPt->size() or sz != hPhi->size() or sz != hWeight->size() ) {
		cout << " --> inconsistency" << endl;
	}

	Handle<VertexCollection> vertexCollection;
	iEvent.getByLabel(vertexTag_, vertexCollection);
	VertexCollection recoVertices = *vertexCollection;
	sort(recoVertices.begin(), recoVertices.end(), [](const reco::Vertex &a, const reco::Vertex &b){
			if ( a.tracksSize() == b.tracksSize() ) return a.chi2() < b.chi2();
			return a.tracksSize() > b.tracksSize();
			});
	int primaryvtx = 0;
	double vz = recoVertices[primaryvtx].z();
	if (fabs(vz) < minvz_ || fabs(vz) > maxvz_) {
		return;
	}

	edm::Handle<int> ch;
	if ( bCent_ ) {
		iEvent.getByLabel(centralityTag_, ch);
	} else {
		iEvent.getByLabel(NoffTag_, ch);
	}
	int Cent = *(ch.product());

	for ( int i = 0; i < sz; i++ ) {
		q.fill(hPhi[i], hWeight[i]);
	}

	correlations::Result r;
	for ( int n = 1; n < 7; n++ ) {
		r = cq_->calculate(harmonics_.size(), hc);
	}

	// RFP
	rQ = r.sum().real();
	iQ = r.sum().imag();
	wQ = r.weight();

	gNoff = ch;
	gMult = sz;

	trV->Fill();

	q_.reset();
}


void
QWSC::initQ()
{
	int sz = harmonics_.size();
	hc_ = correlations::HarmonicVector(sz);
	for ( int i = 0; i < sz; i++ ) {
		hc_[i] = harmonics_[i];
	}

	q_.resize(hc_);
	switch ( cmode_ ) {
		case 1:
			cq_ = new correlations::closed::FromQVector(q_);
			break;
		case 2:
			cq_ = new correlations::recurrence::FromQVector(q_);
			break;
		case 3:
			cq_ = new correlations::recursive::FromQVector(q_);
			break;
	}
}

// ------------ method called once each job just before starting event loop  ------------
	void 
QWSC::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
	void 
QWSC::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
	void 
QWSC::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
	void 
QWSC::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
	void 
QWSC::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
	void 
QWSC::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
QWSC::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);

	//Specify that only 'tracks' is allowed
	//To use, remove the default given above and uncomment below
	//ParameterSetDescription desc;
	//desc.addUntracked<edm::InputTag>("tracks","ctfWithMaterialTracks");
	//descriptions.addDefault(desc);
}

//////////////////////////////////////////


//define this as a plug-in
DEFINE_FWK_MODULE(QWSC);
