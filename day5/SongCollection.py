class SongCollection(object):
	def __init__(self, songs):
		assert isinstance(songs,list)
		self.songs = songs

	def __len__(self):
		"""lenght of the class - i.e. how many songs are there """
		return len(self.songs)

	def __str__(self):
		return "A collection with %d songs"	% len(self)
		
	def __nonzero__(self):
		return False

	def __getitem__(self,num):
		"""Enable indexing"""
		return self.songs[num]	

	def __iter__(self):
		""" Decide iterative behaviour"""
		return iter([1,2,3,4,5])

collections = SongCollection(songs)