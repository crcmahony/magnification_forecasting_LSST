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

fig = plt.figure(figsize=(24,24))

subplotsrequired = (2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,23,24,25,26,27,28,29,30,34,35,36,37,38,39,40,45,46,47,48,49,50,56,57,58,59,60,67,68,69,70,78,79,80,89,90,100)

axset = fig.add_subplot(10,10,1)

ax = [fig.add_subplot(10, 10, i, sharex=axset, sharey=axset) for i in subplotsrequired]

for a in ax:
    plt.setp(a.get_xticklabels(), visible = False) #hide tick labels on subplots
    plt.setp(a.get_yticklabels(), visible = False)

fig.subplots_adjust(wspace=0, hspace=0) #set spacing between subplots to zero


#########################################################
# Load in data from cosmosis

#Cl_datavector_file = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering_gold/2pt_datavector/clustering_gold_datavector.fits'
Cl_datavector_file = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/2pt_datavector/clustering_datavector_new_LF.fits'
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

#mag_Cl_datavector_file = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering_mag_gold/2pt_datavector/clustering_mag_gold_datavector.fits'
mag_Cl_datavector_file = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering_mag/2pt_datavector/clustering_mag_datavector.fits'
mag_Cl_values, mag_ell, mag_cov = read_clustering_Cl_datavector(mag_Cl_datavector_file)
#mag_Cl_plus, mag_Cl_minus, mag_std_dev = calculate_1sigma_bounds(mag_Cl_values, mag_cov)

#Cl_datavector_file_5s = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering_gold/2pt_datavector/clustering_gold_datavector_omega_m_5_sigma_plus.fits'
Cl_datavector_file_5s = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/2pt_datavector/clustering_datavector_new_LF_omega_m_5_sigma_plus.fits'
Cl_values_5s, ell_5s, cov_5s = read_clustering_Cl_datavector(Cl_datavector_file_5s)
#Cl_plus, Cl_minus, std_dev = calculate_1sigma_bounds(Cl_values, cov)

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

####################################################
# Make Cosmosis plots

def plot_sigma_discrepancy_axset(index, ell):
        sigma_discrepancy = abs((Cl_values_binned[index] - mag_Cl_values_binned[index]))/std_dev_binned[index]
        sigma_discrepancy_5s = abs((Cl_values_binned[index] - Cl_values_binned_5s[index]))/std_dev_binned[index]
        axset.plot(ell, sigma_discrepancy, marker='o', markersize=2, color='r', ls='')
        axset.plot(ell, sigma_discrepancy_5s, marker='o', markersize=2, color='grey', ls='')

plot_sigma_discrepancy_axset(0, ell)
axset.axhline(2, color='k', ls='--')

def plot_sigma_discrepancy(index, ell):
        sigma_discrepancy = abs((Cl_values_binned[index] - mag_Cl_values_binned[index]))/std_dev_binned[index]
        sigma_discrepancy_5s = abs((Cl_values_binned[index] - Cl_values_binned_5s[index]))/std_dev_binned[index]
        ax[index-1].plot(ell, sigma_discrepancy, marker='o', markersize=2, color='r', ls='')
        ax[index-1].plot(ell, sigma_discrepancy_5s, marker='o', markersize=2, color='grey', ls='')

for k in np.arange(1,55,1):
        plot_sigma_discrepancy(k, ell)
        ax[k-1].axhline(2, color='k', ls='--')

        
####################################################

# Format figure]

#axset.set_ylim(ymin = 10**(-9.0), ymax = 10**(-3.0))
#axset.set_ylim(ymin = -9.0, ymax = -3.0)
axset.set_ylim(ymax = 200)
axset.set_ylabel('$C_{\ell}-C_{\ell}^{mag} \ / \ \sigma$',fontsize=16)
axset.set_xlabel('$\ell$',fontsize=16)
axset.set_xscale('log')
#axset.set_ylabel('$l^2|C_l|$',fontsize=16)
#axset.set_yticks([10.0**(-8.0),10.0**(-6.0),10.0**(-4.0),10.0**(-2.0)])
#axset.set_xticks([10.0**(2.0),10.0**(3.0)])
#axset.tick_params(labelsize = 12)


labellist = ['(' + str(j) + ',' + str(i) + ')' for i in np.arange(1,11,1) for j in np.arange(i,11,1)]
#print(labellist)

axset.text(0.1,0.1,labellist[0],horizontalalignment='left',verticalalignment='bottom',transform=axset.transAxes,size=12)

for i in range(54):
    ax[i].text(0.1,0.1,labellist[i+1],horizontalalignment='left',verticalalignment='bottom',transform=ax[i].transAxes,size=12)


#######################################################
# Add legend

line_5s = mlines.Line2D([],[],color='grey', label = '$\Omega_m$ 5$\sigma$ bias', lw = 1.0, linestyle='-')
line_mag = mlines.Line2D([],[],color='r', label = 'Magnification', lw = 1.0, linestyle='-')
plt.legend(handles=[line_mag, line_5s], bbox_to_anchor=(-3.0,2.5),loc='upper right',borderaxespad=0.3,fontsize = 14)

######################################################
# Save/Show

plt.savefig('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/plotting_scripts/thesis_bias_plots/diff_between_cl_with_without_mag_5_sigma_omega_m_faint_y_lim.png')
plt.show()
