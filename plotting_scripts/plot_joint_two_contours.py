from Fisher_plot_2_same_axes import fisher_grid
import numpy as np
import matplotlib.pylab as plt
import matplotlib.lines as mlines

########## Options #############################
F = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering_mag_gold/output/fisher_clustering_mag_gold.txt')
F2 = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/joint_mag/output/fisher_joint_mag.txt')
covF = np.linalg.inv(F)
covF2 = np.linalg.inv(F2)

filename = 'clustering_mag_gold_joint_mag_gold_hod_params.png'

plot_cos_params = False
plot_HOD_params = True
plot_nz_params = False
plot_bias_ia_mag_params = False
plot_bias_shear_params = False

red_line = mlines.Line2D([],[],color='b', label = '$C_{nn}$ $\epsilon$-sample including magnification terms', lw = 2.0)
blue_line = mlines.Line2D([],[],color='b', ls='--', label = '3x2pt $\epsilon$-sample including magnification terms', lw = 2.0) #F2 is blue, largest covariance first

########## Code ################################

if plot_cos_params == True and plot_HOD_params == True and plot_nz_params == True and plot_bias_ia_mag_params == True and plot_bias_shear_params == True:
        fiducial = {'0000':0.265, '0101':0.71, '0202':0.0448, '0303':0.963, '0404':2.1, '0505':-1.0, '0606':0.0, '0707':11.24, '0808':9.95, '0909':3.18, '1010':0.245, '1111':0.157, '1212':-1.18, '1313':-1.17, '1414':1.53, '1515':-0.217, '1616':0.0, '1717':0.0, '1818':0.0, '1919':0.0, '2020':0.0, '2121':0.0, '2222':0.0, '2323':0.0, '2424':0.0, '2525':0.0, '2626':1.0, '2727':0.0, '2828':0.0, '2929':0.0, '3030':0.0, '3131':0.0, '3232':0.0, '3333':0.0, '3434':0.0, '3535':0.0, '3636':0.0, '3737':0.001, '3838':0.0}
        par = ['$\Omega_m$', '$H_0$', '$\Omega_b$', '$n_s$', '$A_s/10^{-9}$', '$w$', '$w_a$', '$log(M_1)$', '$log(L_0)$', '$\gamma_1$', '$gamma_2$', '$\sigma_c$', '$alpha_s$', '$b_0$', '$b_1$', '$b_2$', '$\Delta_{e}^1$', '$\Delta_{e}^2$', '$\Delta_{e}^3$', '$\Delta_{e}^4$', '$\Delta_{e}^5$', '$\Delta_{e}^6$', '$\Delta_{e}^7$', '$\Delta_{e}^8$', '$\Delta_{e}^9$', '$\Delta_{e}^10$', '$a_{2h}$', '$m^1$', '$m^2$', '$m^3$', '$m^4$', '$m^5$', '$m^6$', '$m^7$', '$m^8$', '$m^9$', '$m^10$', r'$\alpha_m$', r'$\beta_m$']
        fisher_grid(covF, covF2, fiducial, params=par)
        plt.legend(handles=[red_line, blue_line], bbox_to_anchor=(0.0,6.0), loc='upper right',borderaxespad=0.3,fontsize = 22)

elif plot_cos_params == True and plot_HOD_params == False and plot_nz_params == False and plot_bias_ia_mag_params == False and plot_bias_shear_params == False:
        fiducial = {'0000':0.265, '0101':0.71, '0202':0.0448, '0303':0.963, '0404':2.1, '0505':-1.0, '0606':0.0}
        par = ['$\Omega_m$', '$H_0$', '$\Omega_b$', '$n_s$', '$A_s/10^{-9}$', '$w$', '$w_a$']
        fisher_grid(covF[:7,:7], covF2[:7,:7], fiducial, params=par)
        plt.legend(handles=[red_line, blue_line], loc='upper left', bbox_to_anchor=(-5.0,7.0), borderaxespad=0.3,fontsize = 22)

elif plot_cos_params == False and plot_HOD_params == True and plot_nz_params == False and plot_bias_ia_mag_params == False and plot_bias_shear_params == False:
        fiducial = {'0000':11.24, '0101':9.95, '0202':3.18, '0303':0.245, '0404':0.157, '0505':-1.18, '0606':-1.17, '0707':1.53, '0808':-0.217}
        par = ['$log(M_1)$', '$log(L_0)$', '$\gamma_1$', '$\gamma_2$', '$\sigma_c$', r'$\alpha_s$', '$b_0$', '$b_1$', '$b_2$']
        fisher_grid(covF[7:16,7:16], covF2[7:16,7:16], fiducial, params=par)
        plt.legend(handles=[red_line, blue_line], bbox_to_anchor=(-7.0,9.0), loc='upper left',borderaxespad=0.3,fontsize = 22)

elif plot_cos_params == False and plot_HOD_params == False and plot_nz_params == True and plot_bias_ia_mag_params == False and plot_bias_shear_params == False:
        fiducial = {'0000':0.0, '0101':0.0, '0202':0.0, '0303':0.0, '0404':0.0, '0505':0.0, '0606':0.0, '0707':0.0, '0808':0.0, '0909':0.0}
        par = ['$\Delta_{e}^1$', '$\Delta_{e}^2$', '$\Delta_{e}^3$', '$\Delta_{e}^4$', '$\Delta_{e}^5$', '$\Delta_{e}^6$', '$\Delta_{e}^7$', '$\Delta_{e}^8$', '$\Delta_{e}^9$', '$\Delta_{e}^{10}$']
        fisher_grid(covF[16:26,16:26], covF2[16:26,16:26], fiducial, params=par)
        plt.legend(handles=[red_line, blue_line], bbox_to_anchor=(0.0,7.5), loc='upper left',borderaxespad=0.3,fontsize = 22)

elif plot_cos_params == False and plot_HOD_params == False and plot_nz_params == False and plot_bias_ia_mag_params == True and plot_bias_shear_params == False:
        fiducial = {'0000':1.0, '0101':0.001, '0202':0.0}
        par = ['$a_{2h}$',r'$\alpha_m$', r'$\beta_m$']
        fisher_grid(covF[:,[26,37,38]][[26,37,38]], covF2[:,[26,37,38]][[26,37,38]], fiducial, params=par)
        plt.legend(handles=[red_line, blue_line], bbox_to_anchor=(1.0,1.5), loc='upper right',borderaxespad=0.3,fontsize = 22)

elif plot_cos_params == False and plot_HOD_params == False and plot_nz_params == False and plot_bias_ia_mag_params == False and plot_bias_shear_params == True:
        fiducial = {'0000':0.0, '0101':0.0, '0202':0.0, '0303':0.0, '0404':0.0, '0505':0.0, '0606':0.0, '0707':0.0, '0808':0.0, '0909':0.0}
        par = ['$m^1$', '$m^2$', '$m^3$', '$m^4$', '$m^5$', '$m^6$', '$m^7$', '$m^8$', '$m^9$', '$m^10$']
        fisher_grid(covF[27:37,27:37], covF2[27:37,27:37], fiducial, params=par)
        plt.legend(handles=[red_line, blue_line], bbox_to_anchor=(0.0,7.5), loc='upper right',borderaxespad=0.3,fontsize = 22)
else:
        'This combination does not exist, write some new code :)'




plt.savefig(filename, bbox_inches='tight')
plt.show()
