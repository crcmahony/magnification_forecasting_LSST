#!/bin/bash
#PBS -q mediumc7
#PBS -N clustering_gold_fisher
#PBS -l nodes=1:ppn=1:typeb
#PBS -l mem=20gb

source /unix/atlas4/akorn/LSST/cosmosis/cosmosis/setup-my-cosmosis

cosmosis /unix/atlas4/akorn/LSST/cosmosis/cosmosis/modules/euclid_ias/demos/thesis_results/clustering_gold/clustering_gold.ini
