import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass


class Parser:
	''' A class holding all the methods related to the interaction client -> website '''

	link = 'https://www.imdb.com/'

	criterias = {
	'Plot': 'plot', 
	'Quotes': 'quotes',
	'Trivia': 'trivia', 
	'Goofs': 'goofs', 
	'Crazy Credits': 'crazy_credits', 
	'Filming Locations':'location', 
	'Soundtracks': 'soundtracks', 
	'Versions': 'versions' }

	def get_link(self, criteria, keyword):
		''' Returns a link that will incorporate the criteria and the keyword '''
		return f'https://www.imdb.com/search/title-text/?{criteria}={keyword}'
	
	def get_soup(link=Parser.link, *args, **kwargs):
		''' Accesses the input link and returns a soup with the html'''
		r = requests.get(link)
		soup = BeautifulSoup(r.text, 'html.parser')

		return soup

	def get_tags(tag_name, link=Parser.link, class_ = '', *args, **kwargs):
		''' Returns a list of bs tags from the specified page with the specified class'''
		if class_:
			dot_class = '.'.join(class_.split())  # Correct class for css selector

		if not isinstance(tag_name, str):
			raise ValueError('Tag name must be str')

		soup = get_soup(link=link)
		result = soup.select(f'{tag_name}.{dot_class}')
		return result

	def search_movies(criteria, kw, *args, **kwargs):
		''' Advanced search based on the provided criteria and keyword 
			Returns a list of movie links'''

		if not criteria in self.criterias.values():
			raise AttributeError('No such searching criteria')

		base = self.get_link(criteria, kw)

		# Next we extract the a tags from within h3 tags using tag.a
		movie_tags = get_tags('h3', link=base, class_='lister-item-header')

		movie_links = []
		for tag in movie_tags:
			movie_links.append(get_link(tag.a, full=True))
		return movie_links


class Adjuster:
	''' A class that does all sorts of manipulating on strings/links '''

	def extract_link(tag, full=False, *args, **kwargs):
		''' Returns a link extracted from the href of the tag'''
		main_link = Parser.link
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

	def get_stars(soup, *args, **kwargs):
		''' Returns a dictionary of movie stars(actors) from the soup
			as keys, and links to their profiles as values'''
		selector = 'div.credit_summary_item'
		tags = soup.select(selector)

		for div in tags:  # Making sure we are extracting the stars
			if div.h4.get_text() == 'Stars:':
				star_tags = div.select('a')

		star_dict = dict()

		try:
			for tag in star_tags[:-1]:  # Ignoring the last tag as it is not a star
				key = tag.string
				value = get_link(tag, full=True)  # Getting the full link to the actor
				star_dict[key] = value
			return star_dict
		except UnboundLocalError:
			return {'stars': None}

class Extracter:
	''' The class that extracts the data we need about each movie '''

	data_dict = {
		'title': 'div.title_wrapper > h1', 
		'rating': 'span[itemprop=ratingValue]', 
		'summary': 'div.summary_text',
		'year': '#titleYear a',
		}

	def get_movie_info(soup, *args, **kwargs):
		''' Returns a dictionary with the data about the movie'''

		for prop in self.data_dict:
			try:
				data_dict[prop] = soup.select_one(data_dict[prop]).find(text=True, recursive=False).strip('\n  ').replace('\xa0', '')
			except AttributeError:
				print("Wrong soup or no data")
				data_dict[prop] = None

		data_dict['stars'] = Adjuster.get_stars(soup)
		return data_dict 

@dataclass
class Movie:
	''' A data class for each extracted movie ''' 
	title: str
	rating: float 
	summary: str
	year: int
	#
	duration: str
	pg: int
	photoLink: str
	#
	stars: dict