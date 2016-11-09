import FWCore.ParameterSet.Config as cms

process = cms.Process("PCA")

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')


process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.MessageLogger.cerr.FwkReport.reportEvery = 100

#from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, '75X_dataRun2_v13', '')

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring("file:/afs/cern.ch/user/q/qwang/work/cleanroom2/CMSSW_5_3_20/pPb_HM_1000_1_Bgt.root")
)

import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltHM100 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltHM100.HLTPaths = [
        "HLT_PAPixelTracks_Multiplicity100_v*",
#       "HLT_PAPixelTracks_Multiplicity130_v*",
#       "HLT_PAPixelTracks_Multiplicity160_v*",
#       "HLT_PAPixelTracks_Multiplicity190_v*",
#       "HLT_PAPixelTracks_Multiplicity220_v*"
]
process.hltHM100.andOr = cms.bool(True)
process.hltHM100.throw = cms.bool(False)

process.hltHM130 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltHM130.HLTPaths = [
        "HLT_PAPixelTracks_Multiplicity100_v*",
        "HLT_PAPixelTracks_Multiplicity130_v*",
#       "HLT_PAPixelTracks_Multiplicity160_v*",
##      "HLT_PAPixelTracks_Multiplicity190_v*",
#       "HLT_PAPixelTracks_Multiplicity220_v*"
]
process.hltHM130.andOr = cms.bool(True)
process.hltHM130.throw = cms.bool(False)


process.hltHM160 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltHM160.HLTPaths = [
        "HLT_PAPixelTracks_Multiplicity100_v*",
        "HLT_PAPixelTracks_Multiplicity130_v*",
        "HLT_PAPixelTracks_Multiplicity160_v*",
#       "HLT_PAPixelTracks_Multiplicity190_v*",
#       "HLT_PAPixelTracks_Multiplicity220_v*"
]
process.hltHM160.andOr = cms.bool(True)
process.hltHM160.throw = cms.bool(False)




process.hltHM190 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltHM190.HLTPaths = [
        "HLT_PAPixelTracks_Multiplicity100_v*",
        "HLT_PAPixelTracks_Multiplicity130_v*",
        "HLT_PAPixelTracks_Multiplicity160_v*",
        "HLT_PAPixelTracks_Multiplicity190_v*",
#       "HLT_PAPixelTracks_Multiplicity220_v*"
]
process.hltHM190.andOr = cms.bool(True)
process.hltHM190.throw = cms.bool(False)


process.hltHM220 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltHM220.HLTPaths = [
        "HLT_PAPixelTracks_Multiplicity100_v*",
        "HLT_PAPixelTracks_Multiplicity130_v*",
        "HLT_PAPixelTracks_Multiplicity160_v*",
        "HLT_PAPixelTracks_Multiplicity190_v*",
        "HLT_PAPixelTracks_Multiplicity220_v*"
]
process.hltHM220.andOr = cms.bool(True)
process.hltHM220.throw = cms.bool(False)

process.NoffFilter100 = cms.EDFilter("QWIntFilter",
	selectedBins = cms.vint32(120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149),
	BinLabel = cms.InputTag("Noff")
	)

process.NoffFilter130 = cms.EDFilter("QWIntFilter",
	selectedBins = cms.vint32(
		150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184),
	BinLabel = cms.InputTag("Noff")
	)

process.NoffFilter160 = cms.EDFilter("QWIntFilter",
	selectedBins = cms.vint32(
		185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219),
	BinLabel = cms.InputTag("Noff")
	)

process.NoffFilter190 = cms.EDFilter("QWIntFilter",
	selectedBins = cms.vint32(
		220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259),
	BinLabel = cms.InputTag("Noff")
	)

process.NoffFilter220 = cms.EDFilter("QWIntFilter",
	selectedBins = cms.vint32(
		260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,
		311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349),
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


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('sc.root')
)


process.load('pPb_HM_eff')

process.path100_2_3_2_3 = cms.Path(process.hltHM100*process.Noff*process.NoffFilter100*process.QWEvent*process.QWSC2_3_2_3)
process.path130_2_3_2_3 = cms.Path(process.hltHM130*process.Noff*process.NoffFilter130*process.QWEvent*process.QWSC2_3_2_3)
process.path160_2_3_2_3 = cms.Path(process.hltHM160*process.Noff*process.NoffFilter160*process.QWEvent*process.QWSC2_3_2_3)
process.path190_2_3_2_3 = cms.Path(process.hltHM190*process.Noff*process.NoffFilter190*process.QWEvent*process.QWSC2_3_2_3)
process.path220_2_3_2_3 = cms.Path(process.hltHM220*process.Noff*process.NoffFilter220*process.QWEvent*process.QWSC2_3_2_3)

