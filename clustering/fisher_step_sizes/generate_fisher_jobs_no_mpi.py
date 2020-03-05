import numpy as np
import os
from os import listdir, mkdir
from os.path import isdir, join, isfile
import shutil

def find_varied(values_inifile):
	sections = []
	varied_params = {}
	# find varied parameters in values
	with open(values_inifile, 'r') as vini:
		for line_number, line in enumerate(vini):
			line = line.rstrip()
			if line.startswith('[') & line.endswith(']'): # if line is a [section] header
				section = line[1:-1]
				sections.append(section)
				continue
			if len(line.split('=')) > 1: # if line is a parameter value
				param, value = line.split('=')
				# remove whitespace
				param = param.replace(' ','')
				value = [i for i in value.split(' ') if i!='']

				if (not line.startswith(';')) & (len(value) == 3): # if param is varied in cosmosis
					varied_params[line_number] = ("%s--%s" % (section, param), value)
	return varied_params

def fix_parameters(values_inifile, varied_params):
	new_values = {}
	for ln, (vp, val) in varied_params.items(): # cycle over each varied parameter
		new_values[vp] = []
		# construct new values .inis
		with open(values_inifile, 'r') as vini:
			for line_number, line in enumerate(vini):
				if line_number in [i for i in varied_params.keys() if i!=ln]: # if line is one of the other varied parameters
					param, value = varied_params[line_number]
					param = param.split('--')[1]
					new_line = "%s = %s\n" % (param, value[1]) # fix parameter
					new_values[vp].append(new_line)
				else:
					new_values[vp].append(line)
	return new_values

pipeline_ini = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/fisher_step_sizes/clustering_mag_template.ini'
fisher_vals_ini = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/fisher_step_sizes/values_clustering_mag_fisher.ini'
testdir = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/fisher_step_sizes/fisher_jobs_mag/'

generate_single_executable = True

if not isdir(testdir):
	mkdir(testdir)

NCORES = 1 # ncores per fisher+grid job

# find varied parameters in values
fisher_varied_params = find_varied(fisher_vals_ini)

fisher_new_values = fix_parameters(fisher_vals_ini, fisher_varied_params)

new_pipelines = {}

for vp, val in fisher_varied_params.values(): # cycle over each varied parameter
	# construct new pipeline .inis
	new_pipelines[vp+'_fisher'] = []
	with open(pipeline_ini, 'r') as pipeline:
		for line in pipeline:
			if line.rstrip() == 'sampler =': # change sampler
				f_line = 'sampler = fisher\n'
				new_pipelines[vp+'_fisher'].append(f_line)

			elif line.rstrip() == 'vals_file =': # values
				f_line = 'vals_file = ' + testdir + 'values_%s_fisher.ini\n' % vp
				new_pipelines[vp+'_fisher'].append(f_line)

			elif line.rstrip() == 'out_file =': # and output
				f_line = 'out_file = ' + testdir + '%s_fisher_out.txt\n' % vp
				new_pipelines[vp+'_fisher'].append(f_line)

			else:
				new_pipelines[vp+'_fisher'].append(line)

if generate_single_executable == True:
	single_executable = join(testdir, 'execute_pipelines.sh')
	with open(single_executable, 'w') as single_file:
		bash_prefix = ('#!/bin/bash\n')
		single_file.write(bash_prefix)
	os.system('chmod +x %s'%single_executable)

# save values.inis
for i, key in enumerate(fisher_new_values.keys()):
	with open(join(testdir, "values_%s_fisher.ini"%key), 'w') as new_vini:
		for line in fisher_new_values[key]:
			new_vini.write(line)
"""
	# make executables
	exec_filename = join(testdir, 'exec_pipelines_%s.sh'%(i+1))
	with open(exec_filename, 'w') as exec_file:
		exec_string = (#'#!/bin/bash\n'
					   'echo "' + key + '"\n\n'

					   'cosmosis ' + testdir + 'pipeline_' + key + '_fisher.ini\n\n'

					 )
		exec_file.write(exec_string)
	os.system('chmod +x %s'%exec_filename)
"""

