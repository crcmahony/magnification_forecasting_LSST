import numpy as np

def generate_clustering_prior_matrix(sample):
        prior_matrix = np.zeros((28,28))
        
        for i in np.arange(16, 26, 1):
                if sample == 'faint':
                        prior_matrix[i,i] = 1/0.003**2.0
                elif sample == 'gold':
                        prior_matrix[i,i] = 1/0.001**2.0

        return prior_matrix

def generate_shear_clustering_gold_prior_matrix():
        prior_matrix = np.zeros((39,39))
        
        for i in np.arange(16, 26, 1):
                        prior_matrix[i,i] = 1/0.001**2.0

        for i in np.arange(27, 37, 1):
                        prior_matrix[i,i] = 1/0.003**2.0

        return prior_matrix


F_without_priors = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/shear_clustering/fisher_shear_plus_clustering/shear_clustering_mag_gold.txt')
F_type = 'shear_clustering_gold'
sample = 'faint' #required for clustering
filename = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/priors/shear_clustering_fisher_matrices_with_priors/fisher_shear_clustering_mag_gold_priors.txt'

#F_test = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/output/fisher_clustering_nz_priors.txt')

if F_type == 'clustering':
        prior_matrix = generate_clustering_prior_matrix(sample)
        F_with_priors = F_without_priors + prior_matrix

        #print(np.array_equal(F_with_priors, F_test))
        np.savetxt(filename, F_with_priors)

if F_type == 'shear_clustering_gold':
        prior_matrix = generate_shear_clustering_gold_prior_matrix()
        F_with_priors = F_without_priors + prior_matrix
        np.savetxt(filename, F_with_priors)






