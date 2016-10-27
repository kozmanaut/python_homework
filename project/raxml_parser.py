#!/usr/bin/env python

"""
A parser for Raxml. The input is a genotype file produced in ANGSD, that has the genotypes of all individuals present on one line,
separated by a tab. It will then create a fasta file, containing the concatenated sequence for each individual, across all individuals
Raxml will then be run on the fasta file, using the Raxml wrapper in Biopython.

Get RAxML from: https://github.com/stamatak/standard-RAxML
Website with manual: http://sco.h-its.org/exelixis/web/software/raxml/index.html
On Uppmax, load RAxMl with:
$ module load bioinfo-tools
$ module load raxml/8.2.4-gcc-mpi

Command line usage:
raxml_parser.py [optional: -g -i]  'input_file'

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
#	genotype. Options: 'iupac', 'major', 'random'. 'iupac' combines the two genotypes into IUPAC nucleotide code, \
#	'major' takes the first (major) base and 'random' picks a random base of the two.", type = str, default = 'random')
#parser.add_argument("-i", "--id_file", help = "An optional input file containing the ID (names) of each individual on a single line", type = str)
#
#args = parser.parse_args()
#
#infile = args.input_file
infile = "genotypes.subset.txt"

#geno_method = args.genotype
geno_method = 'major'

#id_file = args.id_file
id_file = "names.txt"

####################################################################
class Geno_Snp(object):
	"""Stores the genotypes of each individual at each position."""

	def __init__(self, path):
		self.path = path
		if not os.path.exists(self.path):
			raise IOError("Input file does not exist")

		# Store the genotypes in a list of tuples and calculate the number of individuals in the file
		rows = []
		with open(self.path, 'r') as data:
			for line in data:
				# remove the whole line (position) in which any genotype is NN, otherwise continue on line 61
				if "NN" in line: continue
				line = line.strip('\n').split('\t')
				rows.append(line[4:-1])
				num_ind =  len(line) - 5
		geno = zip(*rows)
		self.genotypes = geno
		self.num_ind = num_ind

	def single_base(self, option):
		"""Method that takes the 2 bp genotypes and turns it into a 1 bp SNP, depending on the option chosen"""

		# IUPAC nucleotide codes
		nc_dict = {
			"AA" : "A", "CC" : "C", "TT" : "T", "GG" : "G",
			"AC" : "M", "CA" : "M", "AT" : "W", "TA" : "W", "AG" : "R", "GA" : "R",
			"CT" : "Y", "TC" : "Y", "CG" : "S", "GC" : "S",
			"GT" : "K", "TG" : "K",
			}
		if option == 'iupac':
			single_base = [tuple(nc_dict[x] for x in ind) for ind in self.genotypes]
		elif option == 'major':
			single_base = [tuple(x[0] for x in ind) for ind in self.genotypes]
		elif option == 'random':
			single_base = [tuple(random.choice(x) for x in ind) for ind in self.genotypes]

		self.snps = single_base

class Fasta_builder(object):
	"""Takes the 1 bp SNPs from class Geno_Snp, a list of names (given or made automatically) and builds a fasta file from these two items"""
	def __init__(self, snps):

		# create a list of names
		names = []
		# if no id_file given at command line, create own names
		if id_file == None:
			i = 1
			for i in range(len(snps)+1):
				names.append(">Individual" + str(i))
		# raise error if id_file given but the file does not exist
		elif not os.path.exists(id_file):
			raise IOError("Specified id_file does not exist")
		# otherwise, take the id_file and create a list of names
		else:
			with open(id_file, 'r') as ids:
				for line in ids:
					names.append(">"+line.strip('\n'))
		self.names = names

		# join the SNPs from each individual to create a sequence
		seq = ["".join(ind) for ind in snps]
		self.seq = seq

		# make sure lengths of the names list and sequence list are the same
		assert len(self.seq) == len(self.names), "Number of sequences is not the same as number of names provided!"

		# Create a fasta list and output it to a file called the same as the input file, but with .fa extension
		self.fasta = [x for y in zip(names, seq) for x in y]
		tmp = infile.rsplit('.', 1)
		title = tmp[0] + '.' + geno_method + '.fa'
		with open(title, 'w') as fasta_file:
			for line in self.fasta:
				print >> fasta_file, line

class Raxml_runner(object):


###################################################################
data = Geno_Snp(infile)
data.single_base(geno_method)
seq = Fasta_builder(data.snps)
