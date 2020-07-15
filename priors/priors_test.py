import numpy as np

no_priors = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering_mag/output/fisher_clustering_mag3.txt')

prior = 1/(0.003**2.0)

with_priors = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/priors/Fisher_matrices_with_priors/fisher_clustering_mag_priors3.txt')


print(no_priors[17,17]+prior)
print(with_priors[17,17])
