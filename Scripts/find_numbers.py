numbers = range(1,100)

def division(x,y,list):
	for num in list:
		if num % x == 0 and num % y == 0:
			print "%d is divisible by %d and %d" % (num, x, y)
		elif num % x == 0:
			print "%d is divisible by %d" % (num, x)
		elif num % y == 0:
			print "%d is divisible by %d" % (num, y)

division(3,5,numbers)