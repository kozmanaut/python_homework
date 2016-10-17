""" Class Questions"""

class Person(object):
	""" A class that describes a person"""

	def __init__(self, name, age, birth_place, nationality, gender):
		""" Some simple attributes of a person"""
		
		self.name = name
		self.age = age
		self.birth_place = birth_place
		self.nationality = nationality
		self.gender = gender

	def introduction(self):
		""" A simple presentation of a person"""
		
		print "Hello, my name is", self.name + ".", "I am", self.age, "years old and I come from", self.nationality + "."

bob = Person(name='Bob', age = 71, birth_place = "Nine Mile", nationality = "Jamaica", gender ='Male')

bob.introduction()





class Sample(object):
	"""A class that describes a sample"""

	def __init__(self, species, lat, lon, sample_type, date):
		"""Atrributes of the sample"""
		
		self.species = species
		self.lat = lat
		self.lon = lon
		self.sample_type = sample_type
		self.date = date

	def overview(self):
		"""A simple method that prints the information about the sample"""

		print "This sample is", self.species, "[" + self.sample_type +"]", "collected on", self.date, "at", str(self.lat) + ":" + str(self.lon), "(lat:lon)"

sample1 = Sample(species="Lagopus lagopus lagopus", lat = 59.849651, lon = 17.623562, sample_type = 'feather', date = "01-02-2016")
sample2 = Sample(species="Lagopus muta", lat = 60.845651, lon = 17.613562, sample_type = 'blood', date = "09-11-2009")
sample3 = Sample(species="Tetrao tetrix", lat = 61.819651, lon = 17.123562, sample_type = 'wing', date = "15-05-2011")

for i in [sample1, sample2, sample3]:
	i.overview()

""" 
class 			= class Sample(object):
attributes 		= def __init__(self, species, lat, lon, sample_type, date):
					self.species = species
					self.lat = lat
					self.lon = lon
					self.sample_type = sample_type
					self.date = date
method 			= def overview(self):
instance 		= sample1, sample2, sample3
instantiation 	= sample1 = Sample(species="Lagopus lagopus ...)
"""

class Old(Sample):
	def __init__(self, date="Before 1980"):
		self.date = date

	def overview(self):
		print "This sample is old. Dont use it!"

sample4 = Old()

sample4.overview()





"""Pretty up the python code """

"""A script that takes a DNA sequence and produces a useful summary of content"""

a = "ATGTATCTAGATCGATCGACGATCGATCGGATCGATCGGGATCGATCGAGAGAGCTAGCTTAGAGAGAGCTAGAGCTAGCATCGATTATCGATCG"

A_count = a.count("A")		# count all the "A" in the seq 'a'
T_count = a.count("T")		# count all the "T" in the seq 'a'
G_count = a.count("G")		# count all the "G" in the seq 'a'
C_count = a.count("C")		# count all the "C" in the seq 'a'

print "AG content:", float(A_count+G_count)/len(a)		# print AG content
print "The lenght of the whole sequence:", len(a)		# lenght of the whole seq

pCTA=a.count("CTA")										# count number of CTA codons
pCTG=a.count("CTG")										# no. CTG codons
pCTC=a.count("CTC")										# no. CTC codons
pCTT=a.count("CTT")										# no. CTT codons

if pCTA>0: print "Found", pCTA, "'CTA' codon(s)"			# print the number of CTA codons, if any
if pCTG>0: print "Found", pCTG, "'CTG' codon(s)"			# print the number of CTG codons, if any
if pCTC>0: print "Found", pCTC, "'CTC' codon(s)"			# print the number of CTC codons, if any
if pCTT>0: print "Found", pCTT, "'CTT' codon(s)"			# print the number of CTT codons, if any

"""Ask user to input codon of their choice and see if it occurs in the sequence """
codon = raw_input("Enter the desired codon (valid bases are A, C, G and T): ")
codon = codon.upper()

if len(codon) != 3: print "Codon must have 3 bases!"
else:	
	p_codon = a.count(codon)
	print "Your desired codon appears", p_codon, "time(s) in the sequence"





""" Functions excercises"""

int_list = [1,11,111,22,33,44,123, 231]		# list of intigers

def coun_odd(lst):			# function to count the number of odd numbers
	odd_nums = 0
	
	for num in lst:
		if num % 2 == 1:
			odd_nums += 1

	return odd_nums

print "Count of odd numbers in the list: ", coun_odd(int_list)

def get_even(lst): 		# function to count the number of even numbers
	even_nums = 0

	for num in lst:
		if num % 2 == 0:
			even_nums += 1

	return even_nums

print "Count of even numbers in the list: ", get_even(int_list)

def arith_mean(lst):		# function to calculate the arithmetic mean of numbers in list

	return sum(lst)/float(len(lst))

print "Artithmetic mean of the list: ", arith_mean(int_list)

def median(lst):			# function to return the median of the numbers in the list
	lst = sorted(lst)
	middle = (len(lst)-1) / 2

	if len(lst) % 2 == 1:
		return lst[middle]
	else:
		return (lst[middle] + lst[middle +1 ]) / 2.0

print "Median of the list: ", median(int_list)


"""same thing using numpy ... odd and even numbers count is easier with the above code"""
import numpy as np

def numpy_arith_mean(lst): 		# calc. arithmetic mean
	return np.mean(lst)

print "Using numpy, artithmetic mean of the list is: ", numpy_arith_mean(int_list)

def numpy_median(lst): 			# calc. median
	return np.median(lst)

print "Using numpy, median of the list is: ", numpy_median(int_list)