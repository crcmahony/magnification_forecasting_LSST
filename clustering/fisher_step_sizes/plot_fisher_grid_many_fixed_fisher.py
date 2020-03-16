import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.lines as mlines
from os import listdir
import scipy.stats
norm = scipy.stats.norm
import math

def read_and_normalise_grid(grid_dir, param):
        grid_file = [i for i in listdir(grid_dir) if param + '_grid_out.' in i]
        grid = np.loadtxt(grid_dir + grid_file[0])
        x, L = grid.T
        #exp_L = [math.exp(i) for i in L]
        #area = np.trapz(exp_L, x)
        #L = exp_L / area
        return x, L


def calculate_fisher_std_dev(fisher_dir, optimum_step_size_fisher_filename):
        fisher = np.loadtxt(fisher_dir + optimum_step_size_fisher_filename)
        std_dev = (fisher**(-1.))**0.5
        return std_dev




fisher_dir = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/fisher_step_sizes/fisher_jobs_mag_fixed/'
grid_dir= '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/fisher_step_sizes/grid_jobs_mag/'


grid_files = [i for i in listdir(grid_dir) if i.endswith('grid_out.txt')]
params = [i.replace('_grid_out.txt', '') for i in grid_files]
print(params)

if len(params)%4 == 0: x = 0 
else: x = 1 

f, axe = plt.subplots(len(params)//4 + x, 4)
#f, axe = plt.subplots(1, 2)
ax = axe.flatten()

for i, param in enumerate(params):
        x, L = read_and_normalise_grid(grid_dir, param)
        fisher_file = [i for i in listdir(fisher_dir) if param + '_fisher_out.' in i]
        print(fisher_file)
        fisher_std_dev = calculate_fisher_std_dev(fisher_dir, fisher_file[0])

        ax[i].plot(x, L, c='r')

        max_like = x[np.where(L==L.max())]
        x_for_fisher_pdf = np.linspace(x.min(), x.max(), 1000)
        #pdf = norm.pdf(x_for_fisher_pdf, loc=max_like, scale=fisher_std_dev)
        pdf = norm.logpdf(x_for_fisher_pdf, loc=max_like, scale=fisher_std_dev)
        pdf_shifted_to_zero = pdf - max(pdf)
        ax[i].plot(x_for_fisher_pdf, pdf_shifted_to_zero, c='b', ls='--')
        #ax[i].plot(x_for_fisher_pdf, pdf, c='b')

        ax[i].set_xlabel(param)
        ax[i].set_ylabel('Log Posterior')
        #ax[i].set_ylabel('Posterior')

#axe[-1,-1].axis('off')
#f.delaxes(ax.flatten()[26])
#f.delaxes(ax.flatten()[27])
f.set_size_inches(18, 12) 
plt.tight_layout()
plt.subplots_adjust(wspace=0)
plt.legend()
plt.savefig('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/fisher_step_sizes/plots/fisher_grid_check_clustering_mag.png')
plt.show()






