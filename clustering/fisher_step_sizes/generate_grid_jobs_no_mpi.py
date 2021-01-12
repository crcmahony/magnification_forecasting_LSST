import numpy as np
import os
from os import listdir, mkdir
from os.path import isdir, join

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

pipeline_ini = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/fisher_step_sizes/shear_template.ini'
grid_vals_ini = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/fisher_step_sizes/values_shear_grid.ini'
testdir = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/fisher_step_sizes/grid_jobs_shear/'

generate_single_executable = True


if not isdir(testdir):
	mkdir(testdir)

MOD_STEPS = 0

NCORES = 1 # ncores per fisher+grid job

# find varied parameters in values
grid_varied_params = find_varied(grid_vals_ini)

grid_new_values = fix_parameters(grid_vals_ini, grid_varied_params)

new_pipelines = {}

for vp, val in grid_varied_params.values(): # cycle over each varied parameter
	# construct new pipeline .inis
	new_pipelines[vp+'_grid'] = []
	with open(pipeline_ini, 'r') as pipeline:
		for line in pipeline:
			if line.rstrip().startswith('sampler ='): # change sampler
				g_line = 'sampler = grid\n'
				new_pipelines[vp+'_grid'].append(g_line)

			elif line.rstrip() == 'vals_file =': # values
				g_line = 'vals_file = ' + testdir + 'values_%s_grid.ini\n' % vp
				new_pipelines[vp+'_grid'].append(g_line)

			elif line.rstrip() == 'out_file =': # and output
				g_line = 'out_file = ' + testdir + '%s_grid_out.txt\n' % vp
				new_pipelines[vp+'_grid'].append(g_line)

			else:
				new_pipelines[vp+'_grid'].append(line)


if generate_single_executable == True:
	single_executable = join(testdir, 'execute_pipelines.sh')
	with open(single_executable, 'w') as single_file:
		bash_prefix = ('#!/bin/bash\n')
		single_file.write(bash_prefix)
	os.system('chmod +x %s'%single_executable)
		
	
job_string = ('#!/bin/bash\n'
			'#PBS -q mediumc7\n'
			'#PBS -N grid_sampler\n'
			#'#PBS -t 1-%s%%10\n'
			#'#PBS -l nodes=1:ppn=%s\n'
                        '#PBS -l nodes=1:ppn=1:typeb\n'
			'#PBS -l mem=20gb\n'
			'\n'
                        'source /unix/atlas4/akorn/LSST/cosmosis/cosmosis/setup-my-cosmosis\n\n'
			#% (len(grid_new_values.keys()), NCORES)
		)


with open(join(testdir, 'exec_all_jobs.sh'), 'w') as script:
	script.write('#!/bin/bash\n')
os.system('chmod +x %s'%join(testdir, 'exec_all_jobs.sh'))


# save values.inis
for i, key in enumerate(grid_new_values.keys()):
	with open(join(testdir, "values_%s_grid.ini"%key), 'w') as new_vini:
		for line in grid_new_values[key]:
			new_vini.write(line)

	# make executables
	exec_filename = join(testdir, 'exec_pipeline_%s.sh'%(i+1))
	with open(exec_filename, 'w') as exec_file:
		exec_string = (#'#!/bin/bash\n'
				'echo "' + key + '"\n\n'

				'cosmosis ' + testdir + 'pipeline_' + key + '_grid.ini\n\n'
				)
		exec_file.write(job_string + '\n' + exec_string)
	os.system('chmod +x %s'%exec_filename)

	with open(join(testdir, 'exec_all_jobs.sh'), 'a') as script:
		script.write('qsub exec_pipeline_%s.sh\n'%(i+1))

	

	if generate_single_executable == True:
		with open(single_executable, 'a') as single_file:
			cosmosis_command = (#'#!/bin/bash\n'
					'echo "' + key + '"\n\n'
					'cosmosis ' + testdir + 'pipeline_' + key + '_grid.ini\n\n')
			single_file.write(cosmosis_command)

	
		

# save pipeline.inis
for key, new_pipeline in new_pipelines.items():
	with open(join(testdir, "pipeline_%s.ini"%key), 'w') as new_pipe:
		for line in new_pipeline:
			new_pipe.write(line)







