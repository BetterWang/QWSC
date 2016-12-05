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

process.hltMB = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltMB.HLTPaths = [
	"HLT_PAL1MinimumBiasHF_OR_SinglePixelTrack_part*",
]
process.hltMB.andOr = cms.bool(True)
process.hltMB.throw = cms.bool(False)


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

#process.load("HeavyIonsAnalysis.VertexAnalysis.PAPileUpVertexFilter_cff")

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


process.ana = cms.Sequence( process.QWSC2_3_2_3 * process.QWSC2_4_2_4 * process.QWSC3_4_3_4 * process.QWSC2_5_2_5 * process.QWSC3_5_3_5 * process.QWSC4_5_4_5 * process.QWSC2_6_2_6 * process.QWSC3_6_3_6 * process.QWSC4_6_4_6 * process.QWSC5_6_5_6 * process.QWSC2_2 * process.QWSC3_3 * process.QWSC4_4 * process.QWSC5_5 * process.QWSC6_6)

process.path = cms.Path(process.hltMB*process.eventSelection*process.Noff*process.QWEvent*process.ana * process.vectMonW)

process.schedule = cms.Schedule(
	process.path,
)
