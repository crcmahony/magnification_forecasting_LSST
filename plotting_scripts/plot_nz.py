import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.lines as mlines
import matplotlib.cm as cmx

fig = plt.figure(figsize=(6,4.5))

axset = fig.add_subplot(1,1,1)

pipeline_output_folder_a = "/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/test_output/"
#pipeline_output_folder_a = "/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering_gold/test_output/"
#pipeline_output_folder_b = "/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/test_output_2/"
#pipeline_output_folder_c = "/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/test_output_3/"

def load_nz(name, pipeline_output_folder):
	return np.asarray([np.loadtxt(pipeline_output_folder + name + '/' + 'bin_' + str(i) + '.txt') for i in np.arange(1,11,1)])

sample = "nz_n_sample"

nz = load_nz(sample, pipeline_output_folder_a)
z = np.loadtxt(pipeline_output_folder_a + sample + '/z.txt')

#nz2 = load_nz(sample, pipeline_output_folder_b)
#z2 = np.loadtxt(pipeline_output_folder_b + sample + '/z.txt')

#nz3 = load_nz(sample, pipeline_output_folder_c)
#z3 = np.loadtxt(pipeline_output_folder_c + sample + '/z.txt')

#e_bin_edges = [1.049999967217445374e-01, 3.849999904632568359e-01, 5.249999761581420898e-01, 6.549999713897705078e-01, 7.649999856948852539e-01, 8.450000286102294922e-01, 9.350000023841857910e-01, 1.065000057220458984e+00, 1.195000052452087402e+00, 1.375000000000000000e+00, 1.995000004768371582e+00]

n_bin_edges = [1.049999967217445374e-01, 4.749999940395355225e-01, 6.250000000000000000e-01, 7.450000047683715820e-01, 8.349999785423278809e-01, 9.549999833106994629e-01, 1.115000009536743164e+00, 1.254999995231628418e+00, 1.414999961853027344e+00, 1.565000057220458984e+00, 1.995000004768371582e+00]

for i in np.arange(0,11,1):
	axset.axvline(n_bin_edges[i], color='k', ls='--', lw='0.8')

cmap = cmx.get_cmap('inferno')
colour_selection = np.arange(0.1,0.95,0.09)

for i in np.arange(0,10,1):
	axset.plot(z, nz[i], c=cmap(colour_selection[i]), label = 'bin ' + str(i+1))
	#axset.plot(z2, nz2[i], c='b')
	#axset.plot(z3, nz3[i], c='g')

axset.set_xlim(0.0,3.0)
axset.set_ylim(0.0, 5.0) #for n sample
#axset.set_ylim(0.0, 7.5)

axset.set_xlabel('$z$',fontsize=11)
axset.set_ylabel('$n(z)$',fontsize=11)
#plt.title('n(z)')
plt.legend()

#plt.savefig('nz_n_sample_zphot_boundaries.pdf')
plt.show()

