PROJECT DESCRIPTION

ANGSD Genotype to Raxml parser

name: raxml_parser

A parser for Raxml. The input is a genotype file produced in ANGSD, that has the genotypes of all individuals present on one line per position, separated by a tab (first 4 columns = Chr, Position, Major allele, Minor allele). It will then create a fasta file, containing the concatenated sequence for each individual, across all individuals. The user can provide an optional argument that determines how the 2 bp genotype is converted to 1bp SNP - 'iupac', 'major' or 'random'. Another optional input argument is a file with individual id's - one id/name per line.

Raxml will then be run on the fasta file. The user can provide the type of substitution model they wish to run (default = 'GTRGAMMA') and an optional name for the run.

This parser works for the latest release of RAxML: v8.2.9. 

Get RAxML from: https://github.com/stamatak/standard-RAxML
Website with manual: http://sco.h-its.org/exelixis/web/software/raxml/index.html

On Uppmax, load RAxMl with:
$ module load bioinfo-tools
$ module load raxml/8.2.4-gcc-mpi

Command line usage:
raxml_parser.py [-h] (optional: [-g geno_method] [-i id_file] [-m subsitutionModel] [-r RAxML_run_name])  'input_file'




