#!/bin/bash                                                                                                                                                                                                       
SETUPTAG=( Initial_Test_rwgt ) 
ORIGINALTAG=Initial_Test
NSETUPTAG=`echo "scale=0; ${#SETUPTAG[@]} -1 " | bc`
for ISETUPTAG in `seq 0 ${NSETUPTAG}`; do
    SETUP=${SETUPTAG[${ISETUPTAG}]}
    rm -rf addons/cards/${SETUP} 
	# prepare card files 
    mkdir -p addons/cards/${SETUP}
    for CARD in run_card proc_card customizecards reweight_card; do 
	cp -rp addons/cards/${ORIGINALTAG}/${CARD}.dat  addons/cards/${SETUP}/${SETUP}_${CARD}.dat
    done 
    sed -i -e "s|SUBSETUP|${SETUP}|g" addons/cards/${SETUP}/${SETUP}_*.dat 
    # run locally for testing 
    #./gridpack_generation.sh ${SETUP} addons/cards/${SETUP}
	
	
	# the submission script
	echo "#!/bin/bash" >> condor_gridpack_${SETUP}_submit.sh
	#echo "source Utilities/source_condor.sh" >> condor_gridpack_${SETUP}_submit.sh
	echo "source /cvmfs/cms.cern.ch/cmsset_default.sh" >> condor_gridpack_${SETUP}_submit.sh
	echo "source ${PWD}/gridpack_generation.sh ${SETUP} ${PWD}/addons/cards/${SETUP}" >> condor_gridpack_${SETUP}_submit.sh
	
	# the condor config file
	echo "Universe   = vanilla" >> condor_gridpack_${SETUP}_config.sub
	echo "Executable = condor_gridpack_${SETUP}_submit.sh" >> condor_gridpack_${SETUP}_config.sub
	echo "Arguments  = ${SETUP} addons/cards/${SETUP}" >> condor_gridpack_${SETUP}_config.sub
	echo "Log        = condor_${SETUP}.log" >> condor_gridpack_${SETUP}_config.sub
	echo "Output     = condor_${SETUP}.out" >> condor_gridpack_${SETUP}_config.sub
	echo "Error      = condor_${SETUP}.error" >> condor_gridpack_${SETUP}_config.sub
	echo 'requirements = (OpSysAndVer =?= "SLCern6")' >> condor_gridpack_${SETUP}_config.sub
	#echo '+JobFlavour = "microcentury"' >> condor_gridpack_${SETUP}_config.sub
	
	echo "Queue" >> condor_gridpack_${SETUP}_config.sub
	


done


