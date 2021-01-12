import numpy as np

def calculate_FoM_cos_params(path_to_fisher):
	F = np.loadtxt(path_to_fisher)
	covF = np.linalg.inv(F)
	FoM = (np.linalg.det(covF[:7,:7]))**(-1.0/7.0)
	return FoM

def calculate_FoM_DETF_w_wa(path_to_fisher):
	F = np.loadtxt(path_to_fisher)
	covF = np.linalg.inv(F)
	FoM = (np.linalg.det(covF[5:7, 5:7]))**(-1.0/2.0)
	return FoM

fish_file = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/priors/cacciato_rerun/clustering_fishers/clustering_mag_priors.txt'

cos_params_FoM = calculate_FoM_cos_params(fish_file)
DETF_FoM = calculate_FoM_DETF_w_wa(fish_file)

print('cos FoM:', cos_params_FoM)
print('DETF FoM:', DETF_FoM)
