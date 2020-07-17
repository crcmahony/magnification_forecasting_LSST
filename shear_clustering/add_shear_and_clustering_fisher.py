import numpy as np


#### gold sample

shear = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/shear/output/fisher_shear.txt')
shear_zeros = np.zeros((39,39))

shear_zeros[:37, :37] = shear
np.savetxt('shear_zeros.txt', shear_zeros)


clustering_gold = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering_mag_gold/output/fisher_clustering_mag_gold2.txt')
print(clustering_gold.shape)

clustering_zeros_col = np.zeros((28, 11))
print(clustering_zeros_col.shape)
clustering_columns_added = np.hstack((clustering_gold[:,:26], clustering_zeros_col, clustering_gold[:, 26:]))
print(clustering_columns_added.shape)

clustering_zeros_row = np.zeros((11,39))
print(clustering_zeros_row.shape)
clustering_rows_added = np.vstack((clustering_columns_added[:26,:], clustering_zeros_row, clustering_columns_added[26:,:]))
print(clustering_rows_added.shape)

np.savetxt('clustering_zeros.txt', clustering_rows_added)

shear_clustering_fisher = shear_zeros + clustering_rows_added

np.savetxt('fisher_shear_plus_clustering/shear_clustering_mag_gold.txt', shear_clustering_fisher)



