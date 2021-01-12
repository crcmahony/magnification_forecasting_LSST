#import sys
#sys.path.insert(0, '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/without_sigma8_rescale_Aug_18/Fisher_plots')

from Fisher_plot_2_same_axes import fisher_grid
import numpy as np
import matplotlib.pylab as plt
import matplotlib.lines as mlines

########## Options #############################
#F = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/shear/output/fisher_shear.txt')
#F2 = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering_gold/output/fisher_clustering_gold3.txt')

#F = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/shear_clustering/fisher_shear_plus_clustering/shear_clustering_gold.txt')
#F2 = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/shear_clustering/fisher_shear_plus_clustering/shear_clustering_mag_gold.txt')

#F2 = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/priors/shear_clustering_fisher_matrices_with_priors/fisher_shear_clustering_mag_gold_priors.txt')
#F = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/priors/shear_clustering_fisher_matrices_with_priors/fisher_shear_clustering_gold_priors.txt')

F = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/priors/cacciato_rerun/clustering_fishers/clustering_gold_priors.txt')
F2 = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/priors/cacciato_rerun/clustering_fishers/clustering_mag_gold_priors.txt')



covF = np.linalg.inv(F)
covF2 = np.linalg.inv(F2)

filename = 'magnification_paper_plots/clustering_gold_clustering_mag_gold_cos_params.pdf'

plot_cos_params = True
plot_HOD_params = False
plot_nz_params = False
plot_bias_params = False

F_col = 'b' #'r' #'b'
F_line = mlines.Line2D([],[],color=F_col, label = '$C_{nn}$ $\epsilon$-sample', lw = 2.0)
#F_line = mlines.Line2D([],[],color='b', label = '$C_{nn}$ $\epsilon$-sample', lw = 2.0)
#F_line = mlines.Line2D([],[],color='b', label = '$C_{nn}$ $\epsilon$-sample including magnification terms', lw = 2.0)
#F_line = mlines.Line2D([],[],color='b', label = '$C_{nn}$ $\epsilon$-sample', lw = 2.0)

F2_col = 'yellowgreen' #'orange' #'yellowgreen'
F2_line = mlines.Line2D([],[],color=F2_col, label = '$C_{nn}$ $\epsilon$-sample including magnification terms', lw = 2.0) #F2 is blue, largest covariance first
#F2_line = mlines.Line2D([],[], color='maroon', label = '$C_{nn}$ $n$-sample including magnification terms', lw = 2.0) #F2 is blue, largest covariance first
#F2_line = mlines.Line2D([],[],color='midnightblue', label = '$C_{nn}$ $\epsilon$-sample including magnification terms', lw = 2.0)
#F2_line = mlines.Line2D([],[],color='r', label = '$C_{nn}$ $n$-sample including magnification terms', lw = 2.0)
#F2_line = mlines.Line2D([],[],color='r', label = '$C_{nn}$ $\epsilon$-sample no mag bias', lw = 2.0)

########## Code ################################

if plot_cos_params == True and plot_HOD_params == True and plot_nz_params == True and plot_bias_params == True:
        fiducial = {'0000':0.265, '0101':0.71, '0202':0.0448, '0303':0.963, '0404':2.1, '0505':-1.0, '0606':0.0, '0707':11.24, '0808':9.95, '0909':3.18, '1010':0.245, '1111':0.157, '1212':-1.18, '1313':-1.17, '1414':1.53, '1515':-0.217, '1616':0.0, '1717':0.0, '1818':0.0, '1919':0.0, '2020':0.0, '2121':0.0, '2222':0.0, '2323':0.0, '2424':0.0, '2525':0.0, '2626':0.001,'2727':0.0}
        par = ['$\Omega_m$', '$H_0$', '$\Omega_b$', '$n_s$', '$A_s/10^{-9}$', '$w$', '$w_a$', '$log(M_1)$', '$log(L_0)$', '$\gamma_1$', '$gamma_2$', '$\sigma_c$', '$alpha_s$', '$b_0$', '$b_1$', '$b_2$',
        '$\Delta_{z,pos}^1$', '$\Delta_{z,pos}^2$', '$\Delta_{z,pos}^3$', '$\Delta_{z,pos}^4$','$\Delta_{z,pos}^5$', '$\Delta_{z,pos}^6$', '$\Delta_{z,pos}^7$', '$\Delta_{z,pos}^8$','$\Delta_{z,pos}^9$',
        '$\Delta_{z,pos}^{10}$', '$alpha_m$', '$beta_m$']
        fisher_grid(covF, covF2, fiducial, params=par, cov_color=F_col, cov2_color=F2_col)
        plt.legend(handles=[F_line, F2_line], bbox_to_anchor=(0.0,6.0), loc='upper right',borderaxespad=0.3,fontsize = 22)

