import FWCore.ParameterSet.Config as cms

process = cms.Process("PCA")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:/afs/cern.ch/user/q/qwang/work/cleanroomRun2/Ana/data/pixeltracking_1.root')
)
process.MEtoEDMConverter = cms.EDProducer("MEtoEDMConverter",
    Frequency = cms.untracked.int32(50),
    MEPathToSave = cms.untracked.string(''),
    Name = cms.untracked.string('MEtoEDMConverter'),
    Verbosity = cms.untracked.int32(0),
    deleteAfterCopy = cms.untracked.bool(True)
)


process.QWEvent = cms.EDProducer("QWEventProducer",
    Etamax = cms.untracked.double(2.4),
    Etamin = cms.untracked.double(-2.4),
    centralitySrc = cms.untracked.InputTag("centralityBin","HFtowers"),
    d0d0error = cms.untracked.double(3.0),
    dzdzerror = cms.untracked.double(3.0),
    fweight = cms.untracked.InputTag("EffCorrectionsPixel_TT_pt_0_10_v2.root"),
    ptMax = cms.untracked.double(3.0),
    ptMin = cms.untracked.double(0.3),
    pterrorpt = cms.untracked.double(0.1),
    trackSrc = cms.untracked.InputTag("hiGeneralAndPixelTracks"),
    vertexSrc = cms.untracked.InputTag("hiSelectedVertex")
)


process.centralityBin = cms.EDProducer("CentralityBinProducer",
    Centrality = cms.InputTag("hiCentrality"),
    centralityVariable = cms.string('HFtowers'),
    nonDefaultGlauberModel = cms.string(''),
    pPbRunFlip = cms.uint32(99999999)
)


process.randomEngineStateProducer = cms.EDProducer("RandomEngineStateProducer")


process.siPixelRecHits = cms.EDProducer("SiPixelRecHitConverter",
    CPE = cms.string('PixelCPEGeneric'),
    VerboseLevel = cms.untracked.int32(0),
    src = cms.InputTag("siPixelClusters")
)


process.siPixelRecHitsPreSplitting = cms.EDProducer("SiPixelRecHitConverter",
    CPE = cms.string('PixelCPEGeneric'),
    VerboseLevel = cms.untracked.int32(0),
    src = cms.InputTag("siPixelClustersPreSplitting")
)


process.towersAboveThreshold = cms.EDProducer("CaloTowerCandidateCreator",
    minimumE = cms.double(3.0),
    minimumEt = cms.double(0.0),
    src = cms.InputTag("towerMaker"),
    verbose = cms.untracked.int32(0)
)


process.clusterCompatibilityFilter = cms.EDFilter("HIClusterCompatibilityFilter",
    cluscomSrc = cms.InputTag("hiClusterCompatibility"),
    clusterPars = cms.vdouble(0.0, 0.006),
    clusterTrunc = cms.double(2.0),
    maxZ = cms.double(20.05),
    minZ = cms.double(-20.0),
    nhitsTrunc = cms.int32(150)
)


process.hfNegFilter = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("hfNegTowers")
)


process.hfNegFilter2 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(2),
    src = cms.InputTag("hfNegTowers")
)


process.hfNegFilter3 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(3),
    src = cms.InputTag("hfNegTowers")
)


process.hfNegFilter4 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(4),
    src = cms.InputTag("hfNegTowers")
)


process.hfNegFilter5 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(5),
    src = cms.InputTag("hfNegTowers")
)


process.hfNegTowers = cms.EDFilter("EtaPtMinCandSelector",
    etaMax = cms.double(-3.0),
    etaMin = cms.double(-6.0),
    ptMin = cms.double(0),
    src = cms.InputTag("towersAboveThreshold")
)


process.hfPosFilter = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("hfPosTowers")
)


process.hfPosFilter2 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(2),
    src = cms.InputTag("hfPosTowers")
)


process.hfPosFilter3 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(3),
    src = cms.InputTag("hfPosTowers")
)


process.hfPosFilter4 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(4),
    src = cms.InputTag("hfPosTowers")
)


process.hfPosFilter5 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(5),
    src = cms.InputTag("hfPosTowers")
)


process.hfPosTowers = cms.EDFilter("EtaPtMinCandSelector",
    etaMax = cms.double(6.0),
    etaMin = cms.double(3.0),
    ptMin = cms.double(0),
    src = cms.InputTag("towersAboveThreshold")
)


