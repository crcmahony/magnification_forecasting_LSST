import numpy as np
import matplotlib.pyplot as plt

pipeline_output_folder = "/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/shear/test_output/"

#alphas = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/faint_end_magnitude_slopes/n_alphas_fit.txt')

def load_Cl(name, bini, binj):
	return np.asarray(np.loadtxt(pipeline_output_folder + name + '/' + 'bin_' + str(bini) + '_' + str(binj) + '.txt'))

ell = np.loadtxt(pipeline_output_folder + 'shear_cl/ell.txt')

### test for Cnn computation
"""
galaxy = load_Cl("galaxy_cl", 2, 1)
magnification_galaxy_ij = load_Cl("magnification_galaxy_cl", 2, 1)
magnification_galaxy_ji = load_Cl("magnification_galaxy_cl", 1, 2)
magnification = load_Cl("magnification_cl", 2, 1)
galaxy_gg = load_Cl("galaxy_cl_gg", 2, 1)
sum_mag = galaxy_gg+magnification+magnification_galaxy_ij+magnification_galaxy_ji
print(galaxy)
print(sum_mag)
print(galaxy-sum_mag)
"""

### test for Cee computation
shear = load_Cl("shear_cl", 2, 1)
intrinsic_shear_ij = load_Cl("shear_cl_gi", 2,1)
intrinsic_shear_ji = load_Cl("shear_cl_gi", 1,2)
intrinsic = load_Cl("shear_cl_ii", 2,1)
shear_gg = load_Cl("shear_cl_gg", 2,1)
sum_intrin = shear_gg+intrinsic_shear_ij+intrinsic_shear_ji+intrinsic 
print(shear-sum_intrin)
#print(np.array_equal(shear, shear_gg+intrinsic_shear_ij+intrinsic_shear_ji+intrinsic))

### test for Cne computation
"""
galaxy_shear = load_Cl("galaxy_shear_cl", 2, 1)
galaxy_shear_gg = load_Cl("galaxy_shear_cl_gg", 2, 1)
galaxy_intrinsic = load_Cl("galaxy_intrinsic_cl", 2, 1)
sum_gal_intrin = galaxy_shear_gg + galaxy_intrinsic
print(galaxy_shear - sum_gal_intrin)
"""


### test m bias working
#galaxy = load_Cl("galaxy_cl", 2, 1)

#galaxy_no_m_bias = load_Cl("galaxy_cl_no_mag_bias", 2, 1)

#print(np.array_equal(galaxy, galaxy_no_m_bias))


#SN_bin_1 = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/SN_tomographic_samples/SN_e/e_SN_bin_0.txt')
#SN_bin_2 = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/SN_tomographic_samples/SN_e/e_SN_bin_1.txt')

#m1 = (1./len(SN_bin_1))*(0.02*np.sum((SN_bin_1**0.3))-0.001*np.sum((SN_bin_1**0.0)))
#m2 = (1./len(SN_bin_2))*(0.02*np.sum((SN_bin_2**0.3))-0.001*np.sum((SN_bin_2**0.0)))

#galaxy_m_bias_test = (1.+m1)*(1.+m2)*galaxy_no_m_bias

#print(np.array_equal(galaxy, galaxy_m_bias_test))

#galaxy_shear = load_Cl("galaxy_shear_cl", 2, 1)

#galaxy_shear_no_m_bias = load_Cl("galaxy_shear_cl_no_bias", 2, 1)
#print(np.array_equal(galaxy_shear, galaxy_shear_no_m_bias))

#galaxy_shear_m_bias_test = (1.+m2)*galaxy_shear_no_m_bias
#print(np.array_equal(galaxy_shear, galaxy_shear_m_bias_test))


### test shear bias working
#shear_no_bias = load_Cl("test_output/shear_cl", 2, 1)
#shear_bias = load_Cl("test_output_2/shear_cl", 2, 1)
#shear_bias_test = shear_no_bias*(1+0.02)*(1+0.5)
#print(shear_bias-shear_bias_test)

#galaxy_shear_no_bias = load_Cl("test_output/galaxy_shear_cl", 2, 1)
#galaxy_shear_bias = load_Cl("test_output_2/galaxy_shear_cl", 2, 1)
#galaxy_shear_bias_test = galaxy_shear_no_bias*(1+0.02)
#print(galaxy_shear_bias-galaxy_shear_bias_test)


#### test shear and m bias for galaxy shear

#galaxy_shear = load_Cl("test_output_2/galaxy_shear_cl", 2, 1)

#galaxy_shear_no_bias = load_Cl("test_output/galaxy_shear_cl", 2, 1)
#print(np.array_equal(galaxy_shear, galaxy_shear_no_bias))

#galaxy_shear_bias_test = (1.+m2)*(1+0.5)*galaxy_shear_no_bias
#print(np.array_equal(galaxy_shear, galaxy_shear_bias_test))






#plt.loglog(ell, abs(galaxy)*ell**2.0, label='galaxy', color='C0')
#plt.loglog(ell, abs(galaxy_no_m_bias)*ell**2.0, label='galaxy no m bias', color='C1')
#plt.loglog(ell, abs(galaxy_m_bias_test)*ell**2.0, label='galaxy m bias', color='C1', ls='--')

#plt.loglog(ell, abs(galaxy_shear)*ell**2.0, label='galaxy', color='C0')
#plt.loglog(ell, abs(galaxy_shear_no_bias)*ell**2.0, label='galaxy no m bias', color='C1')
#plt.loglog(ell, abs(galaxy_shear_bias_test)*ell**2.0, label='galaxy m bias', color='C1', ls='--')

#plt.loglog(ell, abs(magnification_galaxy_ij)*ell**2.0, label='mag_galaxy', color='C1')
#plt.loglog(ell, abs(magnification+magnification_galaxy_ij+magnification_galaxy_ji+galaxy_gg)*ell**2.0, label='Cnn', color='C2', ls='--')

#plt.loglog(ell, abs(shear)*ell**2.0, label='shear', color='C0')
#plt.loglog(ell, abs(intrinsic)*ell**2.0, label='intrinsic', color='C1')
#plt.loglog(ell, abs(intrinsic_shear_ij)*ell**2.0, label='intrinsic_shear', color='C2')
#plt.loglog(ell, abs(shear_gg)*ell**2.0, label='shear_gg', color='C3', ls='--')

"""

plt.loglog(ell, abs(galaxy_shear_bias)*ell**2.0, label='shear', color='C0')
plt.loglog(ell, abs(galaxy_shear_bias_test)*ell**2.0, label='shear test', color='C1', ls='--')
plt.loglog(ell, abs(galaxy_shear_no_bias)*ell**2.0, label='shear no bias', color='C2'
"""
"""
plt.xlim(xmin = 30.0, xmax = 3000.0)
plt.xlabel('$l$',fontsize=16)
plt.ylabel('$l^2|C_l|$',fontsize=16)
plt.yticks([10.0**(-8.0),10.0**(-6.0),10.0**(-4.0),10.0**(-2.0)])
plt.xticks([10.0**(2.0),10.0**(3.0)])
plt.legend()
plt.savefig("test.png")

plt.show()
"""
