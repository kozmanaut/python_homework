def sum_range(start,end):
	""" provide two intigers (smaller one first) as output and you will receive the sum of the range between the intigers """

	total = 0

	for i in range(start,end+1):
		total += i
	return total

print sum_range(5,7)