elif plot_cos_params == True and plot_HOD_params == False and plot_nz_params == False and plot_bias_params == False:
        fiducial = {'0000':0.265, '0101':0.71, '0202':0.0448, '0303':0.963, '0404':2.1, '0505':-1.0, '0606':0.0}
        par = ['$\Omega_m$', '$H_0$', '$\Omega_b$', '$n_s$', '$A_s/10^{-9}$', '$w$', '$w_a$']
        fisher_grid(covF[:7,:7], covF2[:7,:7], fiducial, params=par, cov_color=F_col, cov2_color=F2_col)
        plt.legend(handles=[F_line, F2_line], loc='upper left', bbox_to_anchor=(-5.0,7.0), borderaxespad=0.3,fontsize = 22)
elif plot_cos_params == False and plot_HOD_params == True and plot_nz_params == False and plot_bias_params == False:
        fiducial = {'0000':11.24, '0101':9.95, '0202':3.18, '0303':0.245, '0404':0.157, '0505':-1.18, '0606':-1.17, '0707':1.53, '0808':-0.217}
        par = ['$log(M_1)$', '$log(L_0)$', '$\gamma_1$', '$\gamma_2$', '$\sigma_c$', r'$\alpha_s$', '$b_0$', '$b_1$', '$b_2$']
        fisher_grid(covF[7:16,7:16], covF2[7:16,7:16], fiducial, params=par, cov_color=F_col, cov2_color=F2_col)
        plt.legend(handles=[F_line, F2_line], bbox_to_anchor=(-7.0,9.0), loc='upper left',borderaxespad=0.3,fontsize = 22)
elif plot_cos_params == False and plot_HOD_params == False and plot_nz_params == True and plot_bias_params == False:
        fiducial = {'0000':0.0, '0101':0.0, '0202':0.0, '0303':0.0, '0404':0.0, '0505':0.0, '0606':0.0, '0707':0.0, '0808':0.0, '0909':0.0}
        par = ['$\Delta_{z,pos}^1$', '$\Delta_{z,pos}^2$', '$\Delta_{z,pos}^3$', '$\Delta_{z,pos}^4$','$\Delta_{z,pos}^5$', '$\Delta_{z,pos}^6$',
        '$\Delta_{z,pos}^7$', '$\Delta_{z,pos}^8$','$\Delta_{z,pos}^9$','$\Delta_{z,pos}^{10}$']
        fisher_grid(covF[16:26,16:26], covF2[16:26,16:26], fiducial, params=par, cov_color=F_col, cov2_color=F2_col)
        plt.legend(handles=[F_line, F2_line], bbox_to_anchor=(0.0,7.5), loc='upper right',borderaxespad=0.3,fontsize = 34)
elif plot_cos_params == False and plot_HOD_params == False and plot_nz_params == False and plot_bias_params == True:
        fiducial = {'0000':0.001, '0101':0.0}
        par = ['$alpha_m$', '$beta_m$']
        fisher_grid(covF[26:,26:], covF2[26:,26:], fiducial, params=par, cov_color=F_col, cov2_color=F2_col)
        plt.legend(handles=[F_line, F2_line], bbox_to_anchor=(1.0,1.5), loc='upper right',borderaxespad=0.3,fontsize = 12)

elif plot_cos_params == True and plot_HOD_params == True and plot_nz_params == False and plot_bias_params == False:
        fiducial = {'0000':0.265, '0101':0.71, '0202':0.0448, '0303':0.963, '0404':2.1, '0505':-1.0, '0606':0.0, '0707':11.24, '0808':9.95, '0909':3.18, '1010':0.245, '1111':0.157, '1212':-1.18, '1313':-1.17, '1414':1.53, '1515':-0.217}
        par = ['$\Omega_m$', '$H_0$', '$\Omega_b$', '$n_s$', '$A_s/10^{-9}$', '$w$', '$w_a$', '$log(M_1)$', '$log(L_0)$', '$\gamma_1$', '$gamma_2$', '$\sigma_c$', '$alpha_s$', '$b_0$', '$b_1$', '$b_2$']
        fisher_grid(covF[:16,:16], covF2[:16,:16], fiducial, params=par, cov_color=F_col, cov2_color=F2_col)
        plt.legend(handles=[F_line, F2_line], bbox_to_anchor=(0.0,6.0), loc='upper right',borderaxespad=0.3,fontsize = 22)

else:
        print('This combination does not exist, write some new code :)')

#plt.savefig(filename, bbox_inches='tight')
plt.show()
