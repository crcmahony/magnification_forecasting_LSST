import numpy as np

no_priors = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/shear_clustering/rerun_cacciato/shear_clustering.txt')
with_priors = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/priors/cacciato_rerun/shear_clustering_fishers/shear_clustering_nz_priors_only.txt')

prior = 1/(0.001**2.0)

index = 7
print(no_priors[index,index]+prior)
print(with_priors[index,index])
