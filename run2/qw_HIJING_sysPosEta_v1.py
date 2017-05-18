import FWCore.ParameterSet.Config as cms

process = cms.Process("SC")

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('GeneratorInterface.HiGenCommon.AfterBurnerGenerator_cff')


process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(20000))
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.MessageLogger.cerr.FwkReport.reportEvery = 100

#from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, '75X_dataRun2_v13', '')

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)

process.source = cms.Source("EmptySource")

process.generator = cms.EDFilter("HijingGeneratorFilter",
                                 rotateEventPlane = cms.bool(True),
                                 frame = cms.string('CMS     '),
                                 targ = cms.string('A       '),
                                 izp = cms.int32(82),
                                 bMin = cms.double(0),
                                 izt = cms.int32(82),
                                 proj = cms.string('A       '),
                                 comEnergy = cms.double(5023.0),
                                 iat = cms.int32(208),
                                 bMax = cms.double(15),
                                 iap = cms.int32(208)
                                 )

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.3 $'),
    annotation = cms.untracked.string('HIJING generator'),
    name = cms.untracked.string('$Source: QW $')
    )

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('keep *'),
    fileName = cms.untracked.string('Hijing.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

process.AftBurner.modv1 = cms.InputTag("0.0")
process.AftBurner.modv2 = cms.InputTag("fEllP_8pct_v2")
#process.AftBurner.modv2 = cms.InputTag("pBG_4pct_v2")
process.AftBurner.modv3 = cms.InputTag("0.0")
process.AftBurner.fluct_v3 = cms.double(0.0)
#process.AftBurner.modv3 = cms.InputTag("pBG_2pct_v3")
process.AftBurner.modmethod = cms.int32(2)

process.pgen = cms.Sequence(cms.SequencePlaceholder("randomEngineStateProducer")+process.AfterBurner+process.GeneInfo)

from IOMC.RandomEngine.RandomServiceHelper import RandomNumberServiceHelper
randSvc = RandomNumberServiceHelper(process.RandomNumberGeneratorService)
randSvc.populate()

process.QWAcc = cms.EDAnalyzer("QWEventAccAnalyzer",
                srcPhi = cms.untracked.InputTag("QWEvent", "phi"),
                srcEta = cms.untracked.InputTag("QWEvent", "eta"),
                srcPt = cms.untracked.InputTag("QWEvent", "pt"),
                srcWeight = cms.untracked.InputTag("QWEvent", "weight"),
                minPt = cms.untracked.double(0.3),
                maxPt = cms.untracked.double(3.)
                )

process.QWRotAcc = cms.EDAnalyzer("QWEventAccAnalyzer",
                srcPhi = cms.untracked.InputTag("QWEventRot", "phi"),
                srcEta = cms.untracked.InputTag("QWEvent", "eta"),
                srcPt = cms.untracked.InputTag("QWEvent", "pt"),
                srcWeight = cms.untracked.InputTag("QWEvent", "weight"),
                minPt = cms.untracked.double(0.3),
                maxPt = cms.untracked.double(3.)
                )

process.QWRotAccHole = cms.EDAnalyzer("QWEventAccAnalyzer",
                srcPhi = cms.untracked.InputTag("QWEventAcc", "phi"),
                srcEta = cms.untracked.InputTag("QWEventAcc", "eta"),
                srcPt = cms.untracked.InputTag("QWEventAcc", "pt"),
                srcWeight = cms.untracked.InputTag("QWEventAcc", "weight"),
                minPt = cms.untracked.double(0.3),
                maxPt = cms.untracked.double(3.)
                )


process.QWSC2 = cms.EDAnalyzer('QWSC',
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


process.QWEvent = cms.EDProducer("QWGenEventProducer",
		trackSrc  = cms.untracked.InputTag("genParticles"),
		Etamin    = cms.untracked.double(0.),
		Etamax    = cms.untracked.double(2.4),
		isPrompt  = cms.untracked.bool(False)
		)

process.QWEventRot = cms.EDProducer("QWPhiRotation",
		src  = cms.untracked.InputTag("QWEvent", "phi")
		)

process.QWEventAcc = cms.EDProducer("QWAccHole",
                srcPhi = cms.untracked.InputTag("QWEventRot", "phi"),
                srcEta = cms.untracked.InputTag("QWEvent", "eta"),
		PhiMin = cms.untracked.double(1.),
		PhiMax = cms.untracked.double(1.4),
		EtaMin = cms.untracked.double(0.),
		EtaMax = cms.untracked.double(2.4),
		srcVtag = cms.untracked.VInputTag(
			cms.InputTag("QWEvent", "pt"),
			cms.InputTag("QWEvent", "weight"),
			)
		)

process.QWHIEvent = cms.EDProducer("QWHepMCProducer",
		src = cms.untracked.InputTag("generator")
		)

process.Noff = cms.EDProducer("QWIntProducer",
		src = cms.untracked.int32(30)
		)

process.bFilter = cms.EDFilter("QWDoubleFilter",
		src = cms.untracked.InputTag("QWHIEvent", "b"),
		dmin = cms.untracked.double(5.0),
		dmax = cms.untracked.double(10.0)
		)


#process.load('PbPb_HIMB2_pixel_eff')

process.generation_step   = cms.Path(process.pgen)

process.pre_ana = cms.Sequence(process.QWHIEvent * process.bFilter * process.QWEvent * process.QWEventRot * process.QWEventAcc * process.Noff)


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
		* process.QWAcc
		* process.QWRotAcc
		* process.QWRotAccHole
		)

process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(
    		process.generation_step,
		process.ana,
#		process.RAWSIMoutput_step
)


for path in process.paths:
                getattr(process,path)._seq = process.generator * getattr(process,path)._seq

