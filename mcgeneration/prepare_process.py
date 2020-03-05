from process_cfg import *

"""
python prepare_process.py
"""

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#
# 		TAG
#
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

if not os.path.isdir("./addons/cards/%s"%tag): os.mkdir("./addons/cards/%s"%tag)
working_dir = "./addons/cards/%s"%tag

print("--> created directory %s"%working_dir)

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#
# 		proc_card.dat
#
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

assert os.path.isdir("./addons/models/%s"%model_name), \
		"ERROR: could not find model with name %s in ./addons/models/!"%model_name

if os.path.isfile(working_dir+"/proc_card.dat"):
	print("WARNING, %s/proc_card.dat already exists! OVERWRITING!!!!"%working_dir)
proc_card_ = open(working_dir+"/proc_card.dat","w")
proc_card_.write("import model %s \n"%model_name)
if flavour_scheme == "5F" or flavour_scheme == "5f":
	print("--> Using 5F scheme")
	proc_card_.write("define p = p b b~ \n")
	proc_card_.write("define j = p \n")
else:
	print("--> Using 4F scheme")
proc_card_.write("define l+ = e+ mu+ ta+ \n")
proc_card_.write("define l- = e- mu- ta- \n")
proc_card_.write("define vl = ve vm vt \n")
proc_card_.write("define vl~ = ve~ vm~ vt~ \n")
for line in processes:
	proc_card_.write("%s \n"%line)
proc_card_.write("output SUBSETUP \n")
proc_card_.close()

print("--> wrote to %s/proc_card.dat"%working_dir)


#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#
# 		customizecards.dat
#
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

if os.path.isfile(working_dir+"/customizecards.dat"):
	print("WARNING, %s/customizecards.dat already exists! OVERWRITING!!!!"%working_dir)
customizecards_ = open(working_dir+"/customizecards.dat","w")
customizecards_.write("set param_card mass 6 172.5 \n")
customizecards_.write("set param_card yukawa 6 172.5 \n")
customizecards_.write("set param_card decay 6 auto \n")
for idx,op in enumerate(operators):
	customizecards_.write("set param_card %s %s \n"%(op,baseline_values[idx]))
if flavour_scheme == "5F" or flavour_scheme == "5f":
	customizecards_.write("set run_card maxjetflavor 5 \n")
else:
	customizecards_.write("set run_card maxjetflavor 4 \n")
customizecards_.close()

print("--> wrote to %s/customizecards.dat"%working_dir)

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#
# 		run_card.dat
#
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

if os.path.isfile(working_dir+"/run_card.dat"):
	print("WARNING, %s/run_card.dat already exists! OVERWRITING!!!!"%working_dir)
os.system("cp %s %s"%("./addons/cards/dim6top_LO_UFO_template/run_card.dat",working_dir))

print("--> wrote to %s/run_card.dat"%working_dir)

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#
# 		reweight_card.dat
#
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*



reweight_dict = {}

if "no_reweights" in reweighting_strategy: 
	print("YOU SPECIFIED 'no_reweights' AS A STRATEGY AND THEREFORE NO REWEIGHTING WILL BE USED!")
	print("--> ALL OTHER STRATEGIES THAT YOU SPECIFIED ARE IGNORED!!!!")

