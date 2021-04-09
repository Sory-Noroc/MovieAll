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

def get_stars(soup):
	''' Returns a dictionary of movie stars(actors) from the soup
	    as keys, and links to their profiles as values'''
	selector = 'div.credit_summary_item'
	tags = soup.select(selector)

	for div in tags:  # Making sure we are extracting the stars
		if div.h4.get_text() == 'Stars:':
			star_tags = div.select('a')

	star_dict = dict()

	for tag in star_tags[:-1]:  # Ignoring the last lag as it is not a star
		key = tag.string
		value = get_link(tag, full=True)  # Getting the full link to the actor
		star_dict[key] = value

	return star_dict

def get_movie_info(link=None, soup=None):
	''' Returns a dictionary with the data about the movie'''
	
	data_dict = {
		'title': 'div.title_wrapper > h1', 
		'rating': 'span[itemprop=ratingValue]', 
		'summary': 'div.summary_text',
		'year': '#titleYear a',
		}

	if link is not None:  # Explicit
		soup = get_soup(link)

	for prop in data_dict:
		try:
			data_dict[prop] = soup.select_one(data_dict[prop]).find(text=True, recursive=False).strip('\n  ').replace('\xa0', '')
		except AttributeError:
			data_dict[prop] = None

	data_dict['stars'] = get_stars(soup)
	return data_dict 