process.path100_2_4_2_4 = cms.Path(process.hltHM100*process.Noff*process.NoffFilter100*process.QWEvent*process.QWSC2_4_2_4)
process.path130_2_4_2_4 = cms.Path(process.hltHM130*process.Noff*process.NoffFilter130*process.QWEvent*process.QWSC2_4_2_4)
process.path160_2_4_2_4 = cms.Path(process.hltHM160*process.Noff*process.NoffFilter160*process.QWEvent*process.QWSC2_4_2_4)
process.path190_2_4_2_4 = cms.Path(process.hltHM190*process.Noff*process.NoffFilter190*process.QWEvent*process.QWSC2_4_2_4)
process.path220_2_4_2_4 = cms.Path(process.hltHM220*process.Noff*process.NoffFilter220*process.QWEvent*process.QWSC2_4_2_4)

process.path100_2_5_2_5 = cms.Path(process.hltHM100*process.Noff*process.NoffFilter100*process.QWEvent*process.QWSC2_5_2_5)
process.path130_2_5_2_5 = cms.Path(process.hltHM130*process.Noff*process.NoffFilter130*process.QWEvent*process.QWSC2_5_2_5)
process.path160_2_5_2_5 = cms.Path(process.hltHM160*process.Noff*process.NoffFilter160*process.QWEvent*process.QWSC2_5_2_5)
process.path190_2_5_2_5 = cms.Path(process.hltHM190*process.Noff*process.NoffFilter190*process.QWEvent*process.QWSC2_5_2_5)
process.path220_2_5_2_5 = cms.Path(process.hltHM220*process.Noff*process.NoffFilter220*process.QWEvent*process.QWSC2_5_2_5)

process.path100_2_6_2_6 = cms.Path(process.hltHM100*process.Noff*process.NoffFilter100*process.QWEvent*process.QWSC2_6_2_6)
process.path130_2_6_2_6 = cms.Path(process.hltHM130*process.Noff*process.NoffFilter130*process.QWEvent*process.QWSC2_6_2_6)
process.path160_2_6_2_6 = cms.Path(process.hltHM160*process.Noff*process.NoffFilter160*process.QWEvent*process.QWSC2_6_2_6)
process.path190_2_6_2_6 = cms.Path(process.hltHM190*process.Noff*process.NoffFilter190*process.QWEvent*process.QWSC2_6_2_6)
process.path220_2_6_2_6 = cms.Path(process.hltHM220*process.Noff*process.NoffFilter220*process.QWEvent*process.QWSC2_6_2_6)

process.path100_3_4_3_4 = cms.Path(process.hltHM100*process.Noff*process.NoffFilter100*process.QWEvent*process.QWSC3_4_3_4)
process.path130_3_4_3_4 = cms.Path(process.hltHM130*process.Noff*process.NoffFilter130*process.QWEvent*process.QWSC3_4_3_4)
process.path160_3_4_3_4 = cms.Path(process.hltHM160*process.Noff*process.NoffFilter160*process.QWEvent*process.QWSC3_4_3_4)
process.path190_3_4_3_4 = cms.Path(process.hltHM190*process.Noff*process.NoffFilter190*process.QWEvent*process.QWSC3_4_3_4)
process.path220_3_4_3_4 = cms.Path(process.hltHM220*process.Noff*process.NoffFilter220*process.QWEvent*process.QWSC3_4_3_4)

process.path100_3_5_3_5 = cms.Path(process.hltHM100*process.Noff*process.NoffFilter100*process.QWEvent*process.QWSC3_5_3_5)
process.path130_3_5_3_5 = cms.Path(process.hltHM130*process.Noff*process.NoffFilter130*process.QWEvent*process.QWSC3_5_3_5)
process.path160_3_5_3_5 = cms.Path(process.hltHM160*process.Noff*process.NoffFilter160*process.QWEvent*process.QWSC3_5_3_5)
process.path190_3_5_3_5 = cms.Path(process.hltHM190*process.Noff*process.NoffFilter190*process.QWEvent*process.QWSC3_5_3_5)
process.path220_3_5_3_5 = cms.Path(process.hltHM220*process.Noff*process.NoffFilter220*process.QWEvent*process.QWSC3_5_3_5)

process.path100_3_6_3_6 = cms.Path(process.hltHM100*process.Noff*process.NoffFilter100*process.QWEvent*process.QWSC3_6_3_6)
process.path130_3_6_3_6 = cms.Path(process.hltHM130*process.Noff*process.NoffFilter130*process.QWEvent*process.QWSC3_6_3_6)
process.path160_3_6_3_6 = cms.Path(process.hltHM160*process.Noff*process.NoffFilter160*process.QWEvent*process.QWSC3_6_3_6)
process.path190_3_6_3_6 = cms.Path(process.hltHM190*process.Noff*process.NoffFilter190*process.QWEvent*process.QWSC3_6_3_6)
process.path220_3_6_3_6 = cms.Path(process.hltHM220*process.Noff*process.NoffFilter220*process.QWEvent*process.QWSC3_6_3_6)

process.path100_4_5_4_5 = cms.Path(process.hltHM100*process.Noff*process.NoffFilter100*process.QWEvent*process.QWSC4_5_4_5)
process.path130_4_5_4_5 = cms.Path(process.hltHM130*process.Noff*process.NoffFilter130*process.QWEvent*process.QWSC4_5_4_5)
process.path160_4_5_4_5 = cms.Path(process.hltHM160*process.Noff*process.NoffFilter160*process.QWEvent*process.QWSC4_5_4_5)
process.path190_4_5_4_5 = cms.Path(process.hltHM190*process.Noff*process.NoffFilter190*process.QWEvent*process.QWSC4_5_4_5)
process.path220_4_5_4_5 = cms.Path(process.hltHM220*process.Noff*process.NoffFilter220*process.QWEvent*process.QWSC4_5_4_5)

process.path100_4_6_4_6 = cms.Path(process.hltHM100*process.Noff*process.NoffFilter100*process.QWEvent*process.QWSC4_6_4_6)
process.path130_4_6_4_6 = cms.Path(process.hltHM130*process.Noff*process.NoffFilter130*process.QWEvent*process.QWSC4_6_4_6)
process.path160_4_6_4_6 = cms.Path(process.hltHM160*process.Noff*process.NoffFilter160*process.QWEvent*process.QWSC4_6_4_6)
process.path190_4_6_4_6 = cms.Path(process.hltHM190*process.Noff*process.NoffFilter190*process.QWEvent*process.QWSC4_6_4_6)
process.path220_4_6_4_6 = cms.Path(process.hltHM220*process.Noff*process.NoffFilter220*process.QWEvent*process.QWSC4_6_4_6)

process.path100_5_6_5_6 = cms.Path(process.hltHM100*process.Noff*process.NoffFilter100*process.QWEvent*process.QWSC5_6_5_6)
process.path130_5_6_5_6 = cms.Path(process.hltHM130*process.Noff*process.NoffFilter130*process.QWEvent*process.QWSC5_6_5_6)
process.path160_5_6_5_6 = cms.Path(process.hltHM160*process.Noff*process.NoffFilter160*process.QWEvent*process.QWSC5_6_5_6)
process.path190_5_6_5_6 = cms.Path(process.hltHM190*process.Noff*process.NoffFilter190*process.QWEvent*process.QWSC5_6_5_6)
process.path220_5_6_5_6 = cms.Path(process.hltHM220*process.Noff*process.NoffFilter220*process.QWEvent*process.QWSC5_6_5_6)

process.schedule = cms.Schedule(
	process.path100_2_3_2_3,
	process.path130_2_3_2_3,
	process.path160_2_3_2_3,
	process.path190_2_3_2_3,
	process.path220_2_3_2_3,
	process.path100_2_4_2_4,
	process.path130_2_4_2_4,
	process.path160_2_4_2_4,
	process.path190_2_4_2_4,
	process.path220_2_4_2_4,
	process.path100_2_5_2_5,
	process.path130_2_5_2_5,
	process.path160_2_5_2_5,
	process.path190_2_5_2_5,
	process.path220_2_5_2_5,
	process.path100_2_6_2_6,
	process.path130_2_6_2_6,
	process.path160_2_6_2_6,
	process.path190_2_6_2_6,
	process.path220_2_6_2_6,
	process.path100_3_4_3_4,
	process.path130_3_4_3_4,
	process.path160_3_4_3_4,
	process.path190_3_4_3_4,
	process.path220_3_4_3_4,
	process.path100_3_5_3_5,
	process.path130_3_5_3_5,
	process.path160_3_5_3_5,
	process.path190_3_5_3_5,
	process.path220_3_5_3_5,
	process.path100_3_6_3_6,
	process.path130_3_6_3_6,
	process.path160_3_6_3_6,
	process.path190_3_6_3_6,
	process.path220_3_6_3_6,
	process.path100_4_5_4_5,
	process.path130_4_5_4_5,
	process.path160_4_5_4_5,
	process.path190_4_5_4_5,
	process.path220_4_5_4_5,
	process.path100_4_6_4_6,
	process.path130_4_6_4_6,
	process.path160_4_6_4_6,
	process.path190_4_6_4_6,
	process.path220_4_6_4_6,
	process.path100_5_6_5_6,
	process.path130_5_6_5_6,
	process.path160_5_6_5_6,
	process.path190_5_6_5_6,
	process.path220_5_6_5_6,
)
