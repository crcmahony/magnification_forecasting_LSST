import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.lines as mlines

fig = plt.figure(figsize=(7,6))

axset = fig.add_subplot(1,1,1)

pipeline_output_folder = "/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/shear/"
#pipeline_output_folder2 = "/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering_mag/test_output_lin_bias/"
#pipeline_output_folder_constant = "/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/without_sigma8_rescale_Aug_18/joint_new_catalog/test_output/"

"""
spectrum1 = 'matter_galaxy_power'
spectrum2 = 'matter_galaxy_power_1h'
spectrum3 = 'matter_galaxy_power_2h'
spectrum4 = 'matter_power_nl'
"""

spectrum1 = 'test_output/matter_power_nl'
spectrum2 = 'test_output_nz/matter_power_nl'
#spectrum2 = 'matter_intrinsic_power'
#spectrum3 = 'intrinsic_power'

k =  np.loadtxt(pipeline_output_folder + spectrum1 + '/k_h.txt')
Pk = np.loadtxt(pipeline_output_folder + spectrum1 + '/p_k.txt')
z = np.loadtxt(pipeline_output_folder + spectrum1 + '/z.txt')
print(z[50])
print('len(z): ', len(z))

k2 =  np.loadtxt(pipeline_output_folder + spectrum2 + '/k_h.txt')
Pk2 = np.loadtxt(pipeline_output_folder + spectrum2 + '/p_k.txt')
z2 = np.loadtxt(pipeline_output_folder + spectrum2 + '/z.txt')
print(z2[0])

#k3 =  np.loadtxt(pipeline_output_folder + spectrum3 + '/k_h.txt')
#Pk3 = np.loadtxt(pipeline_output_folder + spectrum3 + '/p_k.txt')
#z3 = np.loadtxt(pipeline_output_folder + spectrum3 + '/z.txt')
#print(z3[0])

#k4 =  np.loadtxt(pipeline_output_folder + spectrum4 + '/k_h.txt')
#Pk4 = np.loadtxt(pipeline_output_folder + spectrum4 + '/p_k.txt')
#z4 = np.loadtxt(pipeline_output_folder + spectrum4 + '/z.txt')
#print(z4[0])

#bias = np.loadtxt(pipeline_output_folder + 'galaxy_bias/b.txt')
#print(bias[0])
#print(bias[0]**2.0)

ia_factor = 0.5*0.265*0.01387

axset.loglog(k, Pk[0], c='C0', lw = 1.0, label= spectrum1)
axset.loglog(k2, Pk2[0], c='C1', lw = 1.0, label=spectrum2)
#axset.loglog(k3, Pk3[0], c='C2', lw = 1.0, label= spectrum3, ls='--')
#axset.loglog(k4, bias[0]*Pk4[0], c='C3', lw = 1.0, label='b* ' + spectrum4, ls='--')

#axset.set_ylim(ymin = 10**(0.0), ymax = 10**(5.0))
#axset.set_ylim(ymin = 10**(-4.0), ymax = 10**(5.0))
axset.set_xlim(xmin = 10**(-4.0), xmax = 10**(1.0))
axset.set_xlabel('k',fontsize=16)
axset.set_ylabel('P(k)',fontsize=16)
axset.tick_params(labelsize = 14)

plt.legend()
plt.tight_layout()
#plt.savefig("/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/plotting_scripts/rerun_cacciato/intrinsic_power.png")
plt.show()
