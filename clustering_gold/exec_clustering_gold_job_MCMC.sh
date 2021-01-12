#!/bin/bash
#PBS -q longc7
#PBS -N clustering_gold_MCMC
#PBS -l nodes=1:ppn=24:typeb
#PBS -l mem=20gb

source /unix/atlas4/akorn/LSST/cosmosis/cosmosis/setup-my-cosmosis

mpirun -n 24 cosmosis --mpi /unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering_gold/clustering_gold_MCMC.ini
