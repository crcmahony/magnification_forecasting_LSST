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




fisher_dir = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/fisher_step_sizes/fisher_jobs/'
grid_dir= '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/fisher_step_sizes/grid_jobs_2/'


grid_files = [i for i in listdir(grid_dir) if i.endswith('grid_out.txt')]
params = [i.replace('_grid_out.txt', '') for i in grid_files]
print(params)



optimum_step_size_fisher_filenames = dict.fromkeys(params)

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

optimum_step_size_fisher_filenames['nz_n_sample_errors--bias_1'] = 'nz_n_sample_errors--bias_1_fisher_out0022.txt'
optimum_step_size_fisher_filenames['nz_n_sample_errors--bias_2'] = 'nz_n_sample_errors--bias_2_fisher_out0022.txt'
optimum_step_size_fisher_filenames['nz_n_sample_errors--bias_3'] = 'nz_n_sample_errors--bias_3_fisher_out0022.txt'
optimum_step_size_fisher_filenames['nz_n_sample_errors--bias_4'] = 'nz_n_sample_errors--bias_4_fisher_out0022.txt'
optimum_step_size_fisher_filenames['nz_n_sample_errors--bias_5'] = 'nz_n_sample_errors--bias_5_fisher_out0022.txt'
optimum_step_size_fisher_filenames['nz_n_sample_errors--bias_6'] = 'nz_n_sample_errors--bias_6_fisher_out0022.txt'
optimum_step_size_fisher_filenames['nz_n_sample_errors--bias_7'] = 'nz_n_sample_errors--bias_7_fisher_out0022.txt'
optimum_step_size_fisher_filenames['nz_n_sample_errors--bias_8'] = 'nz_n_sample_errors--bias_8_fisher_out0022.txt'
optimum_step_size_fisher_filenames['nz_n_sample_errors--bias_9'] = 'nz_n_sample_errors--bias_9_fisher_out0022.txt'
optimum_step_size_fisher_filenames['nz_n_sample_errors--bias_10'] = 'nz_n_sample_errors--bias_10_fisher_out0022.txt'

#optimum_step_size_fisher_filenames['magnification_bias--alpha_m'] = 'magnification_bias--alpha_m_fisher_out0022.txt'
#optimum_step_size_fisher_filenames['magnification_bias--beta_m'] = 'magnification_bias--beta_m_fisher_out0022.txt'

print(optimum_step_size_fisher_filenames)

if len(params)%4 == 0: x = 0 
else: x = 1 

f, axe = plt.subplots(len(params)//4 + x, 4)
#f, axe = plt.subplots(1, 2)
ax = axe.flatten()

for i, param in enumerate(params):
        x, L = read_and_normalise_grid(grid_dir, param)
        print(optimum_step_size_fisher_filenames[param])
        fisher_std_dev = calculate_fisher_std_dev(fisher_dir, optimum_step_size_fisher_filenames[param])

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
#plt.savefig('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/fisher_step_sizes/plots/fisher_grid_matched_clustering_mag.png')
plt.show()






