import numpy as np
from chainconsumer import ChainConsumer

data_file = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/luminosity_function_fiducial_values/output/LF_some_values_fixed.txt'
data = np.loadtxt(data_file)

samples = data[:,:-1]

#data2 = np.loadtxt('/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/luminosity_function_fiducial_values/output/LF.txt')
#samples2 = data2[:,:-1]

c = ChainConsumer()
c.add_chain(samples, parameters= ["lgm1", "lgl0", "scatter", "b0"]) #["lgm1", "lgl0", "g1", "g2", "scatter", "alfas", "b0", "b1", "b2"])
#c.add_chain(samples2, parameters= ["lgm1", "lgl0", "g1", "g2", "scatter", "alfas", "b0", "b1", "b2"])
c.configure(kde=[True]) #, shade_alpha=0.1, flip=False)
c.plotter.plot(filename="LF_emcee_some_values_fixed.png", figsize="column")