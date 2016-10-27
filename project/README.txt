PROJECT DESCRIPTION

ANGSD Genotype to Raxml parser

name: raxml_parser

What will it do: Take a genotype file created from ANGSD, clean it (remove any line that has NN), take an input argument to decide how to turn a 2 basepair genotype into 1 basebair genotype, format it into a fasta sequence file that will be used as input for Raxml. Use a Raxml wrapper to run Raxml locally. 

For names, have another input file with ind names

Input: 	ANGSD genotype file
Output: Phylo tree created from the Raxml .tre file


Class Genotype()
	SNP.single_2b_genotypes
		Take each genotype (AA) of each individual and store it
	SNP.create_1b_genotypes()
		a method that will take an input argument and convert the genotype into: i) IUPAC nt code using a dictionary or ii) take the major allele or iii) take a random allele
Class Alignment()
	Alignemnt.sequences
		A sequence of each individuals
	Alignment.add_SNP
		a method that uses an object of class SNP to poopulate a sequences with one more position
	alignment.indnames()
		method that uses an input file to create names for fasta file
	Alingment_check_same_number_bases
		method that checks that each individuals has the same number of bases
	alignment.to_fasta("filepath")
		method that creates a fasta file with all the individuals


Class: Raxml_Runner 
	- Use the Raxml wrapper available in BioPython

attributes: Raxml path,  (options to run Raxml?)
methods: run Raxml 


Class: Tree
	- use the Phylo module from Biopython
attributes: self, path to .tre file
methods: draw tree, (convert between formats?)