else: 
	if "individual" in reweighting_strategy:
	
		for idx,op in enumerate(operators):
			for val in points_individual[idx]:
				reweight_dict[translate_weight_name([op],[val])] = {}
				reweight_dict[translate_weight_name([op],[val])][op] = val
				for other_op in [i for i in operators if not i == op]:
					reweight_dict[translate_weight_name([op],[val])][other_op] = 0.0
	
		# include the SM by default
		if not "rwgt_SM" in reweight_dict.keys():
			reweight_dict["rwgt_SM"] = {}
			for op in operators:
				reweight_dict["rwgt_SM"][op] = 0.0
	
		#pprint(reweight_dict)
	
	
	
	if "rnd_scan" in reweighting_strategy:
	
		for i in range(n_points):
			values_tmp_ = []
			for idx,op in enumerate(operators):
				values_tmp_.append(float("%.2f"%random.uniform(boundaries[idx][0],boundaries[idx][1])))
			dict_name = translate_weight_name(operators,values_tmp_)
			if dict_name in reweight_dict:
				print("warning!! two weights happen to be exactly the same!") # sanity check, very unlikely
			reweight_dict[dict_name] = {}
		
			for idx,op in enumerate(operators):
				reweight_dict[dict_name][op] = values_tmp_[idx]
	
		# include the SM by default
		if not "rwgt_SM" in reweight_dict.keys():
			reweight_dict["rwgt_SM"] = {}
			for op in operators:
				reweight_dict["rwgt_SM"][op] = 0.0
	
		#pprint(reweight_dict)
		
		
	
	if "grid" in reweighting_strategy:

		grid_values_per_operator = []
		for op in boundaries_and_npoints:
			grid_values_per_operator.append(np.linspace(op[0],op[1],num=op[2],endpoint=True))
	
		for t in itertools.product(*grid_values_per_operator):
			dict_name = translate_weight_name(operators,np.asarray(t))
			reweight_dict[dict_name] = {}
			for idx,op in enumerate(operators):
				reweight_dict[dict_name][op] = (np.asarray(t))[idx]
		
	
	
		# include the SM by default
		if not "rwgt_SM" in reweight_dict.keys():
			reweight_dict["rwgt_SM"] = {}
			for op in operators:
				reweight_dict["rwgt_SM"][op] = 0.0
	
		#pprint(reweight_dict)
		
	
	if "minimal" in reweighting_strategy:
		init_steps = [i for i in range(order+1)]
		valid_combinations = [i for i in itertools.product(init_steps,repeat=len(operators)) if sum(i)<=order]
		for comb in valid_combinations:
			comb_array = np.asarray(comb)
			rescaled_comb_array = [-999.99]*len(comb_array)
			for idx,val in enumerate(comb_array):
				min_range = boundaries_minimal_scan[idx][0]
				width_range = abs(float(boundaries_minimal_scan[idx][1])-float(boundaries_minimal_scan[idx][0]))
				rescaled_comb_array[idx] = float(val)*(float(width_range)/float(order)) + float(min_range)
			dict_name = translate_weight_name(operators,np.asarray(rescaled_comb_array))
			reweight_dict[dict_name] = {}
			for idx,op in enumerate(operators):
				reweight_dict[dict_name][op] = (np.asarray(rescaled_comb_array))[idx]
				
		if not "rwgt_SM" in reweight_dict.keys():	
			reweight_dict["rwgt_SM"] = {}
			for op in operators:
				reweight_dict["rwgt_SM"][op] = 0.0
		
		# sanity check, should always be fulfilled	
		assert len(reweight_dict.keys()) >= (1. + 2.*len(operators) + (len(operators)*(len(operators)-1.))/2.), \
			"ERROR: you need at least %i points for %i operators to fully determine the coefficients of the quadratic form"%((1. + 2.*len(operators) + (len(operators)*(len(operators)-1.))/2.),len(operators))

		
		#pprint(reweight_dict)

		

	if "custom" in reweighting_strategy:
		reweight_dict.update(reweight_dict_tmp_)
		# include the SM by default
		if not "rwgt_SM" in reweight_dict.keys():
			reweight_dict["rwgt_SM"] = {}
			for op in operators:
				reweight_dict["rwgt_SM"][op] = 0.0
	
		#pprint(reweight_dict)
	
	


	



if os.path.isfile(working_dir+"/reweight_card.dat"):
	print("WARNING, %s/reweight_card.dat already exists! OVERWRITING!!!!"%working_dir)
reweight_card_ = open(working_dir+"/reweight_card.dat","w")
reweight_card_.write("#****************************************************************** \n")
reweight_card_.write("#                       Reweight Module                           * \n")
reweight_card_.write("#****************************************************************** \n")
reweight_card_.write(" \n")
reweight_card_.write(" change rwgt_dir rwgt \n")
reweight_card_.write(" \n")
for w_name,w_dict in reweight_dict.iteritems():
	reweight_card_.write("launch --rwgt_name=%s \n"%w_name)
	for op,val in w_dict.iteritems():
		reweight_card_.write("set %s %f \n"%(op,val))
	reweight_card_.write(" \n")
reweight_card_.close()

print("--> wrote to %s/reweight_card.dat"%working_dir)




#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#
# 		APPLY THE TAG ALSO IN THE submit_madpack_ttbareft.sh
#
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

os.system("cp submit_gridpack_EFT_template.sh submit_gridpack_EFT.sh")
os.system("sed -i 's/REPLACETAG/%s/g' submit_gridpack_EFT.sh"%tag)
print("replaced tag name (%s) in submit_gridpack_EFT.sh"%tag)







	
	