process.hltLevel1GTSeed = cms.EDFilter("HLTLevel1GTSeed",
    L1CollectionsTag = cms.InputTag("l1extraParticles"),
    L1GtObjectMapTag = cms.InputTag("l1GtObjectMap"),
    L1GtReadoutRecordTag = cms.InputTag("gtDigis"),
    L1MuonCollectionTag = cms.InputTag("l1extraParticles"),
    L1NrBxInEvent = cms.int32(3),
    L1SeedsLogicalExpression = cms.string(''),
    L1TechTriggerSeeding = cms.bool(False),
    L1UseAliasesForSeeding = cms.bool(True),
    L1UseL1TriggerObjectMaps = cms.bool(True),
    saveTags = cms.bool(False)
)


process.hltMB = cms.EDFilter("HLTHighLevel",
    HLTPaths = cms.vstring('HLT_HIL1MinimumBiasHF2AND_*', 
        'HLT_HIL1MinimumBiasHF1AND_*'),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    andOr = cms.bool(True),
    eventSetupPathsKey = cms.string(''),
    throw = cms.bool(False)
)


process.hltPixelClusterShapeFilter = cms.EDFilter("HLTPixelClusterShapeFilter",
    clusterPars = cms.vdouble(0, 0.0045),
    clusterTrunc = cms.double(2),
    inputTag = cms.InputTag("siPixelRecHits"),
    maxZ = cms.double(20.05),
    minZ = cms.double(-20),
    nhitsTrunc = cms.int32(150),
    saveTags = cms.bool(False),
    zStep = cms.double(0.2)
)


process.noBSChalo = cms.EDFilter("HLTLevel1GTSeed",
    L1CollectionsTag = cms.InputTag("l1extraParticles"),
    L1GtObjectMapTag = cms.InputTag("l1GtObjectMap"),
    L1GtReadoutRecordTag = cms.InputTag("gtDigis"),
    L1MuonCollectionTag = cms.InputTag("l1extraParticles"),
    L1NrBxInEvent = cms.int32(3),
    L1SeedsLogicalExpression = cms.string('NOT (36 OR 37 OR 38 OR 39)'),
    L1TechTriggerSeeding = cms.bool(True),
    L1UseAliasesForSeeding = cms.bool(True),
    L1UseL1TriggerObjectMaps = cms.bool(True),
    saveTags = cms.bool(False)
)


process.primaryVertexFilter = cms.EDFilter("VertexSelector",
    cut = cms.string('!isFake && abs(z) <= 25 && position.Rho <= 2 && tracksSize >= 2'),
    filter = cms.bool(True),
    src = cms.InputTag("hiSelectedVertex")
)


process.MEtoMEComparitor = cms.EDAnalyzer("MEtoMEComparitor",
    Diffgoodness = cms.double(0.1),
    KSgoodness = cms.double(0.9),
    MEtoEDMLabel = cms.string('MEtoEDMConverter'),
    OverAllgoodness = cms.double(0.9),
    autoProcess = cms.bool(True),
    dirDepth = cms.uint32(1),
    lumiInstance = cms.string('MEtoEDMConverterLumi'),
    processNew = cms.string('RERECO'),
    processRef = cms.string('HLT'),
    runInstance = cms.string('MEtoEDMConverterRun')
)


