import FWCore.ParameterSet.Config as cms

process = cms.Process("SC")

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')


process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.MessageLogger.cerr.FwkReport.reportEvery = 100

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring("file:/afs/cern.ch/user/q/qwang/work/cleanroomRun2/Ana/data/pPb_8_FEVT.root")
)

import HLTrigger.HLTfilters.hltHighLevel_cfi

process.hltHM120 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltHM120.HLTPaths = [
	"HLT_PAFullTracks_Multiplicity120_v*",
#	"HLT_PAFullTracks_Multiplicity150_v*",
#	"HLT_PAFullTracks_Multiplicity185_*",
#	"HLT_PAFullTracks_Multiplicity220_v*",
#	"HLT_PAFullTracks_Multiplicity250_v*",
#	"HLT_PAFullTracks_Multiplicity280_v*",
]
process.hltHM120.andOr = cms.bool(True)
process.hltHM120.throw = cms.bool(False)

process.hltHM150 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltHM150.HLTPaths = [
	"HLT_PAFullTracks_Multiplicity120_v*",
	"HLT_PAFullTracks_Multiplicity150_v*",
#	"HLT_PAFullTracks_Multiplicity185_*",
#	"HLT_PAFullTracks_Multiplicity220_v*",
#	"HLT_PAFullTracks_Multiplicity250_v*",
#	"HLT_PAFullTracks_Multiplicity280_v*",
]
process.hltHM150.andOr = cms.bool(True)
process.hltHM150.throw = cms.bool(False)

process.hltHM185 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltHM185.HLTPaths = [
#	"HLT_PAFullTracks_Multiplicity120_v*",
#	"HLT_PAFullTracks_Multiplicity150_v*",
	"HLT_PAFullTracks_Multiplicity185_*",
#	"HLT_PAFullTracks_Multiplicity220_v*",
#	"HLT_PAFullTracks_Multiplicity250_v*",
#	"HLT_PAFullTracks_Multiplicity280_v*",
]
process.hltHM185.andOr = cms.bool(True)
process.hltHM185.throw = cms.bool(False)

process.hltHM250 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltHM250.HLTPaths = [
#	"HLT_PAFullTracks_Multiplicity120_v*",
#	"HLT_PAFullTracks_Multiplicity150_v*",
#	"HLT_PAFullTracks_Multiplicity185_*",
#	"HLT_PAFullTracks_Multiplicity220_v*",
	"HLT_PAFullTracks_Multiplicity250_v*",
#	"HLT_PAFullTracks_Multiplicity280_v*",
]
process.hltHM250.andOr = cms.bool(True)
process.hltHM250.throw = cms.bool(False)


process.load('RecoHI.HiCentralityAlgos.CentralityFilter_cfi')
process.ppNoffFilter120 = process.centralityFilter.clone(
		selectedBins = cms.vint32(
			*range(120, 150)
			),
		BinLabel = cms.InputTag("Noff")
		)

process.ppNoffFilter150 = process.centralityFilter.clone(
		selectedBins = cms.vint32(
			*range(150, 185)
			),
		BinLabel = cms.InputTag("Noff")
		)

process.ppNoffFilter185 = process.centralityFilter.clone(
		selectedBins = cms.vint32(
			*range(185, 250)
			),
		BinLabel = cms.InputTag("Noff")
		)

process.ppNoffFilter250 = process.centralityFilter.clone(
		selectedBins = cms.vint32(
			*range(250, 600)
			),
		BinLabel = cms.InputTag("Noff")
		)

process.QWSC2_3_2_3 = cms.EDAnalyzer('QWSC',
		trackEta = cms.untracked.InputTag("QWEvent", "eta"),
		trackPt = cms.untracked.InputTag("QWEvent", "pt"),
		trackPhi = cms.untracked.InputTag("QWEvent", "phi"),
		trackWeight = cms.untracked.InputTag("QWEvent", "weight"),
		vertexZ = cms.untracked.InputTag("QWEvent", "vz"),
		centrality = cms.untracked.InputTag("Noff"),
		minvz = cms.untracked.double(-15),
		maxvz = cms.untracked.double(15),
		mineta = cms.untracked.double(-2.4),
		maxeta = cms.untracked.double(2.4),
		cmode = cms.untracked.int32(1),
		nvtx = cms.untracked.int32(100),
		harmonics = cms.untracked.vint32(2, 3, -2, -3)
		)

process.QWSC2_4_2_4 = process.QWSC2_3_2_3.clone(
		harmonics = cms.untracked.vint32(2, 4, -2, -4)
		)

process.QWSC2_5_2_5 = process.QWSC2_3_2_3.clone(
		harmonics = cms.untracked.vint32(2, 5, -2, -5)
		)

process.QWSC2_6_2_6 = process.QWSC2_3_2_3.clone(
		harmonics = cms.untracked.vint32(2, 6, -2, -6)
		)

process.QWSC3_4_3_4 = process.QWSC2_3_2_3.clone(
		harmonics = cms.untracked.vint32(3, 4, -3, -4)
		)

process.QWSC3_5_3_5 = process.QWSC2_3_2_3.clone(
		harmonics = cms.untracked.vint32(3, 5, -3, -5)
		)

process.QWSC3_6_3_6 = process.QWSC2_3_2_3.clone(
		harmonics = cms.untracked.vint32(3, 6, -3, -6)
		)

process.QWSC4_5_4_5 = process.QWSC2_3_2_3.clone(
		harmonics = cms.untracked.vint32(4, 5, -4, -5)
		)

process.QWSC4_6_4_6 = process.QWSC2_3_2_3.clone(
		harmonics = cms.untracked.vint32(4, 6, -4, -6)
		)

