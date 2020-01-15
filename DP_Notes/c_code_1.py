import json
import xml.etree.ElementTree as etree


class JSONDataExtrator:
	def __init__(self, filepath):
		with open(filepath, 'r') as f:
			self.data = json.load(f)

	@property
	def parsed_data(self):
		return self.data


class XMLDataExtractor:
	def __init__(self, filepath):
		self.tree = etree.parse(filepath)

	@property
	def parsed_data(self):
		return self.tree


def dataextraction_factory(filepath):
	if filepath.endswith('.json'):
		extractor = JSONDataExtrator
	elif filepath.endswith('.xml'):
		extractor = XMLDataExtractor
	else:
		raise ValueError(f'Cannot extract data from {filepath}')
	return extractor(filepath)


def extract_data_from(filepath):
	factory_obj = None
	try:
		factory_obj = dataextraction_factory(filepath)
	except ValueError as e:
		print(e)
	return factory_obj


def main():
	sqlite_factory = extract_data_from('data/peson.mp3')
	print()


if __name__ == '__main__':
	# main()
	pth = r'E:\Python\Design_Pattern\Mastering-Python-Design-Patterns-Second-Edition\chapter01\data'
	json_factory = extract_data_from(pth+'/movies.json')
	json_data = json_factory.parsed_data