# save pipeline.inis
for key, new_pipeline in new_pipelines.items():
	with open(join(testdir, "pipeline_%s.ini"%key), 'w') as new_pipe:
		for line in new_pipeline:
			new_pipe.write(line)


########################################################################
# VARY FISHER STEP SIZES
########################################################################

number_of_fisher_steps_to_try = 10
min_step_size_in_log_space = -4
max_step_size_in_log_space = -1
executables_counter = 0

for key, new_pipeline in new_pipelines.items():
	pipeline_ini_file = testdir + "pipeline_" + key + ".ini"
	values_file = testdir + "values_" + key + ".ini"
	output_file = testdir + key + "_out.txt"

	fisher_step_sizes = ['%.4f' % i for i in np.logspace(min_step_size_in_log_space, max_step_size_in_log_space, number_of_fisher_steps_to_try)]

	filenames = [pipeline_ini_file.split('.')[0] + i.split('.')[1] + '.' + pipeline_ini_file.split('.')[1] for i in fisher_step_sizes]
	vals_filenames = [values_file.split('.')[0] + i.split('.')[1] + '.' + values_file.split('.')[1] for i in fisher_step_sizes]
	out_filenames = [output_file.split('.')[0] + i.split('.')[1] + '.' + output_file.split('.')[1] for i in fisher_step_sizes]

	for i in range(len(vals_filenames)):
		shutil.copyfile(values_file, vals_filenames[i])

	for i in range(len(filenames)):
		with open(pipeline_ini_file) as f:
			for line in f:
				if line.startswith('step_size ='):
					line = 'step_size = ' + fisher_step_sizes[i] + '\n'
				if line.startswith('vals_file ='):
					line = 'vals_file = ' + vals_filenames[i] + '\n'
				if line.startswith('out_file ='):
					line = 'out_file = ' + out_filenames[i] + '\n'
				with open(filenames[i], "a") as ini_file:
					ini_file.write(line)

	for i in range(len(filenames)):
		#executable_number = executables_counter*number_of_fisher_steps_to_try + i + 1
		exec_filename = testdir + 'exec_pipelines_%s.sh'%(executables_counter*number_of_fisher_steps_to_try + i + 1)
		print(executables_counter*number_of_fisher_steps_to_try + i + 1)
		with open(exec_filename, 'w') as exec_file:
			exec_string = ('cosmosis ' + filenames[i])
			exec_file.write(exec_string)
		os.system('chmod +x %s'%exec_filename)

	if generate_single_executable == True:
		for i in range(len(filenames)):
			#executable_number = executables_counter*number_of_fisher_steps_to_try + i + 1
			#exec_filename = testdir + 'exec_pipelines_%s.sh'%(executables_counter*number_of_fisher_steps_to_try + i + 1)
			#print(executables_counter*number_of_fisher_steps_to_try + i + 1)
			with open(single_executable, 'a') as single_file:
				cosmosis_command = ('cosmosis ' + filenames[i] + '\n')
				single_file.write(cosmosis_command)
			os.system('chmod +x %s'%exec_filename)

	executables_counter += 1


###################################################################
# CREATE JOB SCRIPT
###################################################################


job_string = ('#!/bin/bash\n'
			'#PBS -q mediumc7\n'
			'#PBS -N fisher_testing_clustering\n'
			'#PBS -t 1-%s%%10\n'
			'#PBS -l nodes=1:ppn=%s\n'
			'#PBS -l mem=20gb\n'
			'\n'
			'source /unix/atlas4/akorn/LSST/cosmosis/cosmosis/setup-my-cosmosis\n'
			'\n'
			% (len(fisher_new_values.keys())*number_of_fisher_steps_to_try, NCORES)
		)


job_string += '\n' + testdir + '/exec_pipelines_${PBS_ARRAYID}.sh\n'

with open(join(testdir, 'exec_job_array.sh'), 'w') as script:
	script.write(job_string)

