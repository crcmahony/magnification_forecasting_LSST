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
                data = hdul['shear_cl'].data #galaxy_cl
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

Cl_datavector_file = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/shear/2pt_datavector/shear_datavector.fits'
#Cl_datavector_file = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/2pt_datavector/clustering_datavector_new_LF.fits'
Cl_values, ell, cov = read_clustering_Cl_datavector(Cl_datavector_file)
Cl_plus, Cl_minus, std_dev = calculate_1sigma_bounds(Cl_values, cov)

print('ell:', ell)

N_bin_combos = Cl_values.shape[0]/20

Cl_values_binned = np.split(Cl_values, N_bin_combos)
Cl_plus_binned = np.split(Cl_plus, N_bin_combos)
Cl_minus_binned = np.split(Cl_minus, N_bin_combos)
std_dev_binned = np.split(std_dev, N_bin_combos)

####################################################
# Make Cosmosis plots



def plot_cl_axset(index, ell):
        axset.plot(ell, abs(Cl_values_binned[index])*ell**2.0, color='k', ls='-')
        #axset.plot(ell, sigma_discrepancy_5s, color='C0', ls='--')
        #axset.plot(ell, w_sigma_discrepancy, color='C1', ls='--')
        #axset.plot(ell, As_sigma_discrepancy, color='C2', ls='--')

plot_cl_axset(0, ell)
#axset.axhline(2, color='k', ls='--')

def plot_sigma_discrepancy(index, ell):
        #sigma_discrepancy = abs((Cl_values_binned[index] - mag_Cl_values_binned[index]))/std_dev_binned[index]
        #sigma_discrepancy_5s = abs((Cl_values_binned[index] - Cl_values_binned_5s[index]))/std_dev_binned[index]
        #w_sigma_discrepancy = abs((Cl_values_binned[index] - w_Cl_values_binned[index]))/std_dev_binned[index]
        #As_sigma_discrepancy = abs((Cl_values_binned[index] - As_Cl_values_binned[index]))/std_dev_binned[index]
        ax[index-1].plot(ell, abs(Cl_values_binned[index])*ell**2.0, color='k', ls='-')
        #ax[index-1].plot(ell, sigma_discrepancy_5s, color='C0', ls='--')
        #ax[index-1].plot(ell, w_sigma_discrepancy, color='C1', ls='--')
        #ax[index-1].plot(ell, As_sigma_discrepancy, color='C2', ls='--')

for k in np.arange(1,55,1):
        plot_sigma_discrepancy(k, ell)
        #ax[k-1].axhline(2, color='k', ls='--')

        
####################################################

# Format figure]

#axset.set_ylim(ymin = 10**(-3.0))
axset.set_ylabel('$l^2|C_{\ell}|$',fontsize=14)
axset.set_xlabel('$\ell$',fontsize=14)
axset.set_xscale('log')
axset.set_yscale('log')
#axset.set_yticks([10.0**(-2.0),10.0**(0.0),10.0**(2.0)])
#axset.tick_params(labelsize = 12)


labellist = ['(' + str(j) + ',' + str(i) + ')' for i in np.arange(1,11,1) for j in np.arange(i,11,1)]
#print(labellist)

axset.text(0.05,0.75,labellist[0],horizontalalignment='left',verticalalignment='bottom',transform=axset.transAxes,size=10)

for i in range(54):
    ax[i].text(0.05,0.75,labellist[i+1],horizontalalignment='left',verticalalignment='bottom',transform=ax[i].transAxes,size=10)


#######################################################
# Add legend

#line_5s = mlines.Line2D([],[],color='C0', label = '$\Omega_m$ 5$\sigma$ bias', lw = 1.0, linestyle='--')
#w_line = mlines.Line2D([],[],color='C1', label = '$w$ 5$\sigma$ bias', lw = 1.0, linestyle='--')
#As_line = mlines.Line2D([],[],color='C2', label = '$A_s$ 5$\sigma$ bias', lw = 1.0, linestyle='--')
#line_mag = mlines.Line2D([],[],color='k', label = 'Magnification', lw = 1.0, linestyle='-')
#plt.legend(handles=[line_mag, line_5s, As_line, w_line], bbox_to_anchor=(-3.0,2.5),loc='upper right',borderaxespad=0.3,fontsize = 14)

######################################################
# Save/Show

plt.savefig('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/plotting_scripts/rerun_cacciato/shear_datavector.png')
plt.show()

