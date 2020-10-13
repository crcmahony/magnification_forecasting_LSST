import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.lines as mlines

fig = plt.figure(figsize=(7,6))

axset = fig.add_subplot(1,1,1)

pipeline_output_folder = "/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/test_output/"
#pipeline_output_folder_constant = "/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/without_sigma8_rescale_Aug_18/joint_new_catalog/test_output/"

spectrum1 = 'matter_power_nl'
spectrum2 = 'galaxy_power'

k =  np.loadtxt(pipeline_output_folder + spectrum1 + '/k_h.txt')
Pk = np.loadtxt(pipeline_output_folder + spectrum1 + '/p_k.txt')
z = np.loadtxt(pipeline_output_folder + spectrum1 + '/z.txt')
print(z[0])

k2 =  np.loadtxt(pipeline_output_folder + spectrum2 + '/k_h.txt')
Pk2 = np.loadtxt(pipeline_output_folder + spectrum2 + '/p_k.txt')
z2 = np.loadtxt(pipeline_output_folder + spectrum2 + '/z.txt')
print(z[0])

bias = np.loadtxt(pipeline_output_folder + 'galaxy_bias/b.txt')
print(bias[0])
print(bias[0]**2.0)

#kc =  np.loadtxt(pipeline_output_folder_constant + spectrum + '/k_h.txt')
#Pkc = np.loadtxt(pipeline_output_folder_constant + spectrum + '/p_k.txt')
#zc = np.loadtxt(pipeline_output_folder_constant + spectrum + '/z.txt')
#print(zc[0])

axset.loglog(k, bias[0]**2.0*Pk[0], c='C0', lw = 1.0, label='b^2 ' + spectrum1)
axset.loglog(k2, Pk2[0], c='C1', lw = 1.0, label=spectrum2)
#axset.loglog(k, -Pk[0]*2.31*10.0**(-3.0), c='r', lw = 1.0)
#axset.loglog(kc, -Pkc[0], c='b', lw = 1.0, ls = '--')
#axset.loglog(kc,-Pkc[0], c='b', lw = 1.0, ls = '--')




axset.set_ylim(ymin = 10**(0.0), ymax = 10**(5.0))
axset.set_xlim(xmin = 10**(-4.0), xmax = 10**(1.0))
axset.set_xlabel('k',fontsize=16)
axset.set_ylabel('P(k)',fontsize=16)
axset.tick_params(labelsize = 14)

#_line = mlines.Line2D([],[],color='b', label = 'linear alignment')
#red_line = mlines.Line2D([],[],color='r', label = 'halo model/fcen')
plt.legend()
plt.tight_layout()
plt.savefig("/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/plotting_scripts/power_spectra_checks/matter_power_galaxy_power_comparison.png")
plt.show()
