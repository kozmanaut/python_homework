import os
import warnings
import sh

################################################################################################
class Song(object):
	""" A class that describes musical songs """
	
	def __init__(self,title, artist, duration):	
		self.title = title
		self.artist = artist
		self.duration = duration

		try :
			self.duration = int(duration)
		except :
			warnings.warn("Duration of %s by %s was not a number - setting to 0" % (self.title, self.artist))
			self.duration = 0
			

		if self.duration < 0 :
			warnings.warn("Duration of %s by %s is negative - setting to 0" % (self.title, self.artist))
			self.duration = 0 
			

	def pretty_duration(self):
		"""Easily readable duration of songs """
		min, sec = divmod(self.duration, 60)
		hr, min = divmod(min, 60)
		return "The duration of %s by %s is %02i:%02i:%02i" % (self.title, self.artist, hr, min, sec)

	def play(self):
		"""Open a youtube search for the title of the song """
		url = 'https://www.youtube.com/results?search_query=%s' % (self.title.replace(" ", "+")) 
		sh.google_chrome(url)

######################################################################################################

path = os.environ["HOME"]
infile = open(path+"/lulu_mix_16.csv", "r")

songs = []

for line in infile:
	if line.startswith("Name,Artist") : continue 		# dont do anything with the header
	title, artist, duration = line.split(",")			# split the string into name, artist and duration
	current_song = Song(title, artist, duration)		# create a song instance for each line
	songs.append(current_song)							# append each song to the list 'songs'

for s in songs: print s.artist
for s in songs: print s.pretty_duration()
print sum(s.duration for s in songs), "seconds in total"
songs[6].play()