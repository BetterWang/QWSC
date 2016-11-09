import FWCore.ParameterSet.Config as cms

process = cms.Process("PCA")

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')


process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.MessageLogger.cerr.FwkReport.reportEvery = 100

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '75X_dataRun2_v13', '')

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring("file:/afs/cern.ch/user/q/qwang/work/cleanroomRun2/Ana/data/ppReco.root")
)

import HLTrigger.HLTfilters.hltHighLevel_cfi

process.hltMB = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltMB.HLTPaths = [
	"HLT_HIL1MinimumBiasHF2AND_*",
	"HLT_HIL1MinimumBiasHF1AND_*",
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


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('sc.root')
)

#process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
#process.centralityBin.Centrality = cms.InputTag("hiCentrality")
#process.centralityBin.centralityVariable = cms.string("HFtowers")

process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')
process.clusterCompatibilityFilter.clusterPars = cms.vdouble(0.0,0.006)

process.primaryVertexFilter.src = cms.InputTag("offlinePrimaryVertices")

process.eventSelection = cms.Sequence(
        process.hfCoincFilter3
        + process.primaryVertexFilter
#        + process.clusterCompatibilityFilter
)

process.load('PbPb_HIMB5_ppReco_eff')
process.load('RecoHI.HiCentralityAlgos.CentralityFilter_cfi')

process.ppRecoCentFilter = process.centralityFilter.clone(
                selectedBins = cms.vint32(
                        60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179),
                BinLabel = cms.InputTag("centralityBins")
                )

process.path2_3_2_3 = cms.Path(process.eventSelection*process.centralityBins*process.ppRecoCentFilter*process.Noff*process.QWEvent*process.QWSC2_3_2_3)

process.schedule = cms.Schedule(
	process.path2_3_2_3,
)
