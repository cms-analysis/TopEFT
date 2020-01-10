# Summary
This directory contains EFT specific modifications and addons for cms-sw/genproductions which allow to prepare EFT gridpacks and LHE files based on MadGraph5_aMC@NLO. 

### Step 1: Get your UFO model
First you need to download your preferred UFO model from the [feynrules model database](https://feynrules.irmp.ucl.ac.be/wiki/ModelDatabaseMainPage) and put it in [addons/models/](addons/models). 
The [dim6top_LO_UFO](https://feynrules.irmp.ucl.ac.be/wiki/dim6top) has been included by default (date of writing: 10 Jan 2020).

### Step 1: Configuration for your process
Open [process_cfg.py](./process_cfg.py) and fill out all the necessary fields outlined below to configure the process you want to generate and the EFT operators you want to probe:

  * tag: can be any name used to identify the process. It will be used as a directory name to save that cards in [addons/cards/](addons/cards). It is important to remember this tag further along.
  * model_name: exact name of the UFO file you downloaded in [addons/models/](addons/models).
  * processes: an array of strings, each representing a process you want to generate with Madgraph. These processes will be added together in the proc_card.dat.
  * flavour_scheme: specify here whether you want to use the 4F (massive b, not in the proton pdf) or 5F scheme (massless b, included in the proton pdf).
  * operators: an array of operators you want to probe. The names should match exactly those in the `parameters.py` file in your UFO directory.
  * baseline_values: an array of initial values for the Wilson coefficients of each operator. This defines the baseline scenario to which the reweighting factors will be calculated. The choice of these values is of crucial importance to ensure a proper coverage of the entire phase space. Putting all values to 0 (~SM) will most likely result in a bad coverage in the part of the Phase space where the EFT is expected to be most abundant, resulting in large weights and uncertain predictions of the yields and differential distributions. Properly assigning these values requires careful studies (please contact [Top-EFT working group conveners](mailto:cms-toppag-eft@cern.ch) in case of doubt).
  * reweighting_strategy: please choose one of the following options
    > **_no_reweights_**: no reweighting is applied<br/>
    > **_individual_**: each operator is varied individually<br/>
    > **_rnd_scan_**: a random scan over all operators is performed<br/>
    > **_grid_**: a rectangular grid of Wilson coefficients is scanned<br/>
    > **_custom_**: a custom reweighting scheme is provided by the user
    
	Then navigate to the corresponding "if statement" and fill out the needed parameters:
	> **_individual_**: "`points_individual`" is an array of arrays where in each subarray the user has to manually specify the values of the WCs to be scanned for the corresponding operator (using the same ordering as the "`operators`" variable).<br/>
    > **_rnd_scan_**: specify in "`n_points`" the number of scan points (NOTE: for N operators you need at least `1 + 2*N + (N*(N-1))/2` scan points to determine the quadratic function of the cross section). Then specify the boundaries for each operator in "`boundaries`".
    > **_grid_**: Specify in each subarray of "`boundaries_and_npoints`" the lower and upper boundary as well as the number of points to be scanned for each operator. For k points and N operators, a grid of k^N points will be constructed.
    > **_custom_**: The user has to manually specify the dictionary "`reweight_dict_tmp_`" where each key,value pair represents one specific scenario of a given set of WCs.
    
    Finally, the SM scenario (all WCs put to 0), will be included by default.
    The naming convention (when not defining "custom" as a reweighting strategy) is defined by the `translate_weight_name` helper function. It starts with "rwgt_", followed by listing all operators with their values. Decimal points are replaced by "p" and minus signs by "min".

### instructions:  
 * execute setup_production.sh to checkout cms-sw/genproductions and merge dedicated EFT tools: 
 * run submit_madpack_ttbareft.sh to produce gridpacks 
   the script will copy card templates from  addons/cards/UFOMODEL_template and the corresponding UFO file in addons/models
   you can modify the copied cards according to your needs via sed in submit_madpack_ttbareft.sh
   afterwards jobs are submitted to lxplus condor 


