#!/usr/bin/env python

"""
A parser for Raxml. The input is a genotype file produced in ANGSD, that has the genotypes of all individuals present on one line,
separated by a tab. It will then create a fasta file, containing the concatenated sequence for each individual, across all individuals
Raxml will then be run on the fasta file, using the Raxml wrapper in Biopython.
Command line usage:
raxml_parser.py [optional: -g]  'input_file'

"""

import os
import sh
import matplotlib
import matplotlib.pyplot as plt
import argparse
import random

try:
	from Bio import Phylo
	from Bio.Phylo.Applications import RaxmlCommandline
except ImportError:
	raise "Biopython is required but it does not seem to be installed. Please install it."

####################################################################
"""Parse arguments """
#parser = argparse.ArgumentParser()
#parser.add_argument("input_file", help = "Path to the genotype file", type = str)
#
#parser.add_argument("-g", "--genotype", help = "A method that takes the 2 basepair genotype and turns it into a single base pair \
#	genotype. Options: 'concat', 'major', 'random'. 'concat' combines the two genotypes into IUPAC nucleotide code, \
#	'major' takes the first (major) base and 'random' picks a random base of the two.", type = str, default = 'random')
#
#args = parser.parse_args()
#
#infile = args.input_file
infile = "genotypes.subset.txt"

#geno_method = args.genotype
geno_method = 'major'

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
				if "NN" in line: continue 	# remove a line (position) in which any genotype is NN
				line = line.strip('\n').split('\t')
				rows.append(line[4:-1])
				num_ind =  len(line) - 5
		geno = zip(*rows)
		self.genotypes = geno
		self.num_ind = num_ind

	# Method that takes the 2 base genotypes and turns it into a single base genotype, depending on the option chosen
	def single_base(self, option):
		nc_dict = {
			"AA" : "A", "CC" : "C", "TT" : "T", "GG" : "G",
			"AC" : "M", "CA" : "M", "AT" : "W", "TA" : "W", "AG" : "R", "GA" : "R",
			"CT" : "Y", "TC" : "Y", "CG" : "S", "GC" : "S",
			"GT" : "K", "TG" : "K",
			}		# IUPAC nucleotide codes

		if option == 'concat':
			single_base = [tuple(nc_dict[x] for x in ind) for ind in self.genotypes]
		elif option == 'major':
			single_base = [tuple(x[0] for x in ind) for ind in self.genotypes]
		elif option == 'random':
			single_base = [tuple(random.choice(x) for x in ind) for ind in self.genotypes]
		self.snps = single_base

class Alignment
###################################################################
test = Genotype(infile)
#print test.num_ind
#print test.genotypes


nc_dict = {
		"AA" : "A", "CC" : "C", "TT" : "T", "GG" : "G",
		"AC" : "M", "CA" : "M", "AT" : "W", "TA" : "W", "AG" : "R", "GA" : "R",
		"CT" : "Y", "TC" : "Y", "CG" : "S", "GC" : "S",
		"GT" : "K", "TG" : "K",
		"NN" : "N"
		}

sin_bas = [tuple(nc_dict[x] for x in ind) for ind in test.genotypes]

sin_bas2 = [tuple(x[0] for x in ind) for ind in test.genotypes]

sin_bas3 = [tuple(random.choice(x) for x in ind) for ind in test.genotypes]

#print sin_bas
#print sin_bas2
#print sin_bas3

test.single_base(geno_method)