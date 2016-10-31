#!/usr/bin/env python

"""
A parser for Raxml. The input is a genotype file produced in ANGSD, that has the genotypes of all individuals present
on one line per position, separated by a tab (first 4 columns = Chr, Position, Major allele, Minor allele). It will then create
a fasta file, containing the concatenated sequence for each individual, across all individuals. The user can provide an
optional argument that determines how the 2 bp genotype is converted to 1bp SNP - 'iupac', 'major' or 'random' (default = 'major').
Another optional input argument is a file with individual id's - one id/name per line.
Raxml will then be run on the fasta file. The user can provide the type of substitution model they wish to run
(default = 'GTRGAMMA') and an optional name for the run.

This parser works for the latest release of RAxML: v8.2.9.

Get RAxML from: https://github.com/stamatak/standard-RAxML
Website with manual: http://sco.h-its.org/exelixis/web/software/raxml/index.html

On Uppmax:
$ module load bioinfo-tools
$ module load raxml
$ module load biopython

Command line usage:
raxml_parser.py [-h] (optional: [-g geno_method] [-i id_file] [-m subsitutionModel] [-r RAxML_run_name])  'input_file'
"""

import os
import matplotlib
import matplotlib.pyplot as plt
import argparse
import random

try:
	from Bio import Phylo
except ImportError:
	raise "Biopython is required but it does not seem to be installed. Please install it."

########################################################################
#Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("input_file", help = "Path to the genotype file", type = str)

parser.add_argument("-g", "--genotype", help = "A method that takes the 2 base pair genotype and turns it into a single \
	base pair genotype. Options: 'iupac', 'major', 'random'. 'iupac' combines the two genotypes into IUPAC nucleotide code, \
	'major' takes the first (major) base and 'random' picks a random base of the two. Default: 'major'", type = str, default = 'major')
parser.add_argument("-i", "--id_file", help = "An optional input file containing the ID (names) of each individual on a single \
	line", type = str)
parser.add_argument("-m", "--substitutionModel", help = "The type of substitution model to use in the RAxML run. \
	See RAxML help page for all the possible models that can be run. Default: 'GTRGAMMA'", type = str, default = 'GTRGAMMA')
parser.add_argument("-r", "--run_name", help = "An optional name for the RAxML output run", type = str)

args = parser.parse_args()

infile = args.input_file
#infile = "genotypes.subset.txt"

geno_method = args.genotype
#geno_method = 'major'

id_file = args.id_file
#id_file = 'names.txt'
#id_file = None

model = args.substitutionModel
#model = 'GTRGAMMA'

run_name = args.run_name
if run_name == None:
	tmp = infile.rsplit('.', 1)
	run_name = tmp[0] + '.' + geno_method

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
				# remove the whole line (position) in which any genotype is NN, otherwise continue
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
			"AC" : "M", "CA" : "M", "AT" : "W", "TA" : "W",
			"AG" : "R", "GA" : "R", "CT" : "Y", "TC" : "Y",
			"CG" : "S", "GC" : "S", "GT" : "K", "TG" : "K",
			}

		if option == 'iupac':
			single_base = [tuple(nc_dict[x] for x in ind) for ind in self.genotypes]
		elif option == 'major':
			single_base = [tuple(x[0] for x in ind) for ind in self.genotypes]
		elif option == 'random':
			single_base = [tuple(random.choice(x) for x in ind) for ind in self.genotypes]

		self.snps = single_base

class Fasta_builder(object):
	"""
	Takes the 1 bp SNPs from class Geno_Snp, a list of names (given or made automatically) and builds a
	fasta file from these two items
	"""
	def __init__(self, snps):

		# create a list of names
		names = []
		# if no id_file given at command line, create own names
		if id_file == None:
			i = 1
			for ind in range(len(snps)):
				names.append(">Individual" + str(i))
				i += 1
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
		assert len(self.seq) == len(self.names), \
		"Number of sequences is not the same as number of names provided!"

		# Create a fasta list and output it to a file called the same as the input file, but with .fa extension
		self.fasta = [x for y in zip(names, seq) for x in y]
		tmp = infile.rsplit('.', 1)
		title = tmp[0] + '.' + geno_method + '.fa'
		with open(title, 'w') as fasta_file:
			for line in self.fasta:
				print >> fasta_file, line
		self.title = title

class Raxml_commander(object):
	"""
	Create a raxml command to then feed it to the run_raxml method that executes it. Input args: name of input fasta file
	(in raxml = -s) and the substitution model to run (-m). Output file name is the same as the input file, without the last
	extension. Type 'raxmlHPC-AVX -h' in a terminal for more information and help.
	"""
	def __init__(self, in_fasta, model):
		self.raxml_comm_line = "raxmlHPC-AVX -f a -x 12345 -p 12345 -# autoMRE -s " + in_fasta + " -m " + model \
		+ " -n " + run_name

	def run_raxml(self, comm_line):
		"""Execute the raxml command"""
		os.system(comm_line)
###################################################################

#Load data into the Geno_Snp object
data = Geno_Snp(infile)

#Convert 2bp genotype to 1bp genotype using the selected 'geno_method'
data.single_base(geno_method)

#Build a fasta sequence using the above created snp's
seq = Fasta_builder(data.snps)

#Create a raxml command
run = Raxml_commander(seq.title, model)
print run.raxml_comm_line

#Run raxml
run.run_raxml(run.raxml_comm_line)

#Extract the best tree from the raxml run
dir_list = os.listdir("./")
for file in dir_list:
	if "RAxML_bipartitions."+run_name in file:
		tree_file = file
		break

#Import the tree using the Phylo module from biopython and display the tree
tree_handle = open(tree_file, 'r')
tree = Phylo.read(tree_handle, "newick")
Phylo.draw(tree)