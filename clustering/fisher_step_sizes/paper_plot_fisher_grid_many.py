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
        exp_L = [math.exp(i) for i in L]
        area = np.trapz(exp_L, x)
        L = exp_L / area
        return x, L


def calculate_fisher_std_dev(fisher_dir, optimum_step_size_fisher_filename):
        fisher = np.loadtxt(fisher_dir + optimum_step_size_fisher_filename)
        std_dev = (fisher**(-1.))**0.5
        return std_dev

fisher_dir = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/fisher_step_sizes/fisher_jobs_clustering_mag/'
grid_dir= '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/fisher_step_sizes/grid_jobs_clustering_mag/'
step_size_choice = 'clustering_mag'
plot_type = 'overlay' #'percentage_diff'

grid_files = [i for i in listdir(grid_dir) if i.endswith('grid_out.txt')]
params = [i.replace('_grid_out.txt', '') for i in grid_files]

#### for subset
#params = [x for x in params if x.startswith('cosmo') or x.startswith('hod')]
#params = [x for x in params if not x.startswith('cosmo') and not x.startswith('hod')]
print(len(params))

fish_files = dict.fromkeys(params)



if step_size_choice == 'clustering':
        fish_files['cosmological_parameters--omega_m'] = 'cosmological_parameters--omega_m_fisher_out0005.txt'
        fish_files['cosmological_parameters--h0'] = 'cosmological_parameters--h0_fisher_out0005.txt'
        fish_files['cosmological_parameters--omega_b'] = 'cosmological_parameters--omega_b_fisher_out0005.txt'
        fish_files['cosmological_parameters--n_s'] = 'cosmological_parameters--n_s_fisher_out0005.txt'
        fish_files['cosmological_parameters--e9A_s'] = 'cosmological_parameters--e9A_s_fisher_out0005.txt'
        fish_files['cosmological_parameters--w'] = 'cosmological_parameters--w_fisher_out0022.txt'
        fish_files['cosmological_parameters--wa'] = 'cosmological_parameters--wa_fisher_out0215.txt'
        
        fish_files['hod_parameters--lgM1'] = 'hod_parameters--lgM1_fisher_out0005.txt'
        fish_files['hod_parameters--lgl0'] = 'hod_parameters--lgl0_fisher_out0005.txt'
        fish_files['hod_parameters--g1'] = 'hod_parameters--g1_fisher_out0005.txt'
        fish_files['hod_parameters--g2'] = 'hod_parameters--g2_fisher_out0005.txt'
        fish_files['hod_parameters--scatter'] = 'hod_parameters--scatter_fisher_out0005.txt'
        fish_files['hod_parameters--alfa_s'] = 'hod_parameters--alfa_s_fisher_out0005.txt'
        fish_files['hod_parameters--b0'] = 'hod_parameters--b0_fisher_out0005.txt'
        fish_files['hod_parameters--b1'] = 'hod_parameters--b1_fisher_out0005.txt'
        fish_files['hod_parameters--b2'] = 'hod_parameters--b2_fisher_out0005.txt'

        fish_files['nz_n_sample_errors--bias_1'] = 'nz_n_sample_errors--bias_1_fisher_out0005.txt'
        fish_files['nz_n_sample_errors--bias_2'] = 'nz_n_sample_errors--bias_2_fisher_out0005.txt'
        fish_files['nz_n_sample_errors--bias_3'] = 'nz_n_sample_errors--bias_3_fisher_out0005.txt'
        fish_files['nz_n_sample_errors--bias_4'] = 'nz_n_sample_errors--bias_4_fisher_out0005.txt'
        fish_files['nz_n_sample_errors--bias_5'] = 'nz_n_sample_errors--bias_5_fisher_out0005.txt'
        fish_files['nz_n_sample_errors--bias_6'] = 'nz_n_sample_errors--bias_6_fisher_out0005.txt'
        fish_files['nz_n_sample_errors--bias_7'] = 'nz_n_sample_errors--bias_7_fisher_out0005.txt'
        fish_files['nz_n_sample_errors--bias_8'] = 'nz_n_sample_errors--bias_8_fisher_out0005.txt'
        fish_files['nz_n_sample_errors--bias_9'] = 'nz_n_sample_errors--bias_9_fisher_out0005.txt'
        fish_files['nz_n_sample_errors--bias_10'] = 'nz_n_sample_errors--bias_10_fisher_out0100.txt'

        fish_files['magnification_bias--alpha_m'] = 'magnification_bias--alpha_m_fisher_out0005.txt'
        fish_files['magnification_bias--beta_m'] = 'magnification_bias--beta_m_fisher_out0005.txt'