process.QWSC2 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(2),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC22 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(2, 2),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC222 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(2, 2, 2),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC2222 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(2, 2, 2, 2),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC22222 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(2, 2, 2, 2, 2),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC222222 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(2, 2, 2, 2, 2, 
        2),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC2222222 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(2, 2, 2, 2, 2, 
        2, 2),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC22222222 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(2, 2, 2, 2, 2, 
        2, 2, 2),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC2222222_2 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(2, 2, 2, 2, 2, 
        2, 2, -2),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC222222_2 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(2, 2, 2, 2, 2, 
        2, -2),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC222222_2_2 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(2, 2, 2, 2, 2, 
        2, -2, -2),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC22222_2 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(2, 2, 2, 2, 2, 
        -2),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC22222_2_2 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(2, 2, 2, 2, 2, 
        -2, -2),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC22222_2_2_2 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(2, 2, 2, 2, 2, 
        -2, -2, -2),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC2222_2 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(2, 2, 2, 2, -2),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC2222_2_2 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(2, 2, 2, 2, -2, 
        -2),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC2222_2_2_2 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(2, 2, 2, 2, -2, 
        -2, -2),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC2222_2_2_2_2 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(2, 2, 2, 2, -2, 
        -2, -2, -2),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC222_2 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(2, 2, 2, -2),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC222_2_2 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(2, 2, 2, -2, -2),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC222_2_2_2 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(2, 2, 2, -2, -2, 
        -2),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC22_2 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(2, 2, -2),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC22_2_2 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(2, 2, -2, -2),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC2_2 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(2, -2),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC3 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(3),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC33 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(3, 3),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC333 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(3, 3, 3),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC3333 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(3, 3, 3, 3),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC33333 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(3, 3, 3, 3, 3),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC333333 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(3, 3, 3, 3, 3, 
        3),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC3333333 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(3, 3, 3, 3, 3, 
        3, 3),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC33333333 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(3, 3, 3, 3, 3, 
        3, 3, 3),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC3333333_3 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(3, 3, 3, 3, 3, 
        3, 3, -3),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC333333_3 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(3, 3, 3, 3, 3, 
        3, -3),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC333333_3_3 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(3, 3, 3, 3, 3, 
        3, -3, -3),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC33333_3 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(3, 3, 3, 3, 3, 
        -3),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC33333_3_3 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(3, 3, 3, 3, 3, 
        -3, -3),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC33333_3_3_3 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(3, 3, 3, 3, 3, 
        -3, -3, -3),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC3333_3 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(3, 3, 3, 3, -3),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC3333_3_3 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(3, 3, 3, 3, -3, 
        -3),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC3333_3_3_3 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(3, 3, 3, 3, -3, 
        -3, -3),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC3333_3_3_3_3 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(3, 3, 3, 3, -3, 
        -3, -3, -3),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC333_3 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(3, 3, 3, -3),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC333_3_3 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(3, 3, 3, -3, -3),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC333_3_3_3 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(3, 3, 3, -3, -3, 
        -3),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC33_3 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(3, 3, -3),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC33_3_3 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(3, 3, -3, -3),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC3_3 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(3, -3),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC4 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(4),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC44 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(4, 4),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC444 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(4, 4, 4),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC4444 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(4, 4, 4, 4),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC44444 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(4, 4, 4, 4, 4),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC444444 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(4, 4, 4, 4, 4, 
        4),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC4444444 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(4, 4, 4, 4, 4, 
        4, 4),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC44444444 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(4, 4, 4, 4, 4, 
        4, 4, 4),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC4444444_4 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(4, 4, 4, 4, 4, 
        4, 4, -4),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC444444_4 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(4, 4, 4, 4, 4, 
        4, -4),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC444444_4_4 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(4, 4, 4, 4, 4, 
        4, -4, -4),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC44444_4 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(4, 4, 4, 4, 4, 
        -4),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC44444_4_4 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(4, 4, 4, 4, 4, 
        -4, -4),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC44444_4_4_4 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(4, 4, 4, 4, 4, 
        -4, -4, -4),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC4444_4 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(4, 4, 4, 4, -4),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC4444_4_4 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(4, 4, 4, 4, -4, 
        -4),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC4444_4_4_4 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(4, 4, 4, 4, -4, 
        -4, -4),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC4444_4_4_4_4 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(4, 4, 4, 4, -4, 
        -4, -4, -4),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC444_4 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(4, 4, 4, -4),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC444_4_4 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(4, 4, 4, -4, -4),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC444_4_4_4 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(4, 4, 4, -4, -4, 
        -4),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC44_4 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(4, 4, -4),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC44_4_4 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(4, 4, -4, -4),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.QWSC4_4 = cms.EDAnalyzer("QWSC",
    centrality = cms.untracked.InputTag("centralityBin","HFtowers"),
    cmode = cms.untracked.int32(1),
    harmonics = cms.untracked.vint32(4, -4),
    maxeta = cms.untracked.double(2.4),
    maxvz = cms.untracked.double(15),
    mineta = cms.untracked.double(-2.4),
    minvz = cms.untracked.double(-15),
    nvtx = cms.untracked.int32(100),
    trackEta = cms.untracked.InputTag("QWEvent","eta"),
    trackPhi = cms.untracked.InputTag("QWEvent","phi"),
    trackPt = cms.untracked.InputTag("QWEvent","pt"),
    trackWeight = cms.untracked.InputTag("QWEvent","weight"),
    vertexZ = cms.untracked.InputTag("QWEvent","vz")
)


