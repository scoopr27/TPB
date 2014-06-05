from tpb import TPB
from tpb import CATEGORIES, ORDERS
import datetime
import os
from subprocess import call

t = TPB('https://thepiratebay.org') # create a TPB object with default domain

# class Show:
# 	"""Create a new show object"""
# 	def __init__(self, name, quality=None):
# 		self.search = name
# 		self.quality = quality

class Show:
	def __init__(self, name, dir_name, use_date=True):
		self.query = name
		self.dir_name = dir_name
		self.use_date = use_date
		
shows = [Show('colbert', 'The Colbert Report'), Show('daily show', 'The Daily Show')]
dir = "/home/scott/Videos/TV Shows"

def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)

def main():
	for show in shows:
		tv_dir = dir + "/" + show.dir_name
		f = tv_dir + "/" + ".orig"
		ensure_dir(f)
		orig = open(f, 'a+r')
		now = datetime.datetime.now()
		if show.use_date:
			query = show.query + (" %02d %02d %02d" % (int(now.year), int(now.month), int(now.day)-1))
		else
			query = show.query
			
		result = list(t.search(query, CATEGORIES.VIDEO.TV_SHOWS).order(ORDERS.SEEDERS.DES))[0]

		if not (result.title in orig.read()):
			print(result.title)
			print(result.magnet_link)
			call(["transmission-cli", '-w', tv_dir, result.magnet_link, "&"])
			orig.write(result.title + "\n")
		# print(list(t.search(show.search))[0].title)




if __name__ == "__main__":
	main()