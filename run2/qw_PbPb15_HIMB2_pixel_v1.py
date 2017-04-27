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
	fileNames = cms.untracked.vstring("file:/afs/cern.ch/user/q/qwang/work/cleanroomRun2/Ana/data/pixeltracking_1.root")
)

import HLTrigger.HLTfilters.hltHighLevel_cfi

process.hltMB = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltMB.HLTPaths = [
	"HLT_HIL1MinimumBiasHF2AND_*",
	"HLT_HIL1MinimumBiasHF1AND_*",
]

process.hltMB.andOr = cms.bool(True)
process.hltMB.throw = cms.bool(False)

process.QWSC2 = cms.EDAnalyzer('QWSC',
		trackEta = cms.untracked.InputTag("QWEvent", "eta"),
		trackPt = cms.untracked.InputTag("QWEvent", "pt"),
		trackPhi = cms.untracked.InputTag("QWEvent", "phi"),
		trackWeight = cms.untracked.InputTag("QWEvent", "weight"),
		vertexZ = cms.untracked.InputTag("QWEvent", "vz"),
		centrality = cms.untracked.InputTag("centralityBin", "HFtowers"),
		minvz = cms.untracked.double(-15),
		maxvz = cms.untracked.double(15),
		mineta = cms.untracked.double(-2.4),
		maxeta = cms.untracked.double(2.4),
		cmode = cms.untracked.int32(1),
		nvtx = cms.untracked.int32(100),
		harmonics = cms.untracked.vint32(2)
		)

# 1-part
process.QWSC3 = process.QWSC2.clone( harmonics = cms.untracked.vint32(3) )
process.QWSC4 = process.QWSC2.clone( harmonics = cms.untracked.vint32(4) )

# 2-part n=2
process.QWSC22  = process.QWSC2.clone( harmonics = cms.untracked.vint32(2,  2) )
process.QWSC2_2 = process.QWSC2.clone( harmonics = cms.untracked.vint32(2, -2) )
# n=3
process.QWSC33  = process.QWSC2.clone( harmonics = cms.untracked.vint32(3,  3) )
process.QWSC3_3 = process.QWSC2.clone( harmonics = cms.untracked.vint32(3, -3) )
# n=4
process.QWSC44  = process.QWSC2.clone( harmonics = cms.untracked.vint32(4,  4) )
process.QWSC4_4 = process.QWSC2.clone( harmonics = cms.untracked.vint32(4, -4) )

# 3-part n=2
process.QWSC222  = process.QWSC2.clone( harmonics = cms.untracked.vint32(2,  2,  2) )
process.QWSC22_2 = process.QWSC2.clone( harmonics = cms.untracked.vint32(2,  2, -2) )
# n=3
process.QWSC333  = process.QWSC2.clone( harmonics = cms.untracked.vint32(3,  3,  3) )
process.QWSC33_3 = process.QWSC2.clone( harmonics = cms.untracked.vint32(3,  3, -3) )
# n=4
process.QWSC444  = process.QWSC2.clone( harmonics = cms.untracked.vint32(4,  4,  4) )
process.QWSC44_4 = process.QWSC2.clone( harmonics = cms.untracked.vint32(4,  4, -4) )

# 4-part n=2
process.QWSC2222  = process.QWSC2.clone( harmonics = cms.untracked.vint32(2,  2,  2,  2) )
process.QWSC222_2 = process.QWSC2.clone( harmonics = cms.untracked.vint32(2,  2,  2, -2) )
process.QWSC22_2_2= process.QWSC2.clone( harmonics = cms.untracked.vint32(2,  2, -2, -2) )
# n=3
process.QWSC3333  = process.QWSC2.clone( harmonics = cms.untracked.vint32(3,  3,  3,  3) )
process.QWSC333_3 = process.QWSC2.clone( harmonics = cms.untracked.vint32(3,  3,  3, -3) )
process.QWSC33_3_3= process.QWSC2.clone( harmonics = cms.untracked.vint32(3,  3, -3, -3) )
# n=4
process.QWSC4444  = process.QWSC2.clone( harmonics = cms.untracked.vint32(4,  4,  4,  4) )
process.QWSC444_4 = process.QWSC2.clone( harmonics = cms.untracked.vint32(4,  4,  4, -4) )
process.QWSC44_4_4= process.QWSC2.clone( harmonics = cms.untracked.vint32(4,  4, -4, -4) )

# 5-part n=2
process.QWSC22222  = process.QWSC2.clone( harmonics = cms.untracked.vint32(2, 2,  2,  2,  2) )
process.QWSC2222_2 = process.QWSC2.clone( harmonics = cms.untracked.vint32(2, 2,  2,  2, -2) )
process.QWSC222_2_2= process.QWSC2.clone( harmonics = cms.untracked.vint32(2, 2,  2, -2, -2) )
# n=3
process.QWSC33333  = process.QWSC2.clone( harmonics = cms.untracked.vint32(3, 3,  3,  3,  3) )
process.QWSC3333_3 = process.QWSC2.clone( harmonics = cms.untracked.vint32(3, 3,  3,  3, -3) )
process.QWSC333_3_3= process.QWSC2.clone( harmonics = cms.untracked.vint32(3, 3,  3, -3, -3) )
# n=4
process.QWSC44444  = process.QWSC2.clone( harmonics = cms.untracked.vint32(4, 4,  4,  4,  4) )
process.QWSC4444_4 = process.QWSC2.clone( harmonics = cms.untracked.vint32(4, 4,  4,  4, -4) )
process.QWSC444_4_4= process.QWSC2.clone( harmonics = cms.untracked.vint32(4, 4,  4, -4, -4) )

# 6-part n=2
process.QWSC222222   = process.QWSC2.clone( harmonics = cms.untracked.vint32(2, 2, 2,  2,  2,  2) )
process.QWSC22222_2  = process.QWSC2.clone( harmonics = cms.untracked.vint32(2, 2, 2,  2,  2, -2) )
process.QWSC2222_2_2 = process.QWSC2.clone( harmonics = cms.untracked.vint32(2, 2, 2,  2, -2, -2) )
process.QWSC222_2_2_2= process.QWSC2.clone( harmonics = cms.untracked.vint32(2, 2, 2, -2, -2, -2) )
# n=3
process.QWSC333333   = process.QWSC2.clone( harmonics = cms.untracked.vint32(3, 3, 3,  3,  3,  3) )
process.QWSC33333_3  = process.QWSC2.clone( harmonics = cms.untracked.vint32(3, 3, 3,  3,  3, -3) )
process.QWSC3333_3_3 = process.QWSC2.clone( harmonics = cms.untracked.vint32(3, 3, 3,  3, -3, -3) )
process.QWSC333_3_3_3= process.QWSC2.clone( harmonics = cms.untracked.vint32(3, 3, 3, -3, -3, -3) )
# n=4
process.QWSC444444   = process.QWSC2.clone( harmonics = cms.untracked.vint32(4, 4, 4,  4,  4,  4) )
process.QWSC44444_4  = process.QWSC2.clone( harmonics = cms.untracked.vint32(4, 4, 4,  4,  4, -4) )
process.QWSC4444_4_4 = process.QWSC2.clone( harmonics = cms.untracked.vint32(4, 4, 4,  4, -4, -4) )
process.QWSC444_4_4_4= process.QWSC2.clone( harmonics = cms.untracked.vint32(4, 4, 4, -4, -4, -4) )

# 7-part n=2
process.QWSC2222222   = process.QWSC2.clone( harmonics = cms.untracked.vint32(2, 2, 2, 2,  2,  2,  2) )
process.QWSC222222_2  = process.QWSC2.clone( harmonics = cms.untracked.vint32(2, 2, 2, 2,  2,  2, -2) )
process.QWSC22222_2_2 = process.QWSC2.clone( harmonics = cms.untracked.vint32(2, 2, 2, 2,  2, -2, -2) )
process.QWSC2222_2_2_2= process.QWSC2.clone( harmonics = cms.untracked.vint32(2, 2, 2, 2, -2, -2, -2) )
# n=3
process.QWSC3333333   = process.QWSC2.clone( harmonics = cms.untracked.vint32(3, 3, 3, 3,  3,  3,  3) )
process.QWSC333333_3  = process.QWSC2.clone( harmonics = cms.untracked.vint32(3, 3, 3, 3,  3,  3, -3) )
process.QWSC33333_3_3 = process.QWSC2.clone( harmonics = cms.untracked.vint32(3, 3, 3, 3,  3, -3, -3) )
process.QWSC3333_3_3_3= process.QWSC2.clone( harmonics = cms.untracked.vint32(3, 3, 3, 3, -3, -3, -3) )
# n=4
process.QWSC4444444   = process.QWSC2.clone( harmonics = cms.untracked.vint32(4, 4, 4, 4,  4,  4,  4) )
process.QWSC444444_4  = process.QWSC2.clone( harmonics = cms.untracked.vint32(4, 4, 4, 4,  4,  4, -4) )
process.QWSC44444_4_4 = process.QWSC2.clone( harmonics = cms.untracked.vint32(4, 4, 4, 4,  4, -4, -4) )
process.QWSC4444_4_4_4= process.QWSC2.clone( harmonics = cms.untracked.vint32(4, 4, 4, 4, -4, -4, -4) )

