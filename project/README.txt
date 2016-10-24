PROJECT DESCRIPTION

ANGSD Genotype to Raxml parser

name: raxml_parser

What will it do: Take a genotype file created from ANGSD, clean it (remove any line that has NN), format it into a fasta file that will be used as input for Raxml.
Run Raxml as well? 
Include additional Raxml options?

For names, have another input file with ind names

Input: 	ANGSD genotype file
Output: Phylo tree created from the Raxml .tre file

Class: SNP

attributes: name, length (bp's), number of ind/seq's

Class: Tree

attributes: branch names

