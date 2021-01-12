import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.lines as mlines
from operator import add
import pickle

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

pipeline_output_folder = "/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/shear/test_output/"

def load_Cl(name):
	return np.asarray([np.loadtxt(pipeline_output_folder + name + '/' + 'bin_' + str(j) + '_' + str(i) + '.txt') for i in np.arange(1,11,1) for j in np.arange(i,11,1)])

bin_list = ['bin_' + str(j) + '_' + str(i) for i in np.arange(1,11,1) for j in np.arange(i,11,1)]

x = np.loadtxt(pipeline_output_folder + 'shear_cl/ell.txt')

shear = load_Cl("shear_cl_gg")
intrinsic_shear = load_Cl("shear_cl_gi")
intrinsic = load_Cl("shear_cl_ii")
combined = load_Cl("shear_cl")

#galaxy = load_Cl("galaxy_cl_gg")
#magnification_galaxy_ij = load_Cl("magnification_galaxy_cl")
#magnification = load_Cl("magnification_cl")
#combined = load_Cl("galaxy_cl")

#galaxy_shear = load_Cl("galaxy_shear_cl") #_gg")
#galaxy_intrinsic =load_Cl("galaxy_intrinsic_cl")
#magnification_shear = load_Cl("magnification_shear_cl")
#magnification_intrinsic = load_Cl("magnification_intrinsic_cl")


####################################################
# Make Cosmosis plots

def plot_Cl_axset(Cl, x, colour, linewidth, linestyle):
	lsquared_Cl = [abs(i)*j**2.0 for i,j in zip(Cl[0],x)]
	axset.loglog(x, lsquared_Cl, colour, lw=linewidth, linestyle=linestyle)

plot_Cl_axset(combined, x, 'C3', 1.0, '-')
plot_Cl_axset(shear, x, 'C0', 1.0, '-')
plot_Cl_axset(intrinsic_shear, x, 'C1', 1.0, '--')
plot_Cl_axset(intrinsic, x, 'C2', 1.0, '-.')

#plot_Cl_axset(galaxy, x, 'C0', 1.0, '-')
#plot_Cl_axset(magnification_galaxy_ij, x, 'C1', 1.0, '-')
#plot_Cl_axset(magnification, x, 'C2', 1.0, '-')
#plot_Cl_axset(combined, x, 'C3', 1.0, '-')

#plot_Cl_axset(galaxy_shear, x, 'C4', 1.0, '-')
#plot_Cl_axset(galaxy_intrinsic, x, 'C5', 1.0, '--')
#plot_Cl_axset(magnification_shear, x, 'C8', 1.0, '-')
#plot_Cl_axset(magnification_intrinsic, x, 'C9', 1.0, '-')


def plot_Cl(Cl, x, k, colour, linewidth, linestyle):
	lsquared_Cl = [abs(i)*j**2.0 for i,j in zip(Cl[k+1],x)]
	ax[k].loglog(x, lsquared_Cl, colour, lw=linewidth, linestyle=linestyle)

for k in range(54):
	plot_Cl(combined, x, k, 'C3', 1.0, '-')
	plot_Cl(shear, x, k, 'C0', 1.0, '-')
	plot_Cl(intrinsic_shear, x, k, 'C1', 1.0, '--')
	plot_Cl(intrinsic, x, k, 'C2', 1.0, '-.')

	
	#plot_Cl(galaxy, x, k, 'C0', 1.0, '-')
	#plot_Cl(magnification_galaxy_ij, x, k, 'C1', 1.0, '-')
	#plot_Cl(magnification, x, k, 'C2', 1.0, '-')
	#plot_Cl(combined, x, k, 'C3', 1.0, '-')

	#plot_Cl(galaxy_shear, x, k, 'C4', 1.0, '-')
	#plot_Cl(galaxy_intrinsic, x, k, 'C5', 1.0, '--')
	#plot_Cl(magnification_shear, x, k, 'C8', 1.0, '-')
	#plot_Cl(magnification_intrinsic, x, k, 'C9', 1.0, '-')
	

####################################################

# Format figure

#axset.set_ylim(ymin = 10**(-9.0), ymax = 10**(-4.0))
axset.set_xlim(xmin = 30.0, xmax = 3000.0)
axset.set_xlabel('$l$',fontsize=16)
axset.set_ylabel('$l^2|C_l|$',fontsize=16)
axset.set_yticks([10.0**(-8.0),10.0**(-6.0),10.0**(-4.0),10.0**(-2.0)])
axset.set_xticks([10.0**(2.0),10.0**(3.0)])
axset.tick_params(labelsize = 12)

labellist = ['(' + str(j) + ',' + str(i) + ')' for i in np.arange(1,11,1) for j in np.arange(i,11,1)]
print(labellist)

axset.text(0.1,0.1,labellist[0],horizontalalignment='left',verticalalignment='bottom',transform=axset.transAxes,size=12)

for i in range(54):
    ax[i].text(0.1,0.1,labellist[i+1],horizontalalignment='left',verticalalignment='bottom',transform=ax[i].transAxes,size=12)


#######################################################
# Add legend

shear_line = mlines.Line2D([],[],color='C0', label = '$C_{GG}$', lw = 1.0, linestyle='--')
intrinsic_shear_line = mlines.Line2D([],[],color='C1', label = '$C_{IG}$', lw = 1.0, linestyle='--')
intrinsic_line = mlines.Line2D([],[],color='C2', label = '$C_{II}$', lw = 1.0, linestyle='--')
combined_line = mlines.Line2D([],[],color='C3', label = '$C_{nn}$', lw = 1.0, linestyle='-')

#galaxy_line = mlines.Line2D([],[],color='C0', label = '$C_{gg}$', lw = 1.0, linestyle='-')
#magnification_galaxy_line = mlines.Line2D([],[],color='C1', label = '$C_{mg}$', lw = 1.0, linestyle='-')
#magnification_line = mlines.Line2D([],[],color='C2', label = '$C_{mm}$', lw = 1.0, linestyle='-')
#combined_line = mlines.Line2D([],[],color='C3', label = '$C_{nn}$', lw = 1.0, linestyle='-')

#galaxy_shear_line = mlines.Line2D([],[],color='C4', label = '$C_{gG}$', lw = 1.0, linestyle='-')
#galaxy_intrinsic_line = mlines.Line2D([],[],color='C5', label = '$C_{gI}$', lw = 1.0, linestyle='--')
#magnification_shear_line = mlines.Line2D([],[],color='C8', label = '$C_{mG}$', lw = 1.0, linestyle='--')
#magnification_intrinsic_line = mlines.Line2D([],[],color='C9', label = '$C_{mI}$', lw = 1.0, linestyle='--')

#plt.legend(handles=[shear_line, intrinsic_shear_line, intrinsic_line, galaxy_line, magnification_galaxy_line, magnification_line, galaxy_shear_line, galaxy_intrinsic_line, magnification_shear_line, magnification_intrinsic_line], bbox_to_anchor=(-3.0,2.5),loc='upper right',borderaxespad=0.3,fontsize = 14)

#plt.legend(handles=[galaxy_line, magnification_galaxy_line, magnification_line, combined_line], bbox_to_anchor=(-3.0,2.5),loc='upper right',borderaxespad=0.3,fontsize = 14)
plt.legend(handles=[shear_line, intrinsic_shear_line, intrinsic_line, combined_line], bbox_to_anchor=(-3.0,2.5),loc='upper right',borderaxespad=0.3,fontsize = 14)

######################################################
# Save/Show

plt.savefig('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/plotting_scripts/rerun_cacciato/shear_cls.png')
plt.show()
