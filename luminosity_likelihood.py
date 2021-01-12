from cosmosis.gaussian_likelihood import GaussianLikelihood
from cosmosis.datablock import names, option_section
import numpy as np
import scipy
 
class luminosity_likelihood(GaussianLikelihood):
 
    def __init__(self, options):
        self.options = options
        self.cov_non_zero = self.load_cov_non_zero()
        self.data_x, self.data_y, self.lum_midpoints = self.build_data()
        self.likelihood_only = options.get_bool('likelihood_only', False)

################################################################
# PULLED FROM GAUSSIAN_LIKELIHOOD.__INIT__
        if self.constant_covariance:
            self.cov = self.build_covariance()
            self.inv_cov = self.build_inverse_covariance()
            if not self.likelihood_only:
                self.chol = np.linalg.cholesky(self.cov)
            include_norm = self.options.get_bool("include_norm", False)
            if include_norm:
                self.log_det_constant = GaussianLikelihood.extract_covariance_log_determinant(self,None)
                print("Including -0.5*|C| normalization in {} likelihood where |C| = {}".format(self.like_name, self.log_det_constant))
            else:
                self.log_det_constant = 0.0
        self.kind = self.options.get_string("kind", "cubic")
        # Allow over-riding where the inputs come from in 
        #the options section
        if options.has_value("x_section"):
            self.x_section = options['x_section']
        if options.has_value("y_section"):
            self.y_section = options['y_section']
        if options.has_value("x_name"):
            self.x_name = options['x_name']
        if options.has_value("y_name"):
            self.y_name = options['y_name']
        if options.has_value("like_name"):
            self.like_name = options['like_name']
################################################################
 
    def load_cov_non_zero(self):
        cov_non_zero_file = self.options.get_string("cov_non_zero_file")
        cov_non_zero = np.loadtxt(cov_non_zero_file, dtype=int)
        return cov_non_zero   

    def build_data(self):
        data_file = self.options.get_string("data_file")
        lum, LF = np.loadtxt(data_file).T
        #print("DATA_x (lum):", lum)
        #print("DATA_y: (LF)", LF)
        n_lum_bins_data = self.options.get_int("n_lum_bins_data")
        return lum[self.cov_non_zero], LF[self.cov_non_zero], lum[:n_lum_bins_data]
 
    def build_covariance(self):
        cov_vector_file = self.options.get_string("cov_vector_file")
        covmat_vector = np.loadtxt(cov_vector_file)
        #print("COVMAT VECTOR: ", covmat_vector)
        #print("COVMAT VECTOR: zeros removed ", covmat_vector[self.cov_non_zero])
        covmat = np.diag(covmat_vector[self.cov_non_zero], k=0)
        return covmat
 
    def extract_theory_points(self, block):
        "Extract relevant theory from block and get theory at data x values"
        theory_x = block[self.x_section, self.x_name]
        theory_y = block[self.y_section, self.y_name]
        #print('theory_x:', theory_x)
        #print('x_new:', self.lum_midpoints)

        n_tomo_bins = self.options.get_int("n_tomo_bins")
        n_lum_bins = len(self.lum_midpoints)
        
        theory_photoz_bin = np.zeros((n_tomo_bins,n_lum_bins))

        for i in np.arange(n_tomo_bins):
                f = scipy.interpolate.interp1d(theory_x, theory_y[i], kind='linear') #self.kind)
                theory_photoz_bin[i] = np.atleast_1d(f(self.lum_midpoints))

        #### save simulated LF
        #sim_L = np.tile(self.lum_midpoints, n_tomo_bins)
        #sim_datavector = np.vstack((sim_L,theory_photoz_bin.flatten()))
        #np.savetxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/luminosity_function_datavectors/simulated_datavector_for_grid/e_sample_fiducial_SDSS_hod_params.txt', sim_datavector.T)
         
        return theory_photoz_bin.flatten()[self.cov_non_zero]
 
setup,execute,cleanup = luminosity_likelihood.build_module()






    

