l = [4, 2, 11, 54]

def sum_of_list(list):
	total = 0

	for i in list:
		total += i

	return total

print sum_of_list(l)



list1 = [1, 3, 5, 22, 1]
list2 = [2, 1, 6, 3, 9]

def remove_dup(list1, list2):
	
	x = list1[:]

	for i in x:
		if i in list2:
			list1.remove(i)
	return list1, list2

print remove_dup(list1, list2)



def simple_func(x):
	"""
	Square root function
	"""
	
	return x ** 2

list3 = [1, 2, 3, 4, 5]

def apply_to_all(numbers, func):
	"""
	Apply the desired function (in case below, the square root) to numbers in a list
	"""

	for i in range(len(numbers)):
		numbers[i] = func(numbers[i])	
	return numbers


print apply_to_all(list3, simple_func)



