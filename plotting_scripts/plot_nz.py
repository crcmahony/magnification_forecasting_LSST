import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.lines as mlines
import matplotlib.cm as cmx

fig = plt.figure(figsize=(6,4.5))

axset = fig.add_subplot(1,1,1)

#pipeline_output_folder_a = "/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/test_output/"
pipeline_output_folder_a = "/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering_gold/test_output/"
#pipeline_output_folder_b = "/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/test_output_2/"
#pipeline_output_folder_c = "/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/test_output_3/"

def load_nz(name, pipeline_output_folder):
	return np.asarray([np.loadtxt(pipeline_output_folder + name + '/' + 'bin_' + str(i) + '.txt') for i in np.arange(1,11,1)])

sample = "nz_e_sample"

nz = load_nz(sample, pipeline_output_folder_a)
z = np.loadtxt(pipeline_output_folder_a + sample + '/z.txt')


#nz2 = load_nz(sample, pipeline_output_folder_b)
#z2 = np.loadtxt(pipeline_output_folder_b + sample + '/z.txt')

#nz3 = load_nz(sample, pipeline_output_folder_c)
#z3 = np.loadtxt(pipeline_output_folder_c + sample + '/z.txt')

cmap = cmx.get_cmap('viridis')
colour_selection = np.arange(0.1,0.95,0.09)

for i in np.arange(0,10,1):
	axset.plot(z, nz[i], c=cmap(colour_selection[i]), label = 'bin ' + str(i+1))
	#axset.plot(z2, nz2[i], c='b')
	#axset.plot(z3, nz3[i], c='g')

axset.set_xlim(0.0,3.0)
#axset.set_ylim(0.0, 5.0) #for n sample
axset.set_ylim(0.0, 7.5)

axset.set_xlabel('$z$',fontsize=11)
axset.set_ylabel('$n(z)$',fontsize=11)
#plt.title('n(z)')
plt.legend()

plt.savefig('nz_e_sample.pdf')
plt.show()

