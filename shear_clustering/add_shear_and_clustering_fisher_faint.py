import numpy as np


#### gold sample

shear = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/shear/output/fisher_shear.txt')
shear_zeros = np.zeros((49,49))

shear_zeros[:37, :37] = shear

np.savetxt('shear_zeros_faint.txt', shear_zeros)



clustering = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering_mag/output/fisher_clustering_mag3.txt')
print(clustering.shape)

clustering_zeros_col = np.zeros((28, 21))
print(clustering_zeros_col.shape)
clustering_columns_added = np.hstack((clustering[:,:16], clustering_zeros_col, clustering[:, 16:]))
print(clustering_columns_added.shape)

clustering_zeros_row = np.zeros((21,49))
print(clustering_zeros_row.shape)
clustering_rows_added = np.vstack((clustering_columns_added[:16,:], clustering_zeros_row, clustering_columns_added[16:,:]))
print(clustering_rows_added.shape)

np.savetxt('clustering_zeros_faint.txt', clustering_rows_added)

shear_clustering_fisher = shear_zeros + clustering_rows_added

np.savetxt('fisher_shear_plus_clustering/shear_clustering_mag.txt', shear_clustering_fisher)


