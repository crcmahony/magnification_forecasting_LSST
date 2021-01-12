#import sys
#sys.path.insert(0, '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/without_sigma8_rescale_Aug_18/Fisher_plots')

from Fisher_plot_emcee import fisher_grid
import numpy as np
import matplotlib.pylab as plt
import matplotlib.lines as mlines
from chainconsumer import ChainConsumer

########## Options #############################
#F = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering/output/fisher_clustering.txt')
F = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering_gold/output/fisher_clustering_gold_cos_params_only.txt')


covF = np.linalg.inv(F)

filename = 'paper_MCMC_fisher_e_sample_comparison.pdf'

MCMC_line = mlines.Line2D([],[],color='yellowgreen', label = 'MCMC', lw = 2.0)
Fish_line = mlines.Line2D([],[],color='b', label = 'Fisher', lw = 2.0) #F2 is blue, largest covariance first


########## Code ################################

### generate fisher plot
fiducial = {'0000':0.265, '0101':0.71, '0202':0.0448, '0303':0.963, '0404':2.1, '0505':-1.0, '0606':0.0}
par = ['$\Omega_m$', '$H_0$', '$\Omega_b$', '$n_s$', '$A_s/10^{-9}$', '$w$', '$w_a$']
plot, axes = fisher_grid(covF[:7,:7], fiducial, params=par)

### add emcee contours

data_file = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering_gold/output/MCMC_clustering_gold.txt'
data = np.loadtxt(data_file)
samples = data[:,:-1]

c = ChainConsumer()
c.add_chain(samples, parameters= ["$\omega_m$", "$H_0$", "$\omega_b$", "$n_s$", "$A_s/10^{-9}$", "$w$", "$w_a$"], walkers=100, color='lg', linewidth=2.0)
c.configure(kde=[True], shade_alpha=0.5) #, flip=False)

geweke_converged = c.diagnostic.geweke()
print(geweke_converged)

c.plotter.plot_contour(axes['ax0001'], "$\omega_m$", "$H_0$")
c.plotter.plot_contour(axes['ax0002'], "$\omega_m$", "$\omega_b$")
c.plotter.plot_contour(axes['ax0003'], "$\omega_m$", "$n_s$")
c.plotter.plot_contour(axes['ax0004'], "$\omega_m$", "$A_s/10^{-9}$")
c.plotter.plot_contour(axes['ax0005'], "$\omega_m$", "$w$")
c.plotter.plot_contour(axes['ax0006'], "$\omega_m$", "$w_a$")

c.plotter.plot_contour(axes['ax0102'], "$H_0$", "$\omega_b$")
c.plotter.plot_contour(axes['ax0103'], "$H_0$", "$n_s$")
c.plotter.plot_contour(axes['ax0104'], "$H_0$", "$A_s/10^{-9}$")
c.plotter.plot_contour(axes['ax0105'], "$H_0$", "$w$")
c.plotter.plot_contour(axes['ax0106'], "$H_0$", "$w_a$")

c.plotter.plot_contour(axes['ax0203'], "$\omega_b$", "$n_s$")
c.plotter.plot_contour(axes['ax0204'], "$\omega_b$", "$A_s/10^{-9}$")
c.plotter.plot_contour(axes['ax0205'], "$\omega_b$", "$w$")
c.plotter.plot_contour(axes['ax0206'], "$\omega_b$", "$w_a$")

c.plotter.plot_contour(axes['ax0304'], "$n_s$", "$A_s/10^{-9}$")
c.plotter.plot_contour(axes['ax0305'], "$n_s$", "$w$")
c.plotter.plot_contour(axes['ax0306'], "$n_s$", "$w_a$")

c.plotter.plot_contour(axes['ax0405'], "$A_s/10^{-9}$", "$w$")
c.plotter.plot_contour(axes['ax0406'], "$A_s/10^{-9}$", "$w_a$")

c.plotter.plot_contour(axes['ax0506'], "$w$", "$w_a$")




print(axes)


plt.legend(handles=[MCMC_line, Fish_line], loc='upper left', bbox_to_anchor=(-5.0,7.0), borderaxespad=0.3,fontsize = 22)


#plt.savefig(filename, bbox_inches='tight')
plt.show()