process.histNoff = cms.EDAnalyzer("QWHistAnalyzer",
    Nbins = cms.untracked.int32(220),
    end = cms.untracked.double(220),
    src = cms.untracked.InputTag("centralityBin","HFtowers"),
    start = cms.untracked.double(0)
)


process.vectEta = cms.EDAnalyzer("QWVectorAnalyzer",
    cNbins = cms.untracked.int32(1000),
    cend = cms.untracked.double(2.5),
    cstart = cms.untracked.double(-2.5),
    hNbins = cms.untracked.int32(5000),
    hend = cms.untracked.double(5000),
    hstart = cms.untracked.double(0),
    src = cms.untracked.InputTag("QWEvent","eta")
)


process.vectEtaW = cms.EDAnalyzer("QWVectorAnalyzer",
    cNbins = cms.untracked.int32(1000),
    cend = cms.untracked.double(2.5),
    cstart = cms.untracked.double(-2.5),
    hNbins = cms.untracked.int32(5000),
    hend = cms.untracked.double(5000),
    hstart = cms.untracked.double(0),
    src = cms.untracked.InputTag("QWEvent","eta"),
    srcW = cms.untracked.InputTag("QWEvent","weight")
)


process.vectPhi = cms.EDAnalyzer("QWVectorAnalyzer",
    cNbins = cms.untracked.int32(1000),
    cend = cms.untracked.double(3.14159265359),
    cstart = cms.untracked.double(-3.14159265359),
    hNbins = cms.untracked.int32(5000),
    hend = cms.untracked.double(5000),
    hstart = cms.untracked.double(0),
    src = cms.untracked.InputTag("QWEvent","phi")
)


process.vectPhiW = cms.EDAnalyzer("QWVectorAnalyzer",
    cNbins = cms.untracked.int32(1000),
    cend = cms.untracked.double(3.14159265359),
    cstart = cms.untracked.double(-3.14159265359),
    hNbins = cms.untracked.int32(5000),
    hend = cms.untracked.double(5000),
    hstart = cms.untracked.double(0),
    src = cms.untracked.InputTag("QWEvent","phi"),
    srcW = cms.untracked.InputTag("QWEvent","weight")
)


process.vectPt = cms.EDAnalyzer("QWVectorAnalyzer",
    cNbins = cms.untracked.int32(1000),
    cend = cms.untracked.double(5),
    cstart = cms.untracked.double(0),
    hNbins = cms.untracked.int32(5000),
    hend = cms.untracked.double(5000),
    hstart = cms.untracked.double(0),
    src = cms.untracked.InputTag("QWEvent","pt")
)


process.vectPtW = cms.EDAnalyzer("QWVectorAnalyzer",
    cNbins = cms.untracked.int32(1000),
    cend = cms.untracked.double(5),
    cstart = cms.untracked.double(0),
    hNbins = cms.untracked.int32(5000),
    hend = cms.untracked.double(5000),
    hstart = cms.untracked.double(0),
    src = cms.untracked.InputTag("QWEvent","pt"),
    srcW = cms.untracked.InputTag("QWEvent","weight")
)


process.hfCoincFilter5 = cms.Sequence(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfPosFilter5+process.hfNegFilter5)


process.hfCoincFilter = cms.Sequence(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfPosFilter+process.hfNegFilter)


process.endOfProcess_withComparison = cms.Sequence(process.MEtoEDMConverter+process.MEtoMEComparitor)


process.endOfProcess = cms.Sequence(process.MEtoEDMConverter)


process.hfposTowers = cms.Sequence(process.towersAboveThreshold+process.hfPosTowers)


process.vectMonW = cms.Sequence(process.histNoff+process.vectPhi+process.vectPt+process.vectEta+process.vectPhiW+process.vectPtW+process.vectEtaW)


process.makeEvent = cms.Sequence(process.centralityBin+process.QWEvent)


process.vectMon = cms.Sequence(process.histNoff+process.vectPhi+process.vectPt+process.vectEta)


process.hfnegTowers = cms.Sequence(process.towersAboveThreshold+process.hfNegTowers)


process.hfCoincFilter4 = cms.Sequence(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfPosFilter4+process.hfNegFilter4)


