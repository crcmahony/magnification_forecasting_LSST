from __future__ import print_function
from builtins import range
import numpy as np
from cosmosis.datablock import option_section, names as section_names


def setup(options):
    # only one parameter - filepath
    filename = options[option_section, "filepath"]
    
    output_section = options.get_string(
        option_section, "output_section", default=section_names.galaxy_luminosity_function)

    alphas = np.loadtxt(filename)
    print(alphas)

    return alphas, output_section


def execute(block, config):
    (alphas, output_section) = config

    block[output_section, 'alpha_binned'] = alphas
    return 0


def cleanup(config):
    return 0
