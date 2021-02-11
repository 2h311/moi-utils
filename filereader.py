'''
accepts filename, return content of file if it exists
else returns an error.
'''
from configparser import ConfigParser
from pathlib import Path

class FileReader:
	@staticmethod
	def file_content():
		'''read in the content of a file into a list'''
		path_object = Path(input("\aEnter a valid filename: "))
		if path_object.exists():
			with path_object.open() as file_handler:
				content = [ line.strip() for line in file_handler.readlines() ]
				return content if content else "No keywords in the file specified"	

		raise Exception("\aYou might have to check the file name.")

	@staticmethod
	def read_ini(filename, section):
		'''read in login credentials from ini file'''
		parser = ConfigParser()
		parser.read(filename)

		if parser.has_section(section):
			# get section
			params = parser.items(section)
			return {param[0]: param[1] for param in params }
		else:
			raise Exception(f"Section {section} not found in {filename}")