if step_size_choice == 'clustering_gold':
        fish_files['cosmological_parameters--omega_m'] = 'cosmological_parameters--omega_m_fisher_out0005.txt' #0022.txt
        fish_files['cosmological_parameters--h0'] = 'cosmological_parameters--h0_fisher_out0010.txt'
        fish_files['cosmological_parameters--omega_b'] = 'cosmological_parameters--omega_b_fisher_out0010.txt' #0005.txt
        fish_files['cosmological_parameters--n_s'] = 'cosmological_parameters--n_s_fisher_out0005.txt'
        fish_files['cosmological_parameters--e9A_s'] = 'cosmological_parameters--e9A_s_fisher_out0005.txt' #100.txt'
        fish_files['cosmological_parameters--w'] = 'cosmological_parameters--w_fisher_out0005.txt' #0010.txt'
        fish_files['cosmological_parameters--wa'] = 'cosmological_parameters--wa_fisher_out0005.txt' #0046.txt'

        fish_files['hod_parameters--lgM1'] = 'hod_parameters--lgM1_fisher_out0005.txt'
        fish_files['hod_parameters--lgl0'] = 'hod_parameters--lgl0_fisher_out0005.txt'
        fish_files['hod_parameters--g1'] = 'hod_parameters--g1_fisher_out0005.txt'
        fish_files['hod_parameters--g2'] = 'hod_parameters--g2_fisher_out0005.txt'
        fish_files['hod_parameters--scatter'] = 'hod_parameters--scatter_fisher_out0005.txt' #0046.txt'
        fish_files['hod_parameters--alfa_s'] = 'hod_parameters--alfa_s_fisher_out0005.txt'
        fish_files['hod_parameters--b0'] = 'hod_parameters--b0_fisher_out0005.txt'
        fish_files['hod_parameters--b1'] = 'hod_parameters--b1_fisher_out0005.txt'
        fish_files['hod_parameters--b2'] = 'hod_parameters--b2_fisher_out0005.txt'

        fish_files['nz_e_sample_errors--bias_1'] = 'nz_e_sample_errors--bias_1_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_2'] = 'nz_e_sample_errors--bias_2_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_3'] = 'nz_e_sample_errors--bias_3_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_4'] = 'nz_e_sample_errors--bias_4_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_5'] = 'nz_e_sample_errors--bias_5_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_6'] = 'nz_e_sample_errors--bias_6_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_7'] = 'nz_e_sample_errors--bias_7_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_8'] = 'nz_e_sample_errors--bias_8_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_9'] = 'nz_e_sample_errors--bias_9_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_10'] = 'nz_e_sample_errors--bias_10_fisher_out0022.txt'

        fish_files['magnification_bias--alpha_m'] = 'magnification_bias--alpha_m_fisher_out0005.txt'
        fish_files['magnification_bias--beta_m'] = 'magnification_bias--beta_m_fisher_out0005.txt'

if step_size_choice == 'clustering_mag':
        fish_files['cosmological_parameters--omega_m'] = 'cosmological_parameters--omega_m_fisher_out0022.txt'
        fish_files['cosmological_parameters--h0'] = 'cosmological_parameters--h0_fisher_out0022.txt' #0010.txt'
        fish_files['cosmological_parameters--omega_b'] = 'cosmological_parameters--omega_b_fisher_out0022.txt' #0005.txt'
        fish_files['cosmological_parameters--n_s'] = 'cosmological_parameters--n_s_fisher_out0022.txt' #0010.txt'
        fish_files['cosmological_parameters--e9A_s'] = 'cosmological_parameters--e9A_s_fisher_out0046.txt' #0022.txt'
        fish_files['cosmological_parameters--w'] = 'cosmological_parameters--w_fisher_out0215.txt' #0010.txt'
        fish_files['cosmological_parameters--wa'] = 'cosmological_parameters--wa_fisher_out0215.txt'

        fish_files['hod_parameters--lgM1'] = 'hod_parameters--lgM1_fisher_out0005.txt'
        fish_files['hod_parameters--lgl0'] = 'hod_parameters--lgl0_fisher_out0005.txt'
        fish_files['hod_parameters--g1'] = 'hod_parameters--g1_fisher_out0005.txt'
        fish_files['hod_parameters--g2'] = 'hod_parameters--g2_fisher_out0005.txt'
        fish_files['hod_parameters--scatter'] = 'hod_parameters--scatter_fisher_out0005.txt'
        fish_files['hod_parameters--alfa_s'] = 'hod_parameters--alfa_s_fisher_out0005.txt'
        fish_files['hod_parameters--b0'] = 'hod_parameters--b0_fisher_out0005.txt'
        fish_files['hod_parameters--b1'] = 'hod_parameters--b1_fisher_out0005.txt'
        fish_files['hod_parameters--b2'] = 'hod_parameters--b2_fisher_out0005.txt'

        fish_files['nz_n_sample_errors--bias_1'] = 'nz_n_sample_errors--bias_1_fisher_out0005.txt'
        fish_files['nz_n_sample_errors--bias_2'] = 'nz_n_sample_errors--bias_2_fisher_out0005.txt'
        fish_files['nz_n_sample_errors--bias_3'] = 'nz_n_sample_errors--bias_3_fisher_out0005.txt'
        fish_files['nz_n_sample_errors--bias_4'] = 'nz_n_sample_errors--bias_4_fisher_out0005.txt'
        fish_files['nz_n_sample_errors--bias_5'] = 'nz_n_sample_errors--bias_5_fisher_out0005.txt'
        fish_files['nz_n_sample_errors--bias_6'] = 'nz_n_sample_errors--bias_6_fisher_out0005.txt'
        fish_files['nz_n_sample_errors--bias_7'] = 'nz_n_sample_errors--bias_7_fisher_out0005.txt'
        fish_files['nz_n_sample_errors--bias_8'] = 'nz_n_sample_errors--bias_8_fisher_out0005.txt'
        fish_files['nz_n_sample_errors--bias_9'] = 'nz_n_sample_errors--bias_9_fisher_out0005.txt'
        fish_files['nz_n_sample_errors--bias_10'] = 'nz_n_sample_errors--bias_10_fisher_out0100.txt'

        fish_files['magnification_bias--alpha_m'] = 'magnification_bias--alpha_m_fisher_out0005.txt'
        fish_files['magnification_bias--beta_m'] = 'magnification_bias--beta_m_fisher_out0005.txt'

