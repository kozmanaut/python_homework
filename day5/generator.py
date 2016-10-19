def my_generator():
	handle = open("lulu_mix_16.csv")
	handle.next()
	for line in handle:
		title = line.split(",")[0]
		title = title.upper()
		yield title

r = my_generator()


