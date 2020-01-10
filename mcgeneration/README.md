## summary
This directory contains EFT specific modifications and addons for cms-sw/genproductions which allow to prepare EFT gridpacks and LHE files. 

### Step 1: Get your UFO model
First you need to download your preferred UFO model from the [feynrules model database](https://feynrules.irmp.ucl.ac.be/wiki/ModelDatabaseMainPage) and put it in [addons/models/](addons/models). 
The [dim6top_LO_UFO](https://feynrules.irmp.ucl.ac.be/wiki/dim6top) has been included by default (date of writing: 10 Jan 2020).

### instructions:  
 * execute setup_production.sh to checkout cms-sw/genproductions and merge dedicated EFT tools: 
 * run submit_madpack_ttbareft.sh to produce gridpacks 
   the script will copy card templates from  addons/cards/UFOMODEL_template and the corresponding UFO file in addons/models
   you can modify the copied cards according to your needs via sed in submit_madpack_ttbareft.sh
   afterwards jobs are submitted to lxplus condor 