if step_size_choice == 'clustering_mag_gold':
        fish_files['cosmological_parameters--omega_m'] = 'cosmological_parameters--omega_m_fisher_out0005.txt'
        fish_files['cosmological_parameters--h0'] = 'cosmological_parameters--h0_fisher_out0005.txt'
        fish_files['cosmological_parameters--omega_b'] = 'cosmological_parameters--omega_b_fisher_out0010.txt'
        fish_files['cosmological_parameters--n_s'] = 'cosmological_parameters--n_s_fisher_out0005.txt'
        fish_files['cosmological_parameters--e9A_s'] = 'cosmological_parameters--e9A_s_fisher_out0022.txt'
        fish_files['cosmological_parameters--w'] = 'cosmological_parameters--w_fisher_out0022.txt'
        fish_files['cosmological_parameters--wa'] = 'cosmological_parameters--wa_fisher_out0046.txt'

        fish_files['hod_parameters--lgM1'] = 'hod_parameters--lgM1_fisher_out0005.txt'
        fish_files['hod_parameters--lgl0'] = 'hod_parameters--lgl0_fisher_out0005.txt'
        fish_files['hod_parameters--g1'] = 'hod_parameters--g1_fisher_out0005.txt'
        fish_files['hod_parameters--g2'] = 'hod_parameters--g2_fisher_out0005.txt'
        fish_files['hod_parameters--scatter'] = 'hod_parameters--scatter_fisher_out0005.txt'
        fish_files['hod_parameters--alfa_s'] = 'hod_parameters--alfa_s_fisher_out0005.txt'
        fish_files['hod_parameters--b0'] = 'hod_parameters--b0_fisher_out0005.txt'
        fish_files['hod_parameters--b1'] = 'hod_parameters--b1_fisher_out0005.txt'
        fish_files['hod_parameters--b2'] = 'hod_parameters--b2_fisher_out0005.txt'

        fish_files['nz_e_sample_errors--bias_1'] = 'nz_e_sample_errors--bias_1_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_2'] = 'nz_e_sample_errors--bias_2_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_3'] = 'nz_e_sample_errors--bias_3_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_4'] = 'nz_e_sample_errors--bias_4_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_5'] = 'nz_e_sample_errors--bias_5_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_6'] = 'nz_e_sample_errors--bias_6_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_7'] = 'nz_e_sample_errors--bias_7_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_8'] = 'nz_e_sample_errors--bias_8_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_9'] = 'nz_e_sample_errors--bias_9_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_10'] = 'nz_e_sample_errors--bias_10_fisher_out0022.txt'

        fish_files['magnification_bias--alpha_m'] = 'magnification_bias--alpha_m_fisher_out0005.txt'
        fish_files['magnification_bias--beta_m'] = 'magnification_bias--beta_m_fisher_out0005.txt'

if step_size_choice == 'joint_gold':
        fish_files['cosmological_parameters--omega_m'] = 'cosmological_parameters--omega_m_fisher_out0005.txt'
        fish_files['cosmological_parameters--h0'] = 'cosmological_parameters--h0_fisher_out0010.txt'
        fish_files['cosmological_parameters--omega_b'] = 'cosmological_parameters--omega_b_fisher_out0005.txt'
        fish_files['cosmological_parameters--n_s'] = 'cosmological_parameters--n_s_fisher_out0005.txt'
        fish_files['cosmological_parameters--e9A_s'] = 'cosmological_parameters--e9A_s_fisher_out0046.txt'
        fish_files['cosmological_parameters--w'] = 'cosmological_parameters--w_fisher_out0046.txt'
        fish_files['cosmological_parameters--wa'] = 'cosmological_parameters--wa_fisher_out0215.txt'

        fish_files['hod_parameters--lgM1'] = 'hod_parameters--lgM1_fisher_out0005.txt'
        fish_files['hod_parameters--lgl0'] = 'hod_parameters--lgl0_fisher_out0010.txt'
        fish_files['hod_parameters--g1'] = 'hod_parameters--g1_fisher_out0046.txt'
        fish_files['hod_parameters--g2'] = 'hod_parameters--g2_fisher_out0005.txt'
        fish_files['hod_parameters--scatter'] = 'hod_parameters--scatter_fisher_out0100.txt'
        fish_files['hod_parameters--alfa_s'] = 'hod_parameters--alfa_s_fisher_out0005.txt'
        fish_files['hod_parameters--b0'] = 'hod_parameters--b0_fisher_out0005.txt'
        fish_files['hod_parameters--b1'] = 'hod_parameters--b1_fisher_out0005.txt'
        fish_files['hod_parameters--b2'] = 'hod_parameters--b2_fisher_out0005.txt'

        fish_files['nz_e_sample_errors--bias_1'] = 'nz_e_sample_errors--bias_1_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_2'] = 'nz_e_sample_errors--bias_2_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_3'] = 'nz_e_sample_errors--bias_3_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_4'] = 'nz_e_sample_errors--bias_4_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_5'] = 'nz_e_sample_errors--bias_5_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_6'] = 'nz_e_sample_errors--bias_6_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_7'] = 'nz_e_sample_errors--bias_7_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_8'] = 'nz_e_sample_errors--bias_8_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_9'] = 'nz_e_sample_errors--bias_9_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_10'] = 'nz_e_sample_errors--bias_10_fisher_out0022.txt'

        fish_files['ia_parameters--gamma_2h'] = 'ia_parameters--gamma_2h_fisher_out0005.txt'

        fish_files['shear_calibration_parameters--m1'] = 'shear_calibration_parameters--m1_fisher_out0005.txt'
        fish_files['shear_calibration_parameters--m2'] = 'shear_calibration_parameters--m2_fisher_out0005.txt'
        fish_files['shear_calibration_parameters--m3'] = 'shear_calibration_parameters--m3_fisher_out0005.txt'
        fish_files['shear_calibration_parameters--m4'] = 'shear_calibration_parameters--m4_fisher_out0005.txt'
        fish_files['shear_calibration_parameters--m5'] = 'shear_calibration_parameters--m5_fisher_out0005.txt'
        fish_files['shear_calibration_parameters--m6'] = 'shear_calibration_parameters--m6_fisher_out0005.txt'
        fish_files['shear_calibration_parameters--m7'] = 'shear_calibration_parameters--m7_fisher_out0005.txt'
        fish_files['shear_calibration_parameters--m8'] = 'shear_calibration_parameters--m8_fisher_out0005.txt'
        fish_files['shear_calibration_parameters--m9'] = 'shear_calibration_parameters--m9_fisher_out0005.txt'
        fish_files['shear_calibration_parameters--m10'] = 'shear_calibration_parameters--m10_fisher_out0005.txt'

        fish_files['magnification_bias--alpha_m'] = 'magnification_bias--alpha_m_fisher_out0005.txt'
        fish_files['magnification_bias--beta_m'] = 'magnification_bias--beta_m_fisher_out0005.txt'

