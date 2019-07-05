#!/bin/bash                                                                                                                                                                                                       
SETUPTAG=( gluontop_rwgt ) 
MODEL=dim6top_LO_UFO
NSETUPTAG=`echo "scale=0; ${#SETUPTAG[@]} -1 " | bc`
for ISETUPTAG in `seq 0 ${NSETUPTAG}`; do
    SETUP=${SETUPTAG[${ISETUPTAG}]}
    rm -rf addons/cards/${SETUP} 
	# prepare card files 
    mkdir -p addons/cards/${SETUP}
    for CARD in run_card proc_card customizecards reweight_card; do 
	cp -rp addons/cards/${MODEL}_template/${CARD}.dat  addons/cards/${SETUP}/${SETUP}_${CARD}.dat
    done 
    sed -i -e "s|SUBSETUP|${SETUP}|g" addons/cards/${SETUP}/${SETUP}_*.dat 
    # submit jobs to condor lxplus 
    ./submit_condor_gridpack_generation.sh ${SETUP} addons/cards/${SETUP}
done


