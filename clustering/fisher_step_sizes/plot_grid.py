from os import listdir
from os.path import join
import numpy as np
import scipy.stats
norm = scipy.stats.norm
import matplotlib.pyplot as plt
import matplotlib.lines as ml
import math

def read_and_normalise_grid(grid_dir, param):
        grid_file = [i for i in listdir(grid_dir) if param + '_grid_out.' in i]
        print(grid_file)
        grid = np.loadtxt(grid_dir + grid_file[0])
        x, L = grid.T
        #print(x, L)
        exp_L = [math.exp(i) for i in L]
        area = np.trapz(exp_L, x)
        L = exp_L / area
        return x, L

grid_dir = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/fisher_step_sizes/grid_jobs_shear/'
#grid_dir2 = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/fisher_step_sizes/grid_jobs_clustering_mag_gold/'

grid_files = [i for i in listdir(grid_dir) if i.endswith('grid_out.txt')]
params = [i.replace('_grid_out.txt', '') for i in grid_files]
#print(params)
#params = [x for x in params if x.startswith('cos')]
#print(len(params))

if len(params)%4 == 0: x = 0 
else: x = 1 

f, axe = plt.subplots(len(params)//4 + x, 4)
ax = axe.flatten()

for i, param in enumerate(params):
    gx, gf = read_and_normalise_grid(grid_dir, param)
    ax[i].plot(gx, gf, c='C0', label='clustering magnification n-sample') #, zorder=10)
    #mean_grid = np.sum(np.multiply(gx,gf)) / np.sum(gf)
    #var_grid = np.sum(np.multiply((np.subtract(gx,mean_grid))**2.0, gf)) / np.sum(gf)

    #gx2, gf2 = read_and_normalise_grid(grid_dir2, param)
    #ax[i].plot(gx2, gf2, c='C0', ls='--', label='clustering magnification e-sample')    

    ax[i].set_xlabel(str(param), fontsize=12)
    ax[i].set_ylabel('P', fontsize=12)
    ax[i].xaxis.set_major_locator(plt.MaxNLocator(4))
    ax[i].tick_params(axis ='both', labelsize = 9)


#axe[-1,-1].axis('off')
f.set_size_inches(18, 10) 
#f.delaxes(ax.flatten()[39])
#f.delaxes(ax.flatten()[19])

plt.tight_layout()
#plt.legend(bbox_to_anchor=(1.6, 0.97))
#plt.subplots_adjust(wspace=0)
plt.savefig('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/fisher_step_sizes/plots/rerun_cacciato/grid_shear.png')
plt.show()