if step_size_choice == 'joint_gold_mag':
        fish_files['cosmological_parameters--omega_m'] = 'cosmological_parameters--omega_m_fisher_out0005.txt'
        fish_files['cosmological_parameters--h0'] = 'cosmological_parameters--h0_fisher_out0010.txt'
        fish_files['cosmological_parameters--omega_b'] = 'cosmological_parameters--omega_b_fisher_out0046.txt'
        fish_files['cosmological_parameters--n_s'] = 'cosmological_parameters--n_s_fisher_out0010.txt'
        fish_files['cosmological_parameters--e9A_s'] = 'cosmological_parameters--e9A_s_fisher_out0046.txt'
        fish_files['cosmological_parameters--w'] = 'cosmological_parameters--w_fisher_out0046.txt'
        fish_files['cosmological_parameters--wa'] = 'cosmological_parameters--wa_fisher_out0100.txt'

        fish_files['hod_parameters--lgM1'] = 'hod_parameters--lgM1_fisher_out0005.txt'
        fish_files['hod_parameters--lgl0'] = 'hod_parameters--lgl0_fisher_out0022.txt'
        fish_files['hod_parameters--g1'] = 'hod_parameters--g1_fisher_out0046.txt'
        fish_files['hod_parameters--g2'] = 'hod_parameters--g2_fisher_out0005.txt'
        fish_files['hod_parameters--scatter'] = 'hod_parameters--scatter_fisher_out0100.txt'
        fish_files['hod_parameters--alfa_s'] = 'hod_parameters--alfa_s_fisher_out0005.txt'
        fish_files['hod_parameters--b0'] = 'hod_parameters--b0_fisher_out0005.txt'
        fish_files['hod_parameters--b1'] = 'hod_parameters--b1_fisher_out0005.txt'
        fish_files['hod_parameters--b2'] = 'hod_parameters--b2_fisher_out0005.txt'

        fish_files['nz_e_sample_errors--bias_1'] = 'nz_e_sample_errors--bias_1_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_2'] = 'nz_e_sample_errors--bias_2_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_3'] = 'nz_e_sample_errors--bias_3_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_4'] = 'nz_e_sample_errors--bias_4_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_5'] = 'nz_e_sample_errors--bias_5_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_6'] = 'nz_e_sample_errors--bias_6_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_7'] = 'nz_e_sample_errors--bias_7_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_8'] = 'nz_e_sample_errors--bias_8_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_9'] = 'nz_e_sample_errors--bias_9_fisher_out0005.txt'
        fish_files['nz_e_sample_errors--bias_10'] = 'nz_e_sample_errors--bias_10_fisher_out0046.txt'

        fish_files['ia_parameters--gamma_2h'] = 'ia_parameters--gamma_2h_fisher_out0005.txt'

        fish_files['shear_calibration_parameters--m1'] = 'shear_calibration_parameters--m1_fisher_out0005.txt'
        fish_files['shear_calibration_parameters--m2'] = 'shear_calibration_parameters--m2_fisher_out0005.txt'
        fish_files['shear_calibration_parameters--m3'] = 'shear_calibration_parameters--m3_fisher_out0005.txt'
        fish_files['shear_calibration_parameters--m4'] = 'shear_calibration_parameters--m4_fisher_out0005.txt'
        fish_files['shear_calibration_parameters--m5'] = 'shear_calibration_parameters--m5_fisher_out0005.txt'
        fish_files['shear_calibration_parameters--m6'] = 'shear_calibration_parameters--m6_fisher_out0005.txt'
        fish_files['shear_calibration_parameters--m7'] = 'shear_calibration_parameters--m7_fisher_out0005.txt'
        fish_files['shear_calibration_parameters--m8'] = 'shear_calibration_parameters--m8_fisher_out0005.txt'
        fish_files['shear_calibration_parameters--m9'] = 'shear_calibration_parameters--m9_fisher_out0005.txt'
        fish_files['shear_calibration_parameters--m10'] = 'shear_calibration_parameters--m10_fisher_out0005.txt'

        fish_files['magnification_bias--alpha_m'] = 'magnification_bias--alpha_m_fisher_out0005.txt'
        fish_files['magnification_bias--beta_m'] = 'magnification_bias--beta_m_fisher_out0005.txt'

