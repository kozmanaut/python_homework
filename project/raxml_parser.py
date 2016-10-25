"""
A parser for Raxml. The input is a genotype file produced in ANGSD, that has the genotypes of all individuals present on one line,
separated by a tab. It will then create a fasta file, containing the concatenated sequence for each individual, across all individuals
Raxml will then be run on the fasta file, using the Raxml wrapper in Biopython
"""

import os
import sh
try:
	from Bio import Phylo
	from Bio.Phylo.Applications import RaxmlCommandline
except ImportError:
	raise "Biopython is required but it does not seem to be installed. Please install it."


class Snps(self, path):
	""" """