process.hfnegFilter = cms.Sequence(process.hfnegTowers+process.hfNegFilter)


process.hfposFilter4 = cms.Sequence(process.hfposTowers+process.hfPosFilter4)


process.hfposFilter5 = cms.Sequence(process.hfposTowers+process.hfPosFilter5)


process.hfposFilter2 = cms.Sequence(process.hfposTowers+process.hfPosFilter2)


process.hfnegFilter5 = cms.Sequence(process.hfnegTowers+process.hfNegFilter5)


process.hfCoincFilter2 = cms.Sequence(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfPosFilter2+process.hfNegFilter2)


process.hfCoincFilter3 = cms.Sequence(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfPosFilter3+process.hfNegFilter3)


process.hfnegFilter2 = cms.Sequence(process.hfnegTowers+process.hfNegFilter2)


process.hfnegFilter3 = cms.Sequence(process.hfnegTowers+process.hfNegFilter3)


process.collisionEventSelection = cms.Sequence(process.hfCoincFilter3+process.primaryVertexFilter+process.siPixelRecHits+process.hltPixelClusterShapeFilter)


process.hfnegFilter4 = cms.Sequence(process.hfnegTowers+process.hfNegFilter4)


process.hfposFilter3 = cms.Sequence(process.hfposTowers+process.hfPosFilter3)


process.collisionEventSelectionAOD = cms.Sequence(process.hfCoincFilter3+process.primaryVertexFilter+process.clusterCompatibilityFilter)


process.eventSelection = cms.Sequence(process.hfCoincFilter3+process.primaryVertexFilter+process.clusterCompatibilityFilter)


process.hfposFilter = cms.Sequence(process.hfposTowers+process.hfPosFilter)


process.pre_ana = cms.Sequence(process.hltMB+process.eventSelection+process.makeEvent)


process.ana = cms.Path(process.pre_ana+process.QWSC2+process.QWSC3+process.QWSC4+process.QWSC22+process.QWSC2_2+process.QWSC33+process.QWSC3_3+process.QWSC44+process.QWSC4_4+process.QWSC222+process.QWSC22_2+process.QWSC333+process.QWSC33_3+process.QWSC444+process.QWSC44_4+process.QWSC2222+process.QWSC222_2+process.QWSC22_2_2+process.QWSC3333+process.QWSC333_3+process.QWSC33_3_3+process.QWSC4444+process.QWSC444_4+process.QWSC44_4_4+process.QWSC22222+process.QWSC2222_2+process.QWSC222_2_2+process.QWSC33333+process.QWSC3333_3+process.QWSC333_3_3+process.QWSC44444+process.QWSC4444_4+process.QWSC444_4_4+process.QWSC222222+process.QWSC22222_2+process.QWSC2222_2_2+process.QWSC222_2_2_2+process.QWSC333333+process.QWSC33333_3+process.QWSC3333_3_3+process.QWSC333_3_3_3+process.QWSC444444+process.QWSC44444_4+process.QWSC4444_4_4+process.QWSC444_4_4_4+process.QWSC2222222+process.QWSC222222_2+process.QWSC22222_2_2+process.QWSC2222_2_2_2+process.QWSC3333333+process.QWSC333333_3+process.QWSC33333_3_3+process.QWSC3333_3_3_3+process.QWSC4444444+process.QWSC444444_4+process.QWSC44444_4_4+process.QWSC4444_4_4_4+process.QWSC22222222+process.QWSC2222222_2+process.QWSC222222_2_2+process.QWSC22222_2_2_2+process.QWSC2222_2_2_2_2+process.QWSC33333333+process.QWSC3333333_3+process.QWSC333333_3_3+process.QWSC33333_3_3_3+process.QWSC3333_3_3_3_3+process.QWSC44444444+process.QWSC4444444_4+process.QWSC444444_4_4+process.QWSC44444_4_4_4+process.QWSC4444_4_4_4_4)


