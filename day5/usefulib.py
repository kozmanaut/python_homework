import os

def add(x,y):
	return x + y

def multiply(x,y):
	return x * y

class Song(object):
	def __init__(self, path):
		print os.path.exists(path)