if len(params)%4 == 0: x = 0 
else: x = 1 

f, axe = plt.subplots(len(params)//4 + x, 4)
ax = axe.flatten()

for i, param in enumerate(params):
        x, L = read_and_normalise_grid(grid_dir, param)

        fisher_std_dev = calculate_fisher_std_dev(fisher_dir, fish_files[param])
        max_like = x[np.where(L==L.max())]
        pdf = norm.pdf(x, loc=max_like, scale=fisher_std_dev)

        if plot_type == 'overlay':
                #x_for_fisher_pdf = np.linspace(x.min(), x.max(), 1000)
                ax[i].plot(x, L, c='C0', label='grid')
                ax[i].plot(x, pdf, c='C1', ls='--', label='fisher')
                ax[i].set_ylabel('P', fontsize=12)

        #pdf = norm.logpdf(x_for_fisher_pdf, loc=max_like, scale=fisher_std_dev)
        #pdf_shifted_to_zero = pdf - max(pdf)
        #ax[i].plot(x_for_fisher_pdf, pdf_shifted_to_zero, c='b', ls='--')

        if plot_type == 'percentage_diff':
                ax[i].axhline(y = 0.0, color = 'C3')
                ax[i].fill_between(x, -0.01, 0.01, alpha=0.2, color='C3')
                ax[i].plot(x, (pdf-L)/L, c='C2')
                ax[i].set_ylabel('(fisherP-gridP)/gridP', fontsize=8)
                ax[i].set_ylim(-0.15, 0.15)

        ax[i].set_xlabel(param, fontsize=12)
        ax[i].xaxis.set_major_locator(plt.MaxNLocator(4))
        ax[i].tick_params(axis ='both', labelsize = 9)

#axe[-1,-1].axis('off')
#f.delaxes(ax.flatten()[26])
#f.delaxes(ax.flatten()[27])
f.set_size_inches(18, 10) 
plt.tight_layout()
#plt.subplots_adjust(wspace=0)
plt.legend()
plt.savefig('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/fisher_step_sizes/plots/fisher_grid_matched_clustering_mag.png')
plt.show()






