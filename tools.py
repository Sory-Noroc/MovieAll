import requests
from bs4 import BeautifulSoup

def get_soup(link='https://www.imdb.com/'):
	''' Accesses the input link and returns a soup with the html'''
	r = requests.get(link)
	soup = BeautifulSoup(r.text, 'html.parser')

	return soup

def get_link(tag, full=False):
	''' Returns a link extracted from the href of the tag'''
	main_link = 'https://www.imdb.com/'
	try:
		rel_link = tag['href']
		if full:  # Full link
			rel_link = rel_link.lstrip('/') if rel_link.startswith('/') else rel_link
			link = main_link + rel_link
		else:
			link = tag['href']
		return link
	except AttributeError:
		raise AttributeError('Provided tag has no href')

def get_tag(tag_name, link='https://www.imdb.com/', class_ = '', *args, **kwargs):
	''' Returns a bs tag from the specified page with the specified class'''
	if class_:
		dot_class = '.'.join(class_.split())  # Correct class for css selector

	if not isinstance(tag_name, str):
		raise ValueError('Tag name must be str')

	soup = get_soup()
	result = soup.select(f'{tag_name}.{dot_class}')

	return result