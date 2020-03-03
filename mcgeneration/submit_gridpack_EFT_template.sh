#!/bin/bash 


if [ -n "$1" ]
  then
    scram_arch=${1}
  else
    scram_arch=slc7_amd64_gcc700
fi
echo "Using SCRAM architecture ${scram_arch}"

if [ -n "$2" ]
  then
    cmssw_version=${2}
  else
    cmssw_version=CMSSW_10_2_18
fi
echo "Running in ${cmssw_version}"
                                                                                                                                                                                                      
SETUPTAG=( REPLACETAG ) 
NSETUPTAG=`echo "scale=0; ${#SETUPTAG[@]} -1 " | bc`
for ISETUPTAG in `seq 0 ${NSETUPTAG}`; do
    SETUP=${SETUPTAG[${ISETUPTAG}]}
    #rm -rf addons/cards/${SETUP} 
	# prepare card files 
    #mkdir -p addons/cards/${SETUP}
    for CARD in run_card proc_card customizecards reweight_card; do 
		mv addons/cards/${SETUP}/${CARD}.dat  addons/cards/${SETUP}/${SETUP}_${CARD}.dat
    done 
    sed -i -e "s|SUBSETUP|${SETUP}|g" addons/cards/${SETUP}/${SETUP}_*.dat 
    
    # run locally for testing 
    #./gridpack_generation.sh ${SETUP} addons/cards/${SETUP}
	
	echo "Submitting gridjob to screen"
	echo "run 'screen -ls' to see active screen sessions"
	echo "run 'screen -r (screenID)' to attach to screen"
	echo "then run 'ctrl+a+d' to detach from screen again"
	echo "the job is finished when the screen session is not visible anymore when doing 'screen ls'"
	screen -d -m bash -c "./gridpack_generation.sh ${SETUP} addons/cards/${SETUP} local ALL ${scram_arch} ${cmssw_version}"

done
