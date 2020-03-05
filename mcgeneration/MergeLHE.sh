#!/bin/bash

MERGEDIR=($1)
CURRENTDIR=($PWD)
cd $MERGEDIR
cp /cvmfs/cms.cern.ch/phys_generator/gridpacks/lhe_merger/merge.pl $MERGEDIR
chmod 755 $MERGEDIR/merge.pl
echo "Submitting LHE Merge job to screen"
echo "run 'screen -ls' to see active screen sessions"
echo "run 'screen -r (screenID)' to attach to screen"
echo "then run 'ctrl+a+d' to detach from screen again"
echo "the job is finished when the screen session is not visible anymore when doing 'screen ls'"
echo "this can take a few minutes up to a few hours depending on the number of files and events to merge"
screen -d -m bash -c "./merge.pl *.lhe merged_LHE.lhe.gz banner.txt; gzip -d merged_LHE.lhe.gz"
cd $CURRENTDIR