process.QWSC5_6_5_6 = process.QWSC2_3_2_3.clone(
		harmonics = cms.untracked.vint32(5, 6, -5, -6)
		)

process.QWSC2_2 = process.QWSC2_3_2_3.clone(
		harmonics = cms.untracked.vint32(2, -2)
		)

process.QWSC3_3 = process.QWSC2_3_2_3.clone(
		harmonics = cms.untracked.vint32(3, -3)
		)

process.QWSC4_4 = process.QWSC2_3_2_3.clone(
		harmonics = cms.untracked.vint32(4, -4)
		)

process.QWSC5_5 = process.QWSC2_3_2_3.clone(
		harmonics = cms.untracked.vint32(5, -5)
		)

process.QWSC6_6 = process.QWSC2_3_2_3.clone(
		harmonics = cms.untracked.vint32(6, -6)
		)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('sc.root')
)

process.PAprimaryVertexFilter = cms.EDFilter("VertexSelector",
    src = cms.InputTag("offlinePrimaryVertices"),
    cut = cms.string("!isFake && abs(z) <= 25 && position.Rho <= 2 && tracksSize >= 2"),
    filter = cms.bool(True), # otherwise it won't filter the events
)

process.NoScraping = cms.EDFilter("FilterOutScraping",
 applyfilter = cms.untracked.bool(True),
 debugOn = cms.untracked.bool(False),
 numtrack = cms.untracked.uint32(10),
 thresh = cms.untracked.double(0.25)
)

process.load("HeavyIonsAnalysis.Configuration.hfCoincFilter_cff")
process.load("HeavyIonsAnalysis.EventAnalysis.pileUpFilter_cff")

process.eventSelection = cms.Sequence(process.hfCoincFilter * process.PAprimaryVertexFilter * process.NoScraping * process.olvFilter_pPb8TeV_dz1p0)

process.load('pPb_HM_eff')
process.QWEvent.dzdzerror = cms.untracked.double(2.0)
process.QWEvent.d0d0error = cms.untracked.double(2.0)
process.QWEvent.pterrorpt = cms.untracked.double(0.05)
process.QWEvent.fweight = cms.untracked.InputTag('Hijing_8TeV_MB_eff_v3_tight.root')

process.vectPhi120 = process.vectPhi.clone()
process.vectPhi150 = process.vectPhi.clone()
process.vectPhi185 = process.vectPhi.clone()
process.vectPhi250 = process.vectPhi.clone()

process.vectPhiW120 = process.vectPhiW.clone()
process.vectPhiW150 = process.vectPhiW.clone()
process.vectPhiW185 = process.vectPhiW.clone()
process.vectPhiW250 = process.vectPhiW.clone()

process.vectEta120 = process.vectEta.clone()
process.vectEta150 = process.vectEta.clone()
process.vectEta185 = process.vectEta.clone()
process.vectEta250 = process.vectEta.clone()

process.vectEtaW120 = process.vectEtaW.clone()
process.vectEtaW150 = process.vectEtaW.clone()
process.vectEtaW185 = process.vectEtaW.clone()
process.vectEtaW250 = process.vectEtaW.clone()

process.vectPt120 = process.vectPt.clone()
process.vectPt150 = process.vectPt.clone()
process.vectPt185 = process.vectPt.clone()
process.vectPt250 = process.vectPt.clone()

process.vectPtW120 = process.vectPtW.clone()
process.vectPtW150 = process.vectPtW.clone()
process.vectPtW185 = process.vectPtW.clone()
process.vectPtW250 = process.vectPtW.clone()


process.mon120 = cms.Sequence( process.histNoff * process.vectPhi120 * process.vectPhiW120 * process.vectEta120 * process.vectEtaW120 * process.vectPt120 * process.vectPtW120)
process.mon150 = cms.Sequence( process.histNoff * process.vectPhi150 * process.vectPhiW150 * process.vectEta150 * process.vectEtaW150 * process.vectPt150 * process.vectPtW150)
process.mon185 = cms.Sequence( process.histNoff * process.vectPhi185 * process.vectPhiW185 * process.vectEta185 * process.vectEtaW185 * process.vectPt185 * process.vectPtW185)
process.mon250 = cms.Sequence( process.histNoff * process.vectPhi250 * process.vectPhiW250 * process.vectEta250 * process.vectEtaW250 * process.vectPt250 * process.vectPtW250)

process.ana = cms.Sequence( process.QWSC2_3_2_3 * process.QWSC2_4_2_4 * process.QWSC3_4_3_4 * process.QWSC2_5_2_5 * process.QWSC3_5_3_5 * process.QWSC4_5_4_5 * process.QWSC2_6_2_6 * process.QWSC3_6_3_6 * process.QWSC4_6_4_6 * process.QWSC5_6_5_6 * process.QWSC2_2 * process.QWSC3_3 * process.QWSC4_4 * process.QWSC5_5 * process.QWSC6_6)

process.path120 = cms.Path(process.hltHM120*process.eventSelection*process.Noff*process.ppNoffFilter120*process.QWEvent*process.ana )
process.path150 = cms.Path(process.hltHM150*process.eventSelection*process.Noff*process.ppNoffFilter150*process.QWEvent*process.ana )
process.path185 = cms.Path(process.hltHM185*process.eventSelection*process.Noff*process.ppNoffFilter185*process.QWEvent*process.ana )
process.path250 = cms.Path(process.hltHM250*process.eventSelection*process.Noff*process.ppNoffFilter250*process.QWEvent*process.ana )

process.schedule = cms.Schedule(
#	process.path120,
#	process.path150,
	process.path185,
#	process.path250,
)
