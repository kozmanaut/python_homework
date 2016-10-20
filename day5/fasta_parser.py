import os
import matplotlib.pyplot as plt
import sh

class FastaParser(object):
	"""Parser of a fasta file, with path to the file being the only input"""
	def __init__(self, path):
		self.path = path
		if not os.path.exists(self.path):
			raise IOError("File does not exist")

		## Go line by line and create a list with the sequence names (seq_name) and another list of sequences themselves (seq_seq)
		tmp = []
		seq_name = []
		seq_seq = []
		with open(self.path, 'r') as infile:
			for line in infile:
				if line.startswith('>'):
					seq_name.append(''.join(line.strip(">").rstrip('\n')))
					seq_seq.append(''.join(tmp))
					tmp = []
				else:
					tmp.append(''.join(line.strip()))
			else:
				seq_seq.append(''.join(tmp))
		del seq_seq[0]

		## Create a dictionary of sequence name (key) and the sequence (value)
		seq_dict = {name : seq for name, seq in zip(seq_name, seq_seq)}
		
		## Create self object from these lists and dictionaries
		self.seq_name = seq_name
		self.sequence = seq_seq
		self.dict = seq_dict
		self.count = len(self.sequence)

	def __len__(self):
		"""Length of the object: number of sequences"""
		return self.count

	def __getitem__(self, arg):
		"""Allow indexing of the object list and the dictionary"""
		if type(arg) == int:
			return self.sequence[arg]
		elif type(arg) == str:
			return self.dict[arg]

	def extract_length(self, length):
		"""Function to exract sequences that are shorter than desired 'length' - the only input of this function"""
		short = []
		for seq in self.sequence:
			if len(seq) < length:
				short.append(seq)
		return short

	def length_dist(self, path):
		"""A function that creates a histogram figure of the sequence length distribution.
		Input - 'path/to/figure.pdf'	
		"""
		tmp = path.rsplit('/', 1)		#split the path in order to create the needed directories
		directory = tmp[0]				#extract just the parent directories
		sh.mkdir("-p", directory)		#make the needed directories
		
		hist = []						
		for seq in self.sequence:		
			hist.append(len(seq))		#create a list of sequence lengths

		plt.hist(hist, bins= 100, facecolor='grey', alpha=0.75 )
		plt.xlabel('Length of sequence')
		plt.ylabel('Number of sequences')
		plt.title("Histogram showing the distribution of the sequence lengths")
		plt.savefig(path)
