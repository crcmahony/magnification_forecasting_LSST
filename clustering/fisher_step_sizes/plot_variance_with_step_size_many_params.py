from os import listdir
from os.path import join
import numpy as np
import scipy.stats
norm = scipy.stats.norm
import matplotlib.pyplot as plt
import matplotlib.lines as ml
import math
import os

def find_fisher_std_dev(param, fisher_dir):

	fisher_files = [i for i in listdir(fisher_dir) if param + '_fisher_out' in i]

	step_sizes = [ '0.' + (i.split('out')[1]).split('.')[0] for i in fisher_files]

	fisher_std_dev = {}

	for i in range(len(fisher_files)):
		if os.stat(fisher_dir + fisher_files[i]).st_size != 0:
			fisher = np.loadtxt(fisher_dir + fisher_files[i])
			std_dev = (fisher**(-1.))**0.5
			fisher_std_dev[float(step_sizes[i])] = std_dev

	return fisher_std_dev

def find_grid_std_dev(param, grid_dir):
	grid_file = [i for i in listdir(grid_dir) if param + '_grid_out.' in i]
	#print grid_file
	grid = np.loadtxt(grid_dir + grid_file[0])

	gx, gL = grid.T
	exp_gL = [math.exp(i) for i in gL]
	area = np.trapz(exp_gL, gx)
	gL = exp_gL / area

	mean_grid = np.sum(np.multiply(gx,gL)) / np.sum(gL) #mean of frequency distribution
	var_grid = np.sum(np.multiply((np.subtract(gx, mean_grid))**2.0, gL)) / np.sum(gL) #variance of frequency distribution
	grid_std_dev = var_grid**0.5
	
	return grid_std_dev



fisher_dir = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/fisher_step_sizes/fisher_jobs/'
grid_dir= '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/fisher_step_sizes/grid_jobs_2/'

grid_files = [i for i in listdir(grid_dir) if i.endswith('grid_out.txt')]
params = [i.replace('_grid_out.txt', '') for i in grid_files]
print(params)

#params = ['cosmological_parameters--h0']


if len(params)%4 == 0: x = 0 
else: x = 1 

f, axe = plt.subplots(len(params)//4 + x, 4)
#f, axe = plt.subplots(1,2)
ax = axe.flatten()

for i, param in enumerate(params):
        fisher_std_dev = find_fisher_std_dev(param, fisher_dir)
        grid_std_dev = find_grid_std_dev(param, grid_dir)

        print(fisher_std_dev)


        ax[i].semilogx(*zip(*fisher_std_dev.items()), linestyle = 'None', marker = 'o', label = 'fisher')
        ax[i].axhline(y = grid_std_dev, color = 'r', label = 'grid')

        ax[i].set_xlabel(param)
        #ax[i].set_ylabel('standard deviation')
        ax[i].set_yticks([])

#axe[-1,-1].axis('off')
#f.delaxes(ax.flatten()[26])
#f.delaxes(ax.flatten()[27])
f.set_size_inches(18, 12) 
plt.tight_layout()
plt.subplots_adjust(wspace=0)
plt.legend()
plt.savefig('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/fisher_step_sizes/plots/fisher_grid_variance_clustering.png')
plt.show()




