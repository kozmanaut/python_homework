"""
A parser for Raxml. The input is a genotype file produced in ANGSD, that has the genotypes of all individuals present on one line,
separated by a tab. It will then create a fasta file, containing the concatenated sequence for each individual, across all individuals
Raxml will then be run on the fasta file, using the Raxml wrapper in Biopython.
"""

import os
import sh
import matplotlib
import matplotlib.pyplot as plt
try:
	from Bio import Phylo
	from Bio.Phylo.Applications import RaxmlCommandline
except ImportError:
	raise "Biopython is required but it does not seem to be installed. Please install it."

####################################################################
class Genotype(object):
	"""Stores the genotypes of each individual at each position. Path to the genotype file is the only input"""

	def __init__(self, path):
		self.path = path
		if not os.path.exists(self.path):
			raise IOError("File does not exist")

		# Store the genotypes in a list of tuples and calculate the number of individuals in the file
		rows = []
		with open(self.path, 'r') as data:
			for line in data:
				line = line.strip('\n').split('\t')
				rows.append(line[4:-1])
				num_ind =  len(line) - 5

		geno = zip(*rows)
		self.genotypes = geno
		self.num_ind = num_ind

	def single_base(self):
		nc_dict = {
			"AA" : "A", "CC": "C", "TT": "T", "GG": "G"
			"AC": "M", "CA": "M", "AT": "W", "TA": "W", "AG": "R", "GA": "R"
			"CT": "Y", "TC": "Y", "CG": "S", "GC": "S"
			"GT": "K", "TG": "K"
			"NN": "N"
			}



###################################################################
test = Genotype("genotypes.subset.txt")
print test.num_ind
print test.genotypes