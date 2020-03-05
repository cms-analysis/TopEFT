#!/bin/bash


### define pathes - please keep structure and names to properly apply patches 
EFTMCPATH=`pwd -P`
GENPRODPATH=${EFTMCPATH}/../../genproductions                                                                                                                                                                      


### check out official genproduction repo, currently branch 2.6 
if [ -d "$GENPRODPATH" ]; then
    echo "Directory ${GENPRODPATH} shouldn't exist at this point"
    echo " We are going to set it up"
    echo " Please remove it and start over again"
    exit 0
else 
    mkdir -p ${GENPRODPATH}
    cd ${GENPRODPATH}/..
    git clone -b mg265 https://github.com/cms-sw/genproductions.git genproductions 
    cd ${GENPRODPATH}

    # copy eft relevant code  
    for COPY in addons submit_gridpack_EFT.sh ProduceLHE_condor.py MergeLHE.sh ; do 
	cp -r ${EFTMCPATH}/${COPY} ${GENPRODPATH}/bin/MadGraph5_aMCatNLO/.
    done

    # add mg5_amc@nlo patches which are not yet in geproductions
    # suppress error messages as there might be no special mg5 patches and error messages are confusing  
    cp -r ${EFTMCPATH}/mg5patches/* ${GENPRODPATH}/bin/MadGraph5_aMCatNLO/patches/. 2>/dev/null 

    # adjust central scripts 
    cd ${GENPRODPATH}/bin/MadGraph5_aMCatNLO
    cat ${EFTMCPATH}/patches/*.patch | patch -p1

    echo "You are done with setting up genproduction for EFT gridpack generation!"
fi                           

