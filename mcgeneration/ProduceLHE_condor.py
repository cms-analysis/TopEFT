import os
import sys
from argparse import ArgumentParser
from array import array
import random
import math

"""
example:
python ProduceLHE_condor.py --tag=Initial_Test_rwgt --gridpack=./Initial_Test_rwgt_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz \
--outdir=/eos/user/s/smoortga/LHE_output_1M/ --jobflavour=longlunch --neventstotal=1000000 --neventsperjob=5000
"""

parser = ArgumentParser()
parser.add_argument('--tag', default="LHE_production_condor",help='A specific tag name to create log files etc.')
parser.add_argument('--gridpack', default=os.getcwd()+"/test_tarball.tar.xz",help='input tarball from the gridpack production')
parser.add_argument('--neventstotal', type=int, default=1000,help='total number of simulated LHE events')
parser.add_argument('--neventsperjob', type=int, default=100,help='number of events per condor job')
parser.add_argument('--outdir', default=os.getcwd(),help='output directory with enough space for the LHE files and with write priviledges (example: EOS)')
parser.add_argument('--jobflavour', default="microcentury",help='jobFlavour as described in https://batchdocs.web.cern.ch/local/submit.html')
args = parser.parse_args()

# check if jobflavour is valid
"""
https://batchdocs.web.cern.ch/local/submit.html
espresso     = 20 minutes
microcentury = 1 hour
longlunch    = 2 hours
workday      = 8 hours
tomorrow     = 1 day
testmatch    = 3 days
nextweek     = 1 week
"""
if not(args.jobflavour in ["espresso","microcentury","longlunch","workday","tomorrow","testmatch","nextweek"]):
	print("ERROR: unknown jobflavour! should be one of the following: 'espresso','microcentury','longlunch','workday','tomorrow','testmatch','nextweek'")
	print("Exiting...")
	sys.exit(1)
	

# Create directory to store the log files
if not os.path.isdir(os.getcwd()+"/condor_log_"+(args.tag).replace(" ","_")): os.mkdir(os.getcwd()+"/condor_log_"+(args.tag).replace(" ","_"))

# check existence of the output directory
if not os.path.isdir(os.path.abspath(args.outdir)):
	need_answer = True
	while need_answer:
		answer = raw_input("The output directory (%s) is not found, should I try to create it now (y/n)?"%os.path.abspath(args.outdir))
		if answer == "n": 
			print("Exiting...")
			sys.exit(1)
		elif answer == "y": 
			os.mkdir(os.path.abspath(args.outdir))
			if not os.path.isdir(os.path.abspath(args.outdir)):
				print("creating directory failed (do you have proper acces rights?)")
				print("Exiting...")
				sys.exit(1)
			need_answer = False
		else:
			print("please type either 'y' or 'n'")


# create a text file with the production paramters
njobs = int(math.ceil(float(args.neventstotal)/float(args.neventsperjob)))
print("preparing %i jobs"%njobs)
initial_seed = int(random.uniform(1,1000))
remaining_events = args.neventstotal
f_tmp_ = open(os.getcwd()+"/params_condor.txt", 'w')
for i in  range(njobs):
	seed = initial_seed + 2*i*args.neventsperjob + int(random.uniform(1,args.neventsperjob))
	nevents = args.neventsperjob
	if remaining_events < args.neventsperjob:nevents = remaining_events
	f_tmp_.write("%i, %i, %i \n"%(i+1, seed, nevents))
	remaining_events -= args.neventsperjob	
f_tmp_.close()


# create a submission batch script that untars the tarball
f_tmp_btach_ = open(os.getcwd()+"/LHEproduction_%s.sh"%((args.tag).replace(" ","_")), 'w')
f_tmp_btach_.write("#!/bin/bash \n")
f_tmp_btach_.write("tar -xaf $1 \n")
f_tmp_btach_.write("source runcmsgrid.sh $2 $3 1 \n")
f_tmp_btach_.close()

# create condor submission file
f_tmp_condor_ = open(os.getcwd()+"/ProduceLHE_condor_%s.submit"%((args.tag).replace(" ","_")), 'w')
f_tmp_condor_.write("Universe = vanilla \n")
f_tmp_condor_.write("Executable = LHEproduction_%s.sh \n"%((args.tag).replace(" ","_")))
f_tmp_condor_.write("Arguments = %s $(nevents) $(rnd) \n"%((args.gridpack).split("/")[-1]))
f_tmp_condor_.write(" \n")
f_tmp_condor_.write("Error = condor_log_%s/job.err \n"%((args.tag).replace(" ","_")))
f_tmp_condor_.write("Output = condor_log_%s/job.out \n"%((args.tag).replace(" ","_")))
f_tmp_condor_.write("Log = condor_log_%s/job.log \n"%((args.tag).replace(" ","_")))
f_tmp_condor_.write(" \n")
f_tmp_condor_.write("should_transfer_files = YES \n")
f_tmp_condor_.write("transfer_input_files = %s \n"%((args.gridpack).split("/")[-1]))
f_tmp_condor_.write("when_to_transfer_output = ON_EXIT \n")
f_tmp_condor_.write('transfer_output_remaps = "cmsgrid_final.lhe = %s/cmsgrid_final_$(number).lhe" \n'%args.outdir)
f_tmp_condor_.write('+JobFlavour = "%s" \n' %args.jobflavour)
f_tmp_condor_.write("queue number,rnd,nevents from params_condor.txt \n")
f_tmp_condor_.close()

print("The jobs can now be submitted via condor with 'condor_submit ProduceLHE_condor_%s.submit'"%((args.tag).replace(" ","_")))
print("The status can then be checked using 'condor_q'")