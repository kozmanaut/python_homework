text = ((1, 'mine'), (3, 'yours'), (7, 'yours'))

def min_max(input):
	
	words = ()
	numbers = ()

	for item in input:
		numbers += (item[0],)
		if item[1] not in words:
			words += (item[1],)

	max_number = max(numbers)
	min_number = min(numbers)
	unique_words = len(words)

	return (min_number, max_number, unique_words)

print min_max(text)