process.DQMStore = cms.Service("DQMStore")


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring('FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(100)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring('warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    AftBurner = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(7410904)
    ),
    LHCTransport = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    MuonSimHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(987346)
    ),
    VtxSmeared = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(98765432)
    ),
    ecalPreshowerRecHit = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(6541321)
    ),
    ecalRecHit = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(654321)
    ),
    externalLHEProducer = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(234567)
    ),
    famosPileUp = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    famosSimHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(13579)
    ),
    g4SimHits = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(11)
    ),
    generator = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hbhereco = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hfreco = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hiSignal = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hiSignalG4SimHits = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(11)
    ),
    hiSignalLHCTransport = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(88776655)
    ),
    horeco = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    l1ParamMuons = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(6453209)
    ),
    mix = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixData = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixGenPU = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixRecoTracks = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixSimCaloHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    paramMuons = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(54525)
    ),
    saveFileName = cms.untracked.string(''),
    siTrackerGaussianSmearingRecHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(24680)
    ),
    simBeamSpotFilter = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    simMuonCSCDigis = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(11223344)
    ),
    simMuonDTDigis = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simMuonRPCDigis = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simSiStripDigiSimLink = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(1234567)
    )
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('sc.root')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring('HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER')
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.CastorDbProducer = cms.ESProducer("CastorDbProducer")


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.MuonNumberingInitialization = cms.ESProducer("MuonNumberingInitialization")


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(18268),
    version = cms.string('Parabolic')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    compatibiltyWith11 = cms.untracked.bool(True),
    useDDD = cms.untracked.bool(False)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(18268)
)


process.XMLFromDBSource = cms.ESProducer("XMLIdealGeometryESProducer",
    label = cms.string('Extended'),
    rootDDName = cms.string('cms:OCMS')
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    appendToDataLabel = cms.string(''),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.l1GtTriggerMaskTechTrig = cms.ESProducer("L1GtTriggerMaskTechTrigTrivialProducer",
    TriggerMask = cms.vuint32(0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0)
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiPixelQualityFromDbRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        ))
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(cms.PSet(
        Label = cms.untracked.string(''),
        NormalizationFactor = cms.untracked.double(1.0),
        Record = cms.string('SiStripApvGainRcd')
    ), 
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiStripDetVOffRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionRetrialPeriod = cms.untracked.int32(10),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(60),
        enableConnectionSharing = cms.untracked.bool(True),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0)
    ),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('75X_dataRun2_v13'),
    toGet = cms.VPSet()
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.L1GtTriggerMaskTechTrigRcdSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1GtTriggerMaskTechTrigRcd')
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HERecalibration = cms.bool(False),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalibration = cms.bool(False),
    HcalReLabel = cms.PSet(
        RelabelHits = cms.untracked.bool(False),
        RelabelRules = cms.untracked.PSet(
            CorrectPhi = cms.untracked.bool(False),
            Eta1 = cms.untracked.vint32(1, 2, 2, 2, 3, 
                3, 3, 3, 3, 3, 
                3, 3, 3, 3, 3, 
                3, 3, 3, 3),
            Eta16 = cms.untracked.vint32(1, 1, 2, 2, 2, 
                2, 2, 2, 2, 3, 
                3, 3, 3, 3, 3, 
                3, 3, 3, 3),
            Eta17 = cms.untracked.vint32(1, 1, 2, 2, 3, 
                3, 3, 4, 4, 4, 
                4, 4, 5, 5, 5, 
                5, 5, 5, 5)
        )
    ),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    ),
    iLumi = cms.double(-1.0),
    toGet = cms.untracked.vstring('GainWidths')
)


process.prefer("es_hardcode")

process.CondDBSetup = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionRetrialPeriod = cms.untracked.int32(10),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(60),
        enableConnectionSharing = cms.untracked.bool(True),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0)
    )
)

process.HcalReLabel = cms.PSet(
    RelabelHits = cms.untracked.bool(False),
    RelabelRules = cms.untracked.PSet(
        CorrectPhi = cms.untracked.bool(False),
        Eta1 = cms.untracked.vint32(1, 2, 2, 2, 3, 
            3, 3, 3, 3, 3, 
            3, 3, 3, 3, 3, 
            3, 3, 3, 3),
        Eta16 = cms.untracked.vint32(1, 1, 2, 2, 2, 
            2, 2, 2, 2, 3, 
            3, 3, 3, 3, 3, 
            3, 3, 3, 3),
        Eta17 = cms.untracked.vint32(1, 1, 2, 2, 3, 
            3, 3, 4, 4, 4, 
            4, 4, 5, 5, 5, 
            5, 5, 5, 5)
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)

process.schedule = cms.Schedule(*[ process.ana ])
