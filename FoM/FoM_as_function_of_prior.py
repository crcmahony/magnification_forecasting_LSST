import numpy as np
import matplotlib.pyplot as plt


def calculate_FoM_cos_params(fisher_matrix):
	covF = np.linalg.inv(fisher_matrix)
	FoM = (np.linalg.det(covF[:7,:7]))**(-1.0/7.0)
	return FoM

def calculate_FoM_DETF_w_wa(fisher_matrix):
	covF = np.linalg.inv(fisher_matrix)
	FoM = (np.linalg.det(covF[5:7, 5:7]))**(-1.0/2.0)
	return FoM

def add_alpha_bias_prior_to_fisher(alpha_m_sigma, fisher_matrix):
	prior = np.zeros(fisher_matrix.shape)
	prior[-2][-2] = 1.0/alpha_m_sigma**2.0
	return prior + fisher_matrix

def add_beta_bias_prior_to_fisher(beta_m_sigma, fisher_matrix):
	prior = np.zeros(fisher_matrix.shape)
	prior[-1][-1] = 1.0/beta_m_sigma**2.0
	return prior + fisher_matrix

def generate_FoMs(alpha_list, fisher_matrix):
	FoM = {}
	FoM_array = np.zeros(len(alpha_list))
	print(FoM_array.shape)
	for i, value in enumerate(alpha_list):
		fisher_plus_prior = add_alpha_bias_prior_to_fisher(value, fisher_matrix)
		#print(fisher_plus_prior)
		#FoM[value] = calculate_FoM_DETF_w_wa(fisher_plus_prior)
		FoM_array[i] = calculate_FoM_cos_params(fisher_plus_prior)
	return FoM_array

def generate_FoMs_beta(beta_list, fisher_matrix):
	FoM_array = np.zeros(len(beta_list))
	print(FoM_array.shape)
	for i, value in enumerate(beta_list):
		fisher_plus_prior = add_beta_bias_prior_to_fisher(value, fisher_matrix)
		#print(fisher_plus_prior)
		#FoM[value] = calculate_FoM_DETF_w_wa(fisher_plus_prior)
		FoM_array[i] = calculate_FoM_cos_params(fisher_plus_prior)
	return FoM_array

### faint
fisher_faint = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/priors/cacciato_rerun/clustering_fishers/clustering_priors.txt')
fisher_mag_faint = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/priors/cacciato_rerun/clustering_fishers/clustering_mag_priors.txt')

### gold
fisher = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/priors/cacciato_rerun/clustering_fishers/clustering_gold_priors.txt')
fisher_mag = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/priors/cacciato_rerun/clustering_fishers/clustering_mag_gold_priors.txt')

alpha_m = np.logspace(-4.0, -1.0, 40)
#beta_m = np.logspace(-2.0, 2.0, 40)
#print('beta_m: ', beta_m)
#print('alpha_m:', alpha_m)

FoM_arr = generate_FoMs(alpha_m, fisher)
FoM_mag_arr = generate_FoMs(alpha_m, fisher_mag)

FoM_arr_faint = generate_FoMs(alpha_m, fisher_faint)
FoM_mag_arr_faint = generate_FoMs(alpha_m, fisher_mag_faint)

#FoM_arr = generate_FoMs_beta(beta_m, fisher)
#FoM_mag_arr = generate_FoMs_beta(beta_m, fisher_mag)

#FoM_arr_faint = generate_FoMs_beta(beta_m, fisher_faint)
#FoM_mag_arr_faint = generate_FoMs_beta(beta_m, fisher_mag_faint)

print('FoM:', FoM_arr)
print('Fom first and last:', FoM_arr_faint[0], FoM_arr_faint[-1])
print('increase: ', FoM_arr_faint[0]/FoM_arr_faint[-1])

fig = plt.figure(figsize=(6,4.5))
ax = fig.add_subplot(1,1,1)

#ax.semilogx(alpha_m, FoM_arr, color = 'b', label = '$C_{nn}$ $\epsilon$-sample')
#ax.semilogx(alpha_m, FoM_mag_arr, color = 'yellowgreen', label = '$C_{nn}$ $\epsilon$-sample including magnification terms')

ax.semilogx(alpha_m, FoM_arr_faint, color = 'r', label = '$C_{nn}$ $n$-sample')
ax.semilogx(alpha_m, FoM_mag_arr_faint, color = 'orange', label = '$C_{nn}$ $n$-sample including magnification terms')

#ax.semilogx(beta_m, FoM_arr, color = 'b', label = '$C_{\epsilon\epsilon}+C_{nn}$ $\epsilon$-sample')
#ax.semilogx(beta_m, FoM_mag_arr, color = 'yellowgreen', label = '$C_{\epsilon\epsilon}+C_{nn}$ $\epsilon$-sample including magnification terms')

#ax.semilogx(beta_m, FoM_arr_faint, color = 'r', label = '$C_{\epsilon\epsilon}+C_{nn}$ $n$-sample')
#ax.semilogx(beta_m, FoM_mag_arr_faint, color = 'orange', label = '$C_{\epsilon\epsilon}+C_{nn}$ $n$-sample including magnification terms')

#diff = (FoM_mag_arr - FoM_arr)/FoM_arr
#ax.semilogx(alpha_m, diff, color = 'b') 

ax.set_xlabel(r'$\sigma$ of $\alpha_m$ Gaussian prior',fontsize=12)
ax.set_ylabel('FoM Cosmological Parameters',fontsize=12)
#ax.set_ylabel('$(FoM_{mag}-FoM) \ / \ FoM$')

plt.legend(fontsize=11)
plt.tight_layout()
#plt.savefig('thesis_plots/faint_gold_FoM_cosmological_parameters_beta.pdf') #sample_difference_in_FoM.png')
plt.show()
