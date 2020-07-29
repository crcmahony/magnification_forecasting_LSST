import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.lines as mlines
from operator import add
import pickle
from astropy.io import fits

def read_clustering_Cl_datavector(Cl_datavector_file):
        with fits.open(Cl_datavector_file) as hdul:
                #print(hdul.info())
                data = hdul['galaxy_cl'].data
                cl_values = data.field('value')
                ell_values = data.field('ang')[0:20]
                cov = hdul['COVMAT'].data
                return cl_values, ell_values, cov


def calculate_1sigma_bounds(Cl_values, cov):
        cov_vec = np.diagonal(cov)
        std_vec = np.sqrt(cov_vec)
        Cl_plus = Cl_values + 2*std_vec
        Cl_minus = Cl_values - 2*std_vec
        return Cl_plus, Cl_minus, std_vec

###################################################
# Create figure and desired subplots

fig = plt.figure(figsize=(10,10))

subplotsrequired = (2,3,4,5,7,8,9,10,13,14,15,19,20,25)

axset = fig.add_subplot(5,5,1)

ax = [fig.add_subplot(5, 5, i, sharex=axset, sharey=axset) for i in subplotsrequired]

for a in ax:
    plt.setp(a.get_xticklabels(), visible = False) #hide tick labels on subplots
    plt.setp(a.get_yticklabels(), visible = False)

fig.subplots_adjust(wspace=0, hspace=0) #set spacing between subplots to zero


#########################################################
# Load in data from cosmosis

Cl_datavector_file = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering_gold/2pt_datavector/clustering_gold_datavector.fits'
#Cl_datavector_file = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/2pt_datavector/clustering_datavector_new_LF.fits'
Cl_values, ell, cov = read_clustering_Cl_datavector(Cl_datavector_file)
Cl_plus, Cl_minus, std_dev = calculate_1sigma_bounds(Cl_values, cov)

"""
##### Cl_test
Cl_datavector_file_t = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering_gold/2pt_datavector/clustering_gold_datavector_test.fits'
Cl_values_t, ell_t, cov_t = read_clustering_Cl_datavector(Cl_datavector_file_t)
print(Cl_values-Cl_values_t)
print(ell-ell_t)
print(cov-cov_t)
"""

mag_Cl_datavector_file = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering_mag_gold/2pt_datavector/clustering_mag_gold_datavector.fits'
#mag_Cl_datavector_file = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering_mag/2pt_datavector/clustering_mag_datavector.fits'
mag_Cl_values, mag_ell, mag_cov = read_clustering_Cl_datavector(mag_Cl_datavector_file)

Cl_datavector_file_5s = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering_gold/2pt_datavector/clustering_gold_datavector_omega_m_5_sigma_plus.fits'
#Cl_datavector_file_5s = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/2pt_datavector/clustering_datavector_new_LF_omega_m_5_sigma_plus.fits'
Cl_values_5s, ell_5s, cov_5s = read_clustering_Cl_datavector(Cl_datavector_file_5s)

w_Cl_datavector_file = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering_gold/2pt_datavector/clustering_gold_datavector_w_5_sigma.fits'
#w_Cl_datavector_file = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/2pt_datavector/clustering_datavector_new_LF_w_5_sigma.fits'
w_Cl_values, w_ell, w_cov = read_clustering_Cl_datavector(w_Cl_datavector_file)

As_Cl_datavector_file = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering_gold/2pt_datavector/clustering_gold_datavector_As_5_sigma.fits'
#As_Cl_datavector_file = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/2pt_datavector/clustering_datavector_new_LF_As_5_sigma.fits'
As_Cl_values, As_ell, As_cov = read_clustering_Cl_datavector(As_Cl_datavector_file)



N_bin_combos = Cl_values.shape[0]/20

Cl_values_binned = np.split(Cl_values, N_bin_combos)
Cl_plus_binned = np.split(Cl_plus, N_bin_combos)
Cl_minus_binned = np.split(Cl_minus, N_bin_combos)
std_dev_binned = np.split(std_dev, N_bin_combos)

mag_Cl_values_binned = np.split(mag_Cl_values, N_bin_combos)
#mag_Cl_plus_binned = np.split(mag_Cl_plus, N_bin_combos)
#mag_Cl_minus_binned = np.split(mag_Cl_minus, N_bin_combos)
#mag_std_dev_binned = np.split(mag_std_dev, N_bin_combos)

Cl_values_binned_5s = np.split(Cl_values_5s, N_bin_combos)

w_Cl_values_binned = np.split(w_Cl_values, N_bin_combos)
As_Cl_values_binned = np.split(As_Cl_values, N_bin_combos)

####################################################
# Make Cosmosis plots

