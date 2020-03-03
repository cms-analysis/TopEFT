# Summary
This directory contains EFT specific modifications and addons for cms-sw/genproductions which allow to prepare EFT gridpacks and LHE files based on MadGraph5_aMC@NLO. **_The following setup has been tested to work on lxplus7 only!_** (login to lxplus using <username>@lxplus7.cern.ch)

### Step 0: create environment and pull this repository
```
mkdir your_favorite_name
cd your_favorite_name
git clone git@github.com:cms-analysis/TopEFT.git
cd TopEFT/mcgeneration/
```

### Step 1: Get your UFO model
First you need to download your preferred UFO model from the [feynrules model database](https://feynrules.irmp.ucl.ac.be/wiki/ModelDatabaseMainPage) and put it in [addons/models/](addons/models). 
The [dim6top_LO_UFO](https://feynrules.irmp.ucl.ac.be/wiki/dim6top) has been included by default (date of writing: 10 Jan 2020).

### Step 2: Configuration for your process
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
    > **_minimal_**: a tetrahedron-construction of scan points that picks the minimal number of scan points needed for a fit of a given order<br/>
    > **_custom_**: a custom reweighting scheme is provided by the user
    
	Then navigate to the corresponding "if statement" and fill out the needed parameters:
	> **_individual_**: "`points_individual`" is an array of arrays where in each subarray the user has to manually specify the values of the WCs to be scanned for the corresponding operator (using the same ordering as the "`operators`" variable).<br/>
    > **_rnd_scan_**: specify in "`n_points`" the number of scan points (NOTE: for N operators you need at least `1 + 2*N + (N*(N-1))/2` scan points to determine the quadratic function of the cross section). Then specify the boundaries for each operator in "`boundaries`".<br/>
    > **_grid_**: specify in each subarray of "`boundaries_and_npoints`" the lower and upper boundary as well as the number of points to be scanned for each operator. For k points and N operators, a grid of k^N points will be constructed.<br/>
    > **_minimal_**: specify in each subarray of "`boundaries_minimal_scan`" the lower and upper boundary of each operator. Also the "`order`" of the fitted yield must be given (usually 2, but can be 1 for interference only or larger than 2 for multiple insertions of EFT operators).<br/>
    > **_custom_**: The user has to manually specify the dictionary "`reweight_dict_tmp_`" where each key,value pair represents one specific scenario of a given set of WCs.
    
    Finally, the SM scenario (all WCs put to 0), will be included by default.
    The naming convention (when not defining "custom" as a reweighting strategy) is defined by the `translate_weight_name` helper function. It starts with "rwgt_", followed by listing all operators with their values. Decimal points are replaced by "p" and minus signs by "min".


### Step 3: create all cards needed for MadGraph5_aMC@NLO.
The [prepare_process.py](prepare_process.py) script will read out the configuration from the [process_cfg.py](./process_cfg.py) file and construct the following cards in `addons/cards/<tag>`:
> run_card.dat<br/>
> proc_card.dat<br/>
> reweight_card.dat<br/>
> customizecards.dat<br/>
	
To this end, run:
```
python prepare_process.py
```

This will also create a copy of [submit_gridpack_EFT_template.sh](submit_gridpack_EFT_template.sh), which will be called "`submit_gridpack_EFT.sh`" and for which the chosen "`tag`" is correctly inserted in the script.

### Step 4: setup genproductions and copy needed EFT tools
For the production of CMS samples, we need the pull the [cms-sw/genproductions](https://github.com/cms-sw/genproductions.git) package from github. The current version of this code only works with the `mg265` branch (this was written on 10th January 2020). To this end, run:
```
source setup_production.sh
```
This will create a new directory called "genproductions" alongside your current TopEFT repository and it will copy all the scripts, models, cards that you need to run your EFT sample production. At the end you will be automatically directed to the proper directory (namely `genproductions/bin/MadGraph5_aMCatNLO/`).

### Step 5: Run gridpack
within the `genproductions/bin/MadGraph5_aMCatNLO/` folder, you can run this "`submit_gridpack_EFT.sh`" script by doing:
```
source submit_gridpack_EFT.sh slc7_amd64_gcc700 CMSSW_10_2_18
```
There are two optional arguments, namely the SCRAM architecture (argument 1) and the CMSSW version (argument 2) that are to be used for the gridpack generation. Make sure these are compatible with your machine (lxplus7 or lxplus6). If these are not given, by default the script takes `slc7_amd64_gcc700` and `CMSSW_10_2_18`, which can be run from lxplus7. 
The above command will launch the gridpack creation locally but in a seperate `screen` session, so you can continue doing other things. You can monitor your screen sessions doing `screen -ls`, and you can attach to the running screen session by doing `screen -r (screenID)`. Use `ctrl+a+d` to detach again form an attached screen session. After the gridpack generation is finished, the screen session will terminate automatically (which is when you will know the job has finished, and it does not show up anymore in `screen -ls`). You should now see a tarball in your directory, which holds your gridpack.

**_NOTE: gridpack generation can take several minutes up to several hours, depending on your process and the amount of weights that need to be saved._**

### Step 6: Launch production of LHE files (using condorHT)
within the `genproductions/bin/MadGraph5_aMCatNLO/` folder, you will see the [ProduceLHE_condor.py](ProduceLHE_condor.py) file. It will create the needed scripts and condor submission configurations to run a parallel production or a chosen number of Les Houches event files (LHE).
It contains 6 configurable parameters:
> **_--tag_**: A specific tag name to create log files etc.<br/>
> **_--gridpack_**: path to the tarball from the gridpack production<br/>
> **_--outdir_**: absolute path to the output directory where the `.lhe` files will be stored. This has to be a folder with write access and anough storage space. A good example is your personal /eos/ space, where you should have 1 TB of memory available (`/eos/user/<initial>/<username>/`). If the directory does not yet exist, the script will try to create it, or it will terminate is it fails to do so.<br/>
> **_--jobflavour_**: jobFlavour as described in [https://batchdocs.web.cern.ch/local/submit.html](https://batchdocs.web.cern.ch/local/submit.html). This defines the walltime for each job.<br/>
> **_--neventstotal_**: total number of events to simulate.<br/>
> **_--neventsperjob_**: number of events per condor job. The number of jobs will be `--neventstotal/--neventsperjob` (rounded up).

As an example, let's say you want to generate 1.5 million events, using 10000 events per job, with a gridpack named `test_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz`, and save the output into a directory called `/eos/user/f/frank/test_eft_production`, you should run:
```
python ProduceLHE_condor.py \
--tag=test \
--gridpack=./test_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz \
--outdir=/eos/user/f/frank/test_eft_production/ \
--jobflavour=longlunch \
--neventstotal=1500000 \
--neventsperjob=10000
```
This will now create several files, amongst which is `ProduceLHE_condor_<tag>.submit`. You can submit this to the condorHT scheduler by doing:
```
condor_submit ProduceLHE_condor_<tag>.submit
```
and check the status using
```
condor_q
```
Once all jobs have finished, the output is stored in the "`outdir`" in the form of a number of files named "`cmsgrid_final_1.lhe`" with increasing file numbers.

### Step 7: Merging several LHE files (optional)
It is often convenient for further processing to have one single LHE files with all your events in it. To this end, a script named [MergeLHE.sh](MergeLHE.sh) was added which has one command-line argument: the directory where the LHE files are stored. In the example from above, where the LHE files are stored in `/eos/user/f/frank/test_eft_production`, you can thus run from the `genproductions/bin/MadGraph5_aMCatNLO/` directory:
```
source MergeLHE.sh /eos/user/f/frank/test_eft_production/ 
```
This will launch in a screen session the merging of the LHE files, resulting once finished in one single LHE file called `merged_LHE.lhe`. You are now free to delete the number subfiles to save storage space. The screen session can be monitored as explained in Step 5.

**_NOTE: merging LHE files can take several minutes up to several hours, depending on the number of events. For more
than ~100k events, this becomes practically very difficult._**


