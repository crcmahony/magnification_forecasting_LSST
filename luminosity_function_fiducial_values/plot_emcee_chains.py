import numpy as np
from chainconsumer import ChainConsumer

#mean = [0.0, 4.0]
data_file = '/unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/luminosity_function_fiducial_values/output/LF.txt'
data = np.loadtxt(data_file)

samples = data[:,:-1]

with open(data_file) as f:
    first_line = f.readline()

print(len(first_line[1:].split('\t')))

parameter_list = [value for index, value in enumerate(first_line[1:].split('\t')[:-1])]
print(parameter_list)

c = ChainConsumer()
c.add_chain(samples, parameters= ["lgm1", "lgl0", "g1", "g2", "scatter", "alfas", "b0", "b1", "b2"])
c.configure(kde=[True]) #, shade_alpha=0.1, flip=False)
c.plotter.plot(filename="LF_emcee.png", figsize="column")
