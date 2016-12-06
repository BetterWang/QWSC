from CRABAPI.RawCommand import crabCommand
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

config = config()

config.General.requestName = 'PAHM0_SC_eff_v5'
config.General.workArea = 'CrabArea'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'qw_pPb8_HM_v2.py'
config.Data.inputDataset = '/PAHighMultiplicity0/PARun2016C-PromptReco-v1/AOD'
config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v2.root']
#config.Data.inputDBS = 'phys03'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 50
config.Data.outLFNDirBase = '/store/user/qwang/SC/'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/HI/Cert_285479-285832_HI8TeV_PromptReco_pPb_Collisions16_JSON_NoL1T.txt'
config.Data.publication = False
config.Data.useParent = False
config.Site.storageSite = 'T2_CH_CERN'
config.Site.ignoreGlobalBlacklist = True
config.Data.allowNonValidInputDataset = True
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)

### sysTight
config.General.requestName = 'PAHM0_SC_eff_sysTight_v5'
config.JobType.psetName = 'qw_pPb8_HM_sysTight_v2.py'
config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v3_tight.root']
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)

### sysLoose
config.General.requestName = 'PAHM0_SC_eff_sysLoose_v5'
config.JobType.psetName = 'qw_pPb8_HM_sysLoose_v2.py'
config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v3_loose.root']
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)

### syVzNarrow
config.General.requestName = 'PAHM0_SC_eff_sysVzNarrow_resub_v5'
config.JobType.psetName = 'qw_pPb8_HM_sysVzNarrow_v2.py'
config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v4_narrow.root']
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

### syVzWide
config.General.requestName = 'PAHM0_SC_eff_sysVzWide_resub_v5'
config.JobType.psetName = 'qw_pPb8_HM_sysVzWide_v2.py'
config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v4_wide.root']
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)








### 1
config.Data.inputDataset = '/PAHighMultiplicity1/PARun2016C-PromptReco-v1/AOD'

config.General.requestName = 'PAHM1_SC_eff_v5'
config.JobType.psetName = 'qw_pPb8_HM1_v2.py'
config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v2.root']
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)


### sysTight
config.General.requestName = 'PAHM1_SC_eff_sysTight_v5'
config.JobType.psetName = 'qw_pPb8_HM1_sysTight_v2.py'
config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v3_tight.root']
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)

### sysLoose
config.General.requestName = 'PAHM1_SC_eff_sysLoose_v5'
config.JobType.psetName = 'qw_pPb8_HM1_sysLoose_v2.py'
config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v3_loose.root']
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)

### syVzNarrow
config.General.requestName = 'PAHM1_SC_eff_sysVzNarrow_resub_v5'
config.JobType.psetName = 'qw_pPb8_HM1_sysVzNarrow_v2.py'
config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v4_narrow.root']
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

### syVzWide
config.General.requestName = 'PAHM1_SC_eff_sysVzWide_resub_v5'
config.JobType.psetName = 'qw_pPb8_HM1_sysVzWide_v2.py'
config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v4_wide.root']
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)



### 7
config.Data.inputDataset = '/PAHighMultiplicity7/PARun2016C-PromptReco-v1/AOD'


config.General.requestName = 'PAHM7_SC_eff_v5'
config.JobType.psetName = 'qw_pPb8_HM7_v2.py'
config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v2.root']
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)


### sysTight
config.General.requestName = 'PAHM7_SC_eff_sysTight_v5'
config.JobType.psetName = 'qw_pPb8_HM7_sysTight_v2.py'
config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v3_tight.root']
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)

### sysLoose
config.General.requestName = 'PAHM7_SC_eff_sysLoose_v5'
config.JobType.psetName = 'qw_pPb8_HM7_sysLoose_v2.py'
config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v3_loose.root']
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)

### syVzNarrow
config.General.requestName = 'PAHM7_SC_eff_sysVzNarrow_resub_v5'
config.JobType.psetName = 'qw_pPb8_HM7_sysVzNarrow_v2.py'
config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v4_narrow.root']
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

### syVzWide
config.General.requestName = 'PAHM7_SC_eff_sysVzWide_resub_v5'
config.JobType.psetName = 'qw_pPb8_HM7_sysVzWide_v2.py'
config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v4_wide.root']
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


