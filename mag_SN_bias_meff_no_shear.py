"""

Errors in the number density measurement can lead to a multiplicative factor
scaling the observed number density spectra.

This module scales the measured C_ell to account for that difference.

Constance Mahony 5/12/17 

"""
from cosmosis.datablock import names, option_section
import numpy as np

cal_section = "magnification_bias"

def setup(options):
        """
        options:
                - global multiplicative and additive bias
                - different multiplicative and additive bias in each tomographic bin
                - signal-to-noise (power law) dependent multiplicatice and additive bias in each tomographic bin
        """
        m_signal_to_noise=options.get_bool(option_section,"m_signal_to_noise",True)
        galaxy_shear=options.get_bool(option_section,"galaxy_shear",True)
        SN_filename_structure = options.get_string(option_section, "SN_filename_structure")
        return (m_signal_to_noise, galaxy_shear, SN_filename_structure)


def execute(block, config):

        def SN_bias(alpha, beta, alpha_fid, beta_fid, bin):
                """
                Compute multiplicative bias with power law dependence on the signal-to-noise
                in each tomographic bin.
                Parameters:
                - alpha, beta - varied power law parameters (from datablock)
                - alpha_fid, beta_fid - fixed fiducial alpha and beta parameters
                - bin - tomographic redshift bin
                m_eff = m_step - m_fid 
                (orginally m_eff = m_step but in case where alpha = 0 became unconstraining on beta) 
                """
                SN_name="%d.txt"%(bin-1.0)
                #SN_ratio_array = block.get_double_array_1d(SN_sec,SN_name)
                SN_ratio_array = np.loadtxt(SN_filename_structure + SN_name)
                m_step = (alpha*np.sum(np.power(SN_ratio_array, beta))) / len(SN_ratio_array)
                m_fid =  (alpha_fid*np.sum(np.power(SN_ratio_array, beta_fid))) / len(SN_ratio_array)
                return m_step - m_fid


        (m_signal_to_noise, galaxy_shear, SN_filename_structure) = config

        if not m_signal_to_noise:
                m0=block[cal_section, "m0"]
                                
        if m_signal_to_noise:
                alpha_m_fid = block[cal_section, "alpha_m_fid"]
                beta_m_fid = block[cal_section, "beta_m_fid"]
                alpha_m = block[cal_section, "alpha_m"]
                beta_m = block[cal_section, "beta_m"]

        cl_sec="galaxy_cl"
        n_a=block[cl_sec,"nbin_a"]
        n_b=block[cl_sec,"nbin_b"]
        
        block['galaxy_cl_no_mag_bias', 'ell'] = block[cl_sec, 'ell']

        cl_shear_sec="galaxy_shear_cl"

        #Loop through bin pairs
        for i in range(1,n_a+1):
                for j in range(i,n_b+1):

                        #Get existing C_ell
                        cl_name="bin_%d_%d"%(j,i) #to make sure names are right - this is confusing
                        cl_orig=block.get_double_array_1d(cl_sec,cl_name)
                        block['galaxy_cl_no_mag_bias', cl_name] = block[cl_sec, cl_name]

                        #Compute bias parameter on this pair
                        if m_signal_to_noise:
                                mi = SN_bias(alpha_m, beta_m, alpha_m_fid, beta_m_fid, i)
                                mj = SN_bias(alpha_m, beta_m, alpha_m_fid, beta_m_fid, j)
                                m2 = (1+mi)*(1+mj)
                        else:
                                m2 = (1+m0)**2

                        #Apply bias and save back to block
                        print('m2:', m2)
                        cl_new = m2*cl_orig
                        block.replace_double_array_1d(cl_sec,cl_name,cl_new)

        if galaxy_shear:
                block['galaxy_shear_cl_no_bias', 'ell'] = block[cl_shear_sec, 'ell']
                for i in range(1,n_a+1):
                        for j in range(1,n_b+1): #bin_12 does not equal bin_21 in case of C_ne^{ij} 
                                
                                cl_shear_name="bin_%d_%d"%(i,j)
                                cl_shear_orig=block.get_double_array_1d(cl_shear_sec,cl_shear_name)
                                block['galaxy_shear_cl_no_bias', cl_shear_name] = block[cl_shear_sec, cl_shear_name]

                                #Compute bias parameter on this pair
                                if m_signal_to_noise:
                                        mi = SN_bias(alpha_m, beta_m, alpha_m_fid, beta_m_fid, i) #1st bin is position
                                        m2s = (1+mi)
                                else:
                                        m2s = (1+m0)

                                #Apply bias and save back to block
                                cl_shear_new = m2s*cl_shear_orig
                                block.replace_double_array_1d(cl_shear_sec,cl_shear_name,cl_shear_new)
                                                                        

        return 0

        
