#include <correlations/Types.hh>
#include <correlations/Result.hh>
#include <correlations/QVector.hh>
#include <correlations/recursive/FromQVector.hh>
#include <correlations/recurrence/FromQVector.hh>
#include <correlations/closed/FromQVector.hh>
#include <TComplex.h>
#include <TH1.h>
#include <TH2.h>
#include <TTree.h>
#include <TNtupleD.h>
#include <TRandom3.h>
#include <TFile.h>
//#include "QWConstV3.h"
#include <RecoHI/HiEvtPlaneAlgos/interface/HiEvtPlaneList.h>
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
//
// constants, enums and typedefs
//


#define PRD(x) cout << "!!QW!! " << __LINE__ << " DEBUG OUTPUT " << (#x) << " = " << (x) << endl;
#define PR(x) cout << "!!QW!! " << __LINE__ << " DEBUG OUTPUT " << (#x) << endl;
//
// class declaration
//


///////////////// Class ////////////////////////////

class QWSC : public edm::EDAnalyzer {
	public:
		explicit QWSC(const edm::ParameterSet&);
		~QWSC();

		static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

	private:
		virtual void beginJob() ;
		virtual void analyze(const edm::Event&, const edm::EventSetup&);
		void analyzeData(const edm::Event&, const edm::EventSetup&);
		void analyzeGen(const edm::Event&, const edm::EventSetup&);
		virtual void endJob() ;

		virtual void beginRun(edm::Run const&, edm::EventSetup const&);
		virtual void endRun(edm::Run const&, edm::EventSetup const&);
		virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
		virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

	/////////////////////////////////////////////
		//TRandom3 * gRandom;
		// ----------member data ---------------------------
		edm::InputTag					trackEta_;
		edm::InputTag					trackPt_;
		edm::InputTag					trackPhi_;
		edm::InputTag					trackWeight_;

		edm::InputTag					vertexTag_;
		edm::InputTag					centralityTag_;
		edm::InputTag					NoffTag_;

	/////////////////////////////////////////////
		double	minvz_, maxvz_;
		double	mineta_, maxeta_;
		double	minpt_, maxpt_;

		bool		bCent_;
		unsigned int	nvtx_;
		int		cmode_;
		std::vector<int>	harmonics_;

	/////////////////////////////////////////////
		TTree * trV;

		int gNoff;
		int gMult;

		double			rQ;
		double			iQ;
		double			wQ;

		correlations::HarmonicVector	hc_;
		correlations::QVector		q_;
		correlations::FromQVector	*cq_;

		void initQ();

};

