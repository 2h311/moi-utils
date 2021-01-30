# This is our base writer which will be extended for other writers
# TODO: define some methods and properties for all writers

def write_multiple_items(file, args, *, separator=','):
	file.write(separator.join(args))

class Writer:
	def __init__(self, filename):
		self.filename = filename



