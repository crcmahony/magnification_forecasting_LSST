import numpy as np

F = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/output/fisher_clustering_mag_bias.txt')
F_with_priors = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/output/fisher_clustering_nz_priors.txt')
F_mag = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering_mag/output/fisher_clustering_mag.txt')

prior_matrix = np.zeros((len(F),len(F)))

for i in np.arange(16, 26, 1):
	prior_matrix[i,i] = 1/0.003**2.0

print(np.array_equal(F_with_priors, F+prior_matrix))

np.savetxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering_mag/output/fisher_clustering_mag_nz_priors.txt', F_mag+prior_matrix)
