from os import listdir
from os.path import join
import numpy as np
import scipy.stats
norm = scipy.stats.norm
import matplotlib.pyplot as plt
import matplotlib.lines as ml
import math
import os


def read_and_normalise_grid(grid_dir, param):
        grid_file = [i for i in listdir(grid_dir) if param + '_grid_out.' in i]
        grid = np.loadtxt(grid_dir + grid_file[0])
        x, L = grid.T
        exp_L = [math.exp(i) for i in L]
        area = np.trapz(exp_L, x)
        L = exp_L / area
        return x, L

def find_grid_std_dev_new(x, L):
        mean_grid = np.sum(np.multiply(x,L)) / np.sum(L) #mean of frequency distribution
        var_grid = np.sum(np.multiply((np.subtract(x, mean_grid))**2.0, L)) / np.sum(L) #variance of frequency distribution
        grid_std_dev = var_grid**0.5
        return grid_std_dev
	
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
fisher_dir = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/fisher_step_sizes/fisher_jobs_clustering_gold_old/'
grid_dir= '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/fisher_step_sizes/grid_jobs_clustering_gold_old/'

grid_files = [i for i in listdir(grid_dir) if i.endswith('grid_out.txt')]
params = [i.replace('_grid_out.txt', '') for i in grid_files]
print(params)

params = sorted(params)

#print(sorted(params))

#params = [x for x in params if x.startswith('cosmo')]

if len(params)%4 == 0: x = 0 
else: x = 1 

f, axe = plt.subplots(len(params)//4 + x, 4)
ax = axe.flatten()

for i, param in enumerate(params):
        fisher_std_dev = find_fisher_std_dev(param, fisher_dir)
        
        gx, gL = read_and_normalise_grid(grid_dir, param)
        grid_std_dev = find_grid_std_dev_new(gx, gL)

        ax[i].semilogx(*zip(*fisher_std_dev.items()), linestyle = 'None', marker = 'o', label = 'fisher', color='b')
        #ax[i].axhline(y = grid_std_dev, color = 'C0', label = 'grid')

        ax[i].set_xlabel('step size', fontsize=12)
        ax[i].text(0.03, 0.6, param, verticalalignment='bottom', horizontalalignment='left', transform=ax[i].transAxes, fontsize=12)
        ax[i].set_ylabel('$\sigma$', fontsize=12)
        ax[i].tick_params(axis ='both', labelsize = 9)
        #ax[i].tick_params(bottom =False, labelbottom = False)
        #ax[i].set_yticks([])

#axe[-1,-1].axis('off')
#f.delaxes(ax.flatten()[26])
#f.delaxes(ax.flatten()[39])
#plt.legend(loc='center right', bbox_to_anchor=(1.0, 0.45))
f.set_size_inches(18, 10)
#f.set_size_inches(18, 5) 
plt.tight_layout()
plt.subplots_adjust(hspace=0.07)

plt.savefig('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/fisher_step_sizes/plots/fisher_variance_clustering_gold_clearer.pdf')
plt.show()