def plot_sigma_discrepancy_axset(index, ell):
        sigma_discrepancy = abs((Cl_values_binned[index] - mag_Cl_values_binned[index]))/std_dev_binned[index]
        sigma_discrepancy_5s = abs((Cl_values_binned[index] - Cl_values_binned_5s[index]))/std_dev_binned[index]
        w_sigma_discrepancy = abs((Cl_values_binned[index] - w_Cl_values_binned[index]))/std_dev_binned[index]
        As_sigma_discrepancy = abs((Cl_values_binned[index] - As_Cl_values_binned[index]))/std_dev_binned[index]
        axset.plot(ell, sigma_discrepancy, color='k', ls='-')
        axset.plot(ell, sigma_discrepancy_5s, color='C0', ls='--')
        axset.plot(ell, w_sigma_discrepancy, color='C1', ls='--')
        axset.plot(ell, As_sigma_discrepancy, color='C2', ls='--')

plot_sigma_discrepancy_axset(0, ell)
#axset.axhline(2, color='k', ls='--')

def plot_sigma_discrepancy(plot_index, index, ell):
        sigma_discrepancy = abs((Cl_values_binned[index] - mag_Cl_values_binned[index]))/std_dev_binned[index]
        sigma_discrepancy_5s = abs((Cl_values_binned[index] - Cl_values_binned_5s[index]))/std_dev_binned[index]
        w_sigma_discrepancy = abs((Cl_values_binned[index] - w_Cl_values_binned[index]))/std_dev_binned[index]
        As_sigma_discrepancy = abs((Cl_values_binned[index] - As_Cl_values_binned[index]))/std_dev_binned[index]
        ax[plot_index].plot(ell, sigma_discrepancy, color='k', ls='-')
        ax[plot_index].plot(ell, sigma_discrepancy_5s, color='C0', ls='--')
        ax[plot_index].plot(ell, w_sigma_discrepancy, color='C1', ls='--')
        ax[plot_index].plot(ell, As_sigma_discrepancy, color='C2', ls='--')

chosen_plots = [2,4,6,8,19,21,23,25,34,36,38,45,47,52]

for counter, value in enumerate(chosen_plots):
	plot_sigma_discrepancy(counter, value, ell)

#for k in np.arange(1,55,1):
#        plot_sigma_discrepancy(k, ell)
        #ax[k-1].axhline(2, color='k', ls='--')

        
####################################################

# Format figure]

axset.set_ylim(ymin = 10**(-3.0))
axset.set_ylabel('$|C_{\ell}-C_{\ell}^{mag}| \ / \ \sigma$',fontsize=14)
axset.set_xlabel('$\ell$',fontsize=14)
axset.set_xscale('log')
axset.set_yscale('log')
axset.set_yticks([10.0**(-2.0),10.0**(0.0),10.0**(2.0)])
#axset.tick_params(labelsize = 12)


#labellist = ['(' + str(j) + ',' + str(i) + ')' for i in np.arange(1,11,1) for j in np.arange(i,11,1)]
labellist = ['(1,1)', '(3,1)', '(5,1)', '(7,1)', '(9,1)', '(3,3)', '(5,3)', '(7,3)', '(9,3)', '(5,5)', '(7,5)', '(9,5)', '(7,7)', '(9,7)', '(9,9)']
#print(labellist)

axset.text(0.05,0.75,labellist[0],horizontalalignment='left',verticalalignment='bottom',transform=axset.transAxes,size=12)

axset.axhspan(2.0, 10.0**2.0, alpha=0.3, color='grey')

for i in range(14):
    ax[i].text(0.05,0.75,labellist[i+1],horizontalalignment='left',verticalalignment='bottom',transform=ax[i].transAxes,size=12)
    ax[i].axhspan(2.0, 10.0**2.0, alpha=0.3, color='grey')


#######################################################
# Add legend

line_5s = mlines.Line2D([],[],color='C0', label = '$\Omega_m$ 5$\sigma$ bias', lw = 1.0, linestyle='--')
w_line = mlines.Line2D([],[],color='C1', label = '$w$ 5$\sigma$ bias', lw = 1.0, linestyle='--')
As_line = mlines.Line2D([],[],color='C2', label = '$A_s$ 5$\sigma$ bias', lw = 1.0, linestyle='--')
line_mag = mlines.Line2D([],[],color='k', label = 'Magnification', lw = 1.0, linestyle='-')
plt.legend(handles=[line_mag, line_5s, As_line, w_line], bbox_to_anchor=(-2.1,2.9),loc='upper right',borderaxespad=0.3,fontsize = 14)

######################################################
# Save/Show

plt.savefig('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/plotting_scripts/thesis_bias_plots/5sigma_bias_compared_to_mag_gold_every_other_sigma_shading.pdf')
plt.show()
