import numpy as np
from os.path import isfile
from os import remove
import shutil

#pipeline_ini_file = "/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/clustering.ini"
pipeline_ini_file = "/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/joint/joint.ini"
pipeline_template_file = "joint_template.ini"
generate_values_file = True

pipeline_values_file = "/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/joint/values_joint.ini"
#pipeline_values_file = "/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering_mag/values_clustering_mag.ini"
fisher_values_file = "values_joint_fisher.ini"
#grid_values_file = "values_clustering_mag_grid.ini"

if isfile(pipeline_template_file):
        remove(pipeline_template_file)

with open(pipeline_ini_file) as f:
        for line in f:
                if line.startswith('sampler ='):
                        line = 'sampler = \n'
                if line.startswith('out_file ='):
                        line = 'out_file = \n'
                if line.startswith('vals_file ='):
                        line = 'vals_file = \n' 
                with open(pipeline_template_file, "a") as template_file:
                        template_file.write(line)

if generate_values_file == True:
        #shutil.copyfile(pipeline_values_file, grid_values_file)
        with open(pipeline_values_file) as g:
                for line in g:
                        if "=" in line:
                                #line = line.split('=')[0] + '= ' + str(float(line.split('=')[1])-0.5) + ' ' + str(float(line.split('=')[1])) + ' ' + str(float(line.split('=')[1])+0.5) + '\n'
                                lower_lim = ' %.4f '%(float(line.split('=')[1])-0.5)
                                upper_lim = ' %.4f'%(float(line.split('=')[1])+0.5)
                                fid = line.split(' = ')[1].rstrip()
                                print(lower_lim, type(lower_lim))
                                print(upper_lim, type(upper_lim))
                                print(fid, type(fid))
                                line = line.split('=')[0] + '=' + lower_lim + fid + upper_lim + '\n'
                                #line = line.split('=')[0] + '= ' + '%'str(float(line.split('=')[1])-0.5) + ' ' + str(float(line.split('=')[1])) + ' ' + str(float(line.split('=')[1])+0.5) + '\n'
                        with open(fisher_values_file, "a") as f_vals_file:
                                f_vals_file.write(line)


