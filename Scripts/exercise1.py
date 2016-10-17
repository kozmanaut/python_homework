s = 'az2cbobobegghakl'

def vowel_count(string):
	count = 0
	
	if any(i.isdigit() for i in string):
		print "There is a number!"
	else:
		for i in string:
			if i == "a" or i == "i" or i == "o" or i == "u" or i == "e":
				count += 1
	
			return count

print vowel_count(s)
