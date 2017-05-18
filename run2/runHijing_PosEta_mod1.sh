#/bin/bash

echo $PWD
WORKDIR=$PWD
ls -l
source /afs/cern.ch/project/eos/installation/cms/etc/setup.sh
cd /afs/cern.ch/user/q/qwang/work/cleanroomRun2/Ana/CMSSW_7_5_8_patch3/src/QWAna/QWSC/run2
eval `scramv1 runtime -sh`
cp qw_HIJING_sysPosEta_mod1_v1.py $WORKDIR/cfg.py
cd $WORKDIR
cmsRun cfg.py
ls -l
NEW_UUID=$(openssl rand -base64 32 | tr -dc 'a-zA-Z0-9' | head -c 8)
cmsStage sc.root /store/group/phys_heavyions/qwang/PbPb2015_cumu/MC/HIJING_SC_sysPosEta_mod1/hijing_$NEW_UUID.root
echo done transfter
