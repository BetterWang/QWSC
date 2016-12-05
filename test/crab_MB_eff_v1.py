from CRABAPI.RawCommand import crabCommand
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

config = config()

config.General.requestName = 'PAMB1_SC_eff_v2'
config.General.workArea = 'CrabArea'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'qw_pPb8_MB_v1.py'
config.Data.inputDataset = '/PAMinimumBias1/PARun2016C-PromptReco-v1/AOD'
config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v2.root']
#config.Data.inputDBS = 'phys03'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 100
config.Data.outLFNDirBase = '/store/group/phys_heavyions/qwang/SC/'
config.Data.lumiMask = '/afs/cern.ch/work/q/qwang/public/pPb_JSON.txt'
config.Data.publication = False
config.Data.useParent = False
config.Site.storageSite = 'T2_CH_CERN'
config.Site.ignoreGlobalBlacklist = True
config.Data.allowNonValidInputDataset = True
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


### 2
config.General.requestName = 'PAMB2_SC_eff_v2'
config.Data.inputDataset = '/PAMinimumBias2/PARun2016C-PromptReco-v1/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


### 3
config.General.requestName = 'PAMB3_SC_eff_v2'
config.Data.inputDataset = '/PAMinimumBias3/PARun2016C-PromptReco-v1/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

### 4
config.General.requestName = 'PAMB4_SC_eff_v2'
config.Data.inputDataset = '/PAMinimumBias4/PARun2016C-PromptReco-v1/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

### 5
config.General.requestName = 'PAMB5_SC_eff_v2'
config.Data.inputDataset = '/PAMinimumBias5/PARun2016C-PromptReco-v1/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

### 6
config.General.requestName = 'PAMB6_SC_eff_v2'
config.Data.inputDataset = '/PAMinimumBias6/PARun2016C-PromptReco-v1/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

### 7
config.General.requestName = 'PAMB7_SC_eff_v2'
config.Data.inputDataset = '/PAMinimumBias7/PARun2016C-PromptReco-v1/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

### 8
config.General.requestName = 'PAMB8_SC_eff_v2'
config.Data.inputDataset = '/PAMinimumBias8/PARun2016C-PromptReco-v1/AOD'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)
