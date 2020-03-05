import numpy as np
from os.path import isfile
from os import remove
import shutil

######Create step size dictionary from list of fisher files

optimum_step_size_fisher_filenames = {}

optimum_step_size_fisher_filenames['cosmological_parameters--omega_m'] = 'cosmological_parameters--omega_m_fisher_out0010.txt'
optimum_step_size_fisher_filenames['cosmological_parameters--h0'] = 'cosmological_parameters--h0_fisher_out0010.txt'
optimum_step_size_fisher_filenames['cosmological_parameters--omega_b'] = 'cosmological_parameters--omega_b_fisher_out0010.txt'
optimum_step_size_fisher_filenames['cosmological_parameters--n_s'] = 'cosmological_parameters--n_s_fisher_out0022.txt'
optimum_step_size_fisher_filenames['cosmological_parameters--e9A_s'] = 'cosmological_parameters--e9A_s_fisher_out0022.txt'
optimum_step_size_fisher_filenames['cosmological_parameters--w'] = 'cosmological_parameters--w_fisher_out0022.txt'
optimum_step_size_fisher_filenames['cosmological_parameters--wa'] = 'cosmological_parameters--wa_fisher_out0022.txt'

optimum_step_size_fisher_filenames['hod_parameters--lgM1'] = 'hod_parameters--lgM1_fisher_out0022.txt'
optimum_step_size_fisher_filenames['hod_parameters--lgl0'] = 'hod_parameters--lgl0_fisher_out0022.txt'
optimum_step_size_fisher_filenames['hod_parameters--g1'] = 'hod_parameters--g1_fisher_out0022.txt'
optimum_step_size_fisher_filenames['hod_parameters--g2'] = 'hod_parameters--g2_fisher_out0022.txt'
optimum_step_size_fisher_filenames['hod_parameters--scatter'] = 'hod_parameters--scatter_fisher_out0022.txt'
optimum_step_size_fisher_filenames['hod_parameters--alfa_s'] = 'hod_parameters--alfa_s_fisher_out0022.txt'
optimum_step_size_fisher_filenames['hod_parameters--b0'] = 'hod_parameters--b0_fisher_out0022.txt'
optimum_step_size_fisher_filenames['hod_parameters--b1'] = 'hod_parameters--b1_fisher_out0022.txt'
optimum_step_size_fisher_filenames['hod_parameters--b2'] = 'hod_parameters--b2_fisher_out0022.txt'

optimum_step_size_fisher_filenames['nz_n_sample_errors--bias_1'] = 'nz_n_sample_errors--bias_1_fisher_out0046.txt'
optimum_step_size_fisher_filenames['nz_n_sample_errors--bias_2'] = 'nz_n_sample_errors--bias_2_fisher_out0010.txt'
optimum_step_size_fisher_filenames['nz_n_sample_errors--bias_3'] = 'nz_n_sample_errors--bias_3_fisher_out0010.txt'
optimum_step_size_fisher_filenames['nz_n_sample_errors--bias_4'] = 'nz_n_sample_errors--bias_4_fisher_out0022.txt'
optimum_step_size_fisher_filenames['nz_n_sample_errors--bias_5'] = 'nz_n_sample_errors--bias_5_fisher_out0022.txt'
optimum_step_size_fisher_filenames['nz_n_sample_errors--bias_6'] = 'nz_n_sample_errors--bias_6_fisher_out0022.txt'
optimum_step_size_fisher_filenames['nz_n_sample_errors--bias_7'] = 'nz_n_sample_errors--bias_7_fisher_out0046.txt'
optimum_step_size_fisher_filenames['nz_n_sample_errors--bias_8'] = 'nz_n_sample_errors--bias_8_fisher_out0100.txt'
optimum_step_size_fisher_filenames['nz_n_sample_errors--bias_9'] = 'nz_n_sample_errors--bias_9_fisher_out0100.txt'
optimum_step_size_fisher_filenames['nz_n_sample_errors--bias_10'] = 'nz_n_sample_errors--bias_10_fisher_out0464.txt'

step_size_files = list(optimum_step_size_fisher_filenames.values())
no_section_labels = [i.split('--')[1] for i in step_size_files]
params_in_values = [i.split('_fisher_out')[0] for i in no_section_labels]
step_size_with_txt = [i.split('_fisher_out')[1] for i in no_section_labels]
step_size = [float('0.' + i.split('.')[0]) for i in step_size_with_txt]
step_sizes = dict(zip(params_in_values, step_size)) 

print(tuple(step_sizes.keys()))


pipeline_values_file = "/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/values_clustering.ini"
fisher_values_file = "/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/values_clustering_fisher.ini"

with open(pipeline_values_file) as f:
	for line in f:
		print(line)
		if line.startswith(tuple(step_sizes.keys())):
			print(line.split(' = ')[0])
			param = line.split(' = ')[0]
			print(param)
			fid_value = line.split(' = ')[1].rstrip()
			print(fid_value)
			width = step_sizes[param]/0.01
			print(width)
			max_value = float(fid_value) + width/2.0
			min_value = float(fid_value) - width/2.0
			line = line.split(' = ')[0] + ' = ' + str(min_value) + ' ' + fid_value + ' ' + str(max_value) + '\n'
		else:
			line=line
		with open(fisher_values_file, "a") as f_vals_file:
			f_vals_file.write(line)
