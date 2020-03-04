from __future__ import print_function
from builtins import range
from cosmosis.datablock import option_section, names


def setup(options):
    do_shear_shear = options.get_bool(option_section, "shear-shear", True)
    do_position_position=options.get_bool(option_section,"position-position", True)
    do_position_shear_intrinsic = options.get_bool(option_section, "position-shear_intrinsic", True)
    do_position_shear_mag = options.get_bool(option_section, "position-shear_mag", True)
    print()
    print("The add_intrinsic_add_magnification module will combine") 
    if do_shear_shear:
        print("IA terms into the shear-shear spectra.")
    if do_position_position:
        print("magnification terms into the position-position spectra.")
    if do_position_shear_intrinsic:
        print("IA terms into the position-shear spectra.")
    if do_position_shear_mag:
        print("magnification terms into the position-shear spectra.")
    if not do_shear_shear and not do_position_shear_intrinsic and not do_position_shear_mag and not do_position_position:
        print("...actually not into anything. You set shear-shear=F, position-shear=F and position-position=F")
        print("Ths module will not do anything in this configuration")
    print()
    return do_shear_shear, do_position_position, do_position_shear_intrinsic, do_position_shear_mag


def execute(block, config):
    do_shear_shear, do_position_position, do_position_shear_intrinsic, do_position_shear_mag = config

    if do_shear_shear:
        nbin_shear = block[names.shear_cl, 'nbin']
    elif do_position_shear_intrinsic or do_position_shear_mag:
        nbin_shear = block["galaxy_shear_cl", 'nbin_b']
    
    if do_position_position:
        nbin_pos = block[names.galaxy_cl, 'nbin']
    elif do_position_shear_intrinsic or do_position_shear_mag:
        nbin_pos = block["galaxy_shear_cl", 'nbin_a']

    if do_shear_shear:
        # for shear-shear, we're replacing 'shear_cl' (the GG term) with GG+GI+II
        # so in case useful, save the GG term to shear_cl_gg.
        # also check for a b-mode contribution from IAs
        block[names.shear_cl_gg, 'ell'] = block[names.shear_cl, 'ell']
        for i in range(nbin_shear):
            for j in range(i + 1):
                bin_ij = 'bin_{0}_{1}'.format(i + 1, j + 1)
                bin_ji = 'bin_{1}_{0}'.format(i + 1, j + 1)
                block[names.shear_cl_gg, bin_ij] = block[names.shear_cl, bin_ij]
                block[names.shear_cl, bin_ij] += (
                      block[names.shear_cl_ii, bin_ij]  # II
                    + block[names.shear_cl_gi, bin_ij]  # The two GI terms
                    + block[names.shear_cl_gi, bin_ji]
                )

    if do_position_position:
        #for position-position, we're replacing 'galaxy_cl' (the gg term) with gg+gm+mm
        #so in case useful, save the gg term to galaxy_cl_gg
        block["galaxy_cl_gg",'ell']=block[names.galaxy_cl, 'ell']
        for i in range(nbin_pos):
            for j in range(i+1):
                bin_ij = 'bin_{0}_{1}'.format(i + 1, j + 1)
                bin_ji = 'bin_{1}_{0}'.format(i + 1, j + 1)
                block["galaxy_cl_gg", bin_ij]=block[names.galaxy_cl, bin_ij]
                block[names.galaxy_cl, bin_ij] += (
                    block["magnification_cl", bin_ij]  #mm
                    + block["magnification_galaxy_cl", bin_ij]  # The two gm terms
                    + block["magnification_galaxy_cl", bin_ji]
                    )

    if do_position_shear_intrinsic or do_position_shear_mag:
        block["galaxy_shear_cl_gG",'ell']=block["galaxy_shear_cl", 'ell']
        for i in range(nbin_pos):
            for j in range(nbin_shear):
                bin_ij = 'bin_{0}_{1}'.format(i + 1, j + 1)
                block["galaxy_shear_cl_gG", bin_ij]=block["galaxy_shear_cl", bin_ij]
                if do_position_shear_intrinsic:
                    block["galaxy_shear_cl", bin_ij] += block["galaxy_intrinsic_cl", bin_ij]
                if do_position_shear_mag:
                    block["galaxy_shear_cl", bin_ij] += (
                        block["magnification_shear_cl", bin_ij]
                        + block["magnification_intrinsic_cl", bin_ij]  #see Joachimi Bridle 2010 eq(6) for guidance
                        )
                

    return 0
