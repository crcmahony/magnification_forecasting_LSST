from os import listdir
from os.path import join
import numpy as np
import scipy.stats
norm = scipy.stats.norm
import matplotlib.pyplot as plt
import matplotlib.lines as ml
import math

def new_handle(**kwargs):
    return ml.Line2D([], [], **kwargs)

testdir = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/fisher_step_sizes/grid_jobs_mag/'
grid_files = [i for i in listdir(testdir) if i.endswith('grid_out.txt')]
    
marginals = {}

params = [i.replace('_grid_out.txt', '') for i in grid_files]
for param in params:    
    grid = np.loadtxt(join(testdir, param+'_grid_out.txt')) 
    x, L = grid.T
    exp_L = [math.exp(i) for i in L]
    area = np.trapz(exp_L, x)
    L = exp_L / area 
    marginals[param+'_grid'] = np.column_stack((x, L))    

print(params)
print(len(params))

if len(params)%4 == 0:
    print(len(params)%4)
    x = 0 
else: 
    x = 1 

f, axe = plt.subplots(len(params)//4 + x, 4)
#f, axe = plt.subplots(1, 2)
print(len(params)//4 + x)
ax = axe.flatten()
for i, param in enumerate(params):
    print(i)
    grid = np.loadtxt(join(testdir, param+'_grid_out.txt')) 
    gx, gf = marginals[param+'_grid'].T
    ax[i].plot(gx, gf, c='g', zorder=10)
    mean_grid = np.sum(np.multiply(gx,gf)) / np.sum(gf)
    var_grid = np.sum(np.multiply((np.subtract(gx,mean_grid))**2.0, gf)) / np.sum(gf)

    #h = [new_handle(ls='', label='\n'.join(param.split('--')))]
    #ax[i].legend(handles=h, loc='best', fontsize=8)
    #ax[i].xaxis.set_ticks([])
    #ax[i].yaxis.set_ticks([])
	
    ax[i].set_ylabel('Posterior')
    ax[i].set_xlabel(str(param))


#axe[-1,-1].axis('off')
f.set_size_inches(18, 12) 
plt.tight_layout()
plt.subplots_adjust(wspace=0)
#plt.savefig('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/fisher_step_sizes/grid_L_nz_fixed.png')
plt.show()
