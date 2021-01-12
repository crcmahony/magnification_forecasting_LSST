#import sys
#sys.path.insert(0, '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/without_sigma8_rescale_Aug_18/Fisher_plots')

from Fisher_plot_2_same_axes import fisher_grid
import numpy as np
import matplotlib.pylab as plt
import matplotlib.lines as mlines

########## Options #############################
### without priors
#F2 = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/shear_clustering/rerun_cacciato/shear_clustering_mag.txt')
#F = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/shear_clustering/rerun_cacciato/shear_clustering.txt')

F2 = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/priors/cacciato_rerun/shear_clustering_fishers/shear_clustering_mag.txt')
F = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/priors/cacciato_rerun/shear_clustering_fishers/shear_clustering.txt')

### with priors
#F2 = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/priors/shear_clustering_fisher_matrices_with_priors/fisher_shear_clustering_mag_priors.txt')
#F = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/priors/shear_clustering_fisher_matrices_with_priors/fisher_shear_clustering_priors.txt')

covF = np.linalg.inv(F)
covF2 = np.linalg.inv(F2)

filename = 'magnification_paper_plots/shear_clustering_faint_shear_bias_params_nz_priors_included.pdf'

plot_cos_params = False
plot_HOD_params = False
plot_nz_params = True #includes ia
#plot_ia_param = 
plot_shear_params = False
#plot_nz_clustering_params = True
plot_bias_params = False

F_col = 'r'
F_line = mlines.Line2D([],[],color=F_col, label = '$C_{\epsilon\epsilon}+C_{nn}$ $n$-sample', lw = 2.0)


F2_col = 'orange'
F2_line = mlines.Line2D([],[],color=F2_col, label = '$C_{\epsilon\epsilon}+C_{nn}$ $n$-sample including magnification terms', lw = 2.0) #F2 is blue, largest covariance first


########## Code ################################

if plot_cos_params == True and plot_HOD_params == False and plot_nz_params == False and plot_shear_params == False and plot_bias_params == False:
        fiducial = {'0000':0.265, '0101':0.71, '0202':0.0448, '0303':0.963, '0404':2.1, '0505':-1.0, '0606':0.0}
        par = ['$\Omega_m$', '$H_0$', '$\Omega_b$', '$n_s$', '$A_s/10^{-9}$', '$w$', '$w_a$']
        fisher_grid(covF[:7,:7], covF2[:7,:7], fiducial, params=par, cov_color=F_col, cov2_color=F2_col)
        plt.legend(handles=[F_line, F2_line], loc='upper left', bbox_to_anchor=(-5.0,7.0), borderaxespad=0.3,fontsize = 22)

elif plot_cos_params == False and plot_HOD_params == True and plot_nz_params == False and plot_shear_params == False and plot_bias_params == False:
        fiducial = {'0000':10.98, '0101':9.9, '0202':3.0, '0303':0.429, '0404':0.047, '0505':-0.18, '0606':-0.63, '0707':1.5, '0808':-0.177}
        par = ['$log(M_1)$', '$log(L_0)$', '$\gamma_1$', '$\gamma_2$', '$\sigma_c$', r'$\alpha_s$', '$b_0$', '$b_1$', '$b_2$']
        fisher_grid(covF[7:16,7:16], covF2[7:16,7:16], fiducial, params=par, cov_color=F_col, cov2_color=F2_col)
        plt.legend(handles=[F_line, F2_line], bbox_to_anchor=(-7.0,9.0), loc='upper left',borderaxespad=0.3,fontsize = 22)

elif plot_cos_params == False and plot_HOD_params == False and plot_nz_params == True and plot_shear_params == False and plot_bias_params == False:
        fiducial = {'0000':0.0, '0101':0.0, '0202':0.0, '0303':0.0, '0404':0.0, '0505':0.0, '0606':0.0, '0707':0.0, '0808':0.0, '0909':0.0, '1010':1.0}
        par = ['$\Delta_{z,pos}^1$', '$\Delta_{z,pos}^2$', '$\Delta_{z,pos}^3$', '$\Delta_{z,pos}^4$','$\Delta_{z,pos}^5$', '$\Delta_{z,pos}^6$',
        '$\Delta_{z,pos}^7$', '$\Delta_{z,pos}^8$','$\Delta_{z,pos}^9$','$\Delta_{z,pos}^{10}$', '$A_{IA}$']
        fisher_grid(covF[7:18,7:18], covF2[7:18,7:18], fiducial, params=par, cov_color=F_col, cov2_color=F2_col)
        plt.legend(handles=[F_line, F2_line], bbox_to_anchor=(0.0,7.5), loc='upper right',borderaxespad=0.3,fontsize = 34)

elif plot_cos_params == False and plot_HOD_params == False and plot_nz_params == False and plot_shear_params == True and plot_bias_params == False:
        fiducial = {'0000':0.0, '0101':0.0, '0202':0.0, '0303':0.0, '0404':0.0, '0505':0.0, '0606':0.0, '0707':0.0, '0808':0.0, '0909':0.0}
        par = ['$m^1$', '$m^2$', '$m^3$', '$m^4$', '$m^5$', '$m^6$', '$m^7$', '$m^8$', '$m^9$', '$m^{10}$']
        fisher_grid(covF[18:28,18:28], covF2[18:28,18:28], fiducial, params=par, cov_color=F_col, cov2_color=F2_col)
        plt.legend(handles=[F_line, F2_line], bbox_to_anchor=(-8.0,10.0), loc='upper left',borderaxespad=0.3,fontsize = 22)

elif plot_cos_params == False and plot_HOD_params == False and plot_nz_params == False and plot_shear_params == False and plot_bias_params == True:
        fiducial = {'0000':0.001, '0101':0.0}
        par = [r'$\alpha_m$', r'$\beta_m$']
        fisher_grid(covF[47:,47:], covF2[47:,47:], fiducial, params=par, cov_color=F_col, cov2_color=F2_col)
        plt.legend(handles=[F_line, F2_line], bbox_to_anchor=(0.0,2.0), loc='upper left',borderaxespad=0.3,fontsize = 18)
else:
        print('This combination does not exist, write some new code :)')

#plt.savefig(filename, bbox_inches='tight')
plt.show()