# 8-part n=2
process.QWSC22222222    = process.QWSC2.clone( harmonics = cms.untracked.vint32(2, 2, 2, 2, 2,  2,  2,  2) )
process.QWSC2222222_2   = process.QWSC2.clone( harmonics = cms.untracked.vint32(2, 2, 2, 2, 2,  2,  2, -2) )
process.QWSC222222_2_2  = process.QWSC2.clone( harmonics = cms.untracked.vint32(2, 2, 2, 2, 2,  2, -2, -2) )
process.QWSC22222_2_2_2 = process.QWSC2.clone( harmonics = cms.untracked.vint32(2, 2, 2, 2, 2, -2, -2, -2) )
process.QWSC2222_2_2_2_2= process.QWSC2.clone( harmonics = cms.untracked.vint32(2, 2, 2, 2,-2, -2, -2, -2) )
# n=3
process.QWSC33333333    = process.QWSC2.clone( harmonics = cms.untracked.vint32(3, 3, 3, 3, 3,  3,  3,  3) )
process.QWSC3333333_3   = process.QWSC2.clone( harmonics = cms.untracked.vint32(3, 3, 3, 3, 3,  3,  3, -3) )
process.QWSC333333_3_3  = process.QWSC2.clone( harmonics = cms.untracked.vint32(3, 3, 3, 3, 3,  3, -3, -3) )
process.QWSC33333_3_3_3 = process.QWSC2.clone( harmonics = cms.untracked.vint32(3, 3, 3, 3, 3, -3, -3, -3) )
process.QWSC3333_3_3_3_3= process.QWSC2.clone( harmonics = cms.untracked.vint32(3, 3, 3, 3,-3, -3, -3, -3) )
# n=4
process.QWSC44444444    = process.QWSC2.clone( harmonics = cms.untracked.vint32(4, 4, 4, 4, 4,  4,  4,  4) )
process.QWSC4444444_4   = process.QWSC2.clone( harmonics = cms.untracked.vint32(4, 4, 4, 4, 4,  4,  4, -4) )
process.QWSC444444_4_4  = process.QWSC2.clone( harmonics = cms.untracked.vint32(4, 4, 4, 4, 4,  4, -4, -4) )
process.QWSC44444_4_4_4 = process.QWSC2.clone( harmonics = cms.untracked.vint32(4, 4, 4, 4, 4, -4, -4, -4) )
process.QWSC4444_4_4_4_4= process.QWSC2.clone( harmonics = cms.untracked.vint32(4, 4, 4, 4,-4, -4, -4, -4) )





process.TFileService = cms.Service("TFileService",
    fileName = cms.string('sc.root')
)


process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')
process.clusterCompatibilityFilter.clusterPars = cms.vdouble(0.0,0.006)

process.eventSelection = cms.Sequence(
        process.hfCoincFilter3
        + process.primaryVertexFilter
        + process.clusterCompatibilityFilter
)


process.load('PbPb_HIMB2_pixel_eff')

process.pre_ana = cms.Sequence(process.hltMB*process.eventSelection*process.makeEvent)

process.ana = cms.Path(process.pre_ana 
		* process.QWSC2
		* process.QWSC3
		* process.QWSC4

		* process.QWSC22
		* process.QWSC2_2
		* process.QWSC33
		* process.QWSC3_3
		* process.QWSC44
		* process.QWSC4_4

		* process.QWSC222
		* process.QWSC22_2
		* process.QWSC333
		* process.QWSC33_3
		* process.QWSC444
		* process.QWSC44_4

		* process.QWSC2222
		* process.QWSC222_2
		* process.QWSC22_2_2
		* process.QWSC3333
		* process.QWSC333_3
		* process.QWSC33_3_3
		* process.QWSC4444
		* process.QWSC444_4
		* process.QWSC44_4_4

		* process.QWSC22222
		* process.QWSC2222_2
		* process.QWSC222_2_2
		* process.QWSC33333
		* process.QWSC3333_3
		* process.QWSC333_3_3
		* process.QWSC44444
		* process.QWSC4444_4
		* process.QWSC444_4_4

		* process.QWSC222222
		* process.QWSC22222_2
		* process.QWSC2222_2_2
		* process.QWSC222_2_2_2
		* process.QWSC333333
		* process.QWSC33333_3
		* process.QWSC3333_3_3
		* process.QWSC333_3_3_3
		* process.QWSC444444
		* process.QWSC44444_4
		* process.QWSC4444_4_4
		* process.QWSC444_4_4_4

		* process.QWSC2222222
		* process.QWSC222222_2
		* process.QWSC22222_2_2
		* process.QWSC2222_2_2_2
		* process.QWSC3333333
		* process.QWSC333333_3
		* process.QWSC33333_3_3
		* process.QWSC3333_3_3_3
		* process.QWSC4444444
		* process.QWSC444444_4
		* process.QWSC44444_4_4
		* process.QWSC4444_4_4_4

		* process.QWSC22222222
		* process.QWSC2222222_2
		* process.QWSC222222_2_2
		* process.QWSC22222_2_2_2
		* process.QWSC2222_2_2_2_2
		* process.QWSC33333333
		* process.QWSC3333333_3
		* process.QWSC333333_3_3
		* process.QWSC33333_3_3_3
		* process.QWSC3333_3_3_3_3
		* process.QWSC44444444
		* process.QWSC4444444_4
		* process.QWSC444444_4_4
		* process.QWSC44444_4_4_4
		* process.QWSC4444_4_4_4_4
		)

process.schedule = cms.Schedule(
		process.ana
)
