# ImdbScraper.py
# Python 3.6.8

import requests
import random
from bs4 import BeautifulSoup
from time import sleep

class ImdbSearcher:
	'''Searches Imdb for a specific product'''

	def __init__(self, keyword):
		''' The first 'm' in variable names stands for 'movie' '''
		self.imdb_link = 'https://www.imdb.com'
		self.keyword = '+'.join(keyword.split())

	def get_mlinks(self, keyword=None):
		'''Returns result links for searched keyword, as a list'''
		keyword = self.keyword if keyword is None else keyword  # Assigning keyword correctly
		if not isinstance(keyword, str):
			return []
		self.page = requests.get(f'{self.imdb_link}/find?q={keyword}') # Getting the website url with the movie

		soup = BeautifulSoup(self.page.text, 'lxml') # Parsing the web page to the scraper

		found_movies = soup.find('table', class_='findList') # Finding the movies

		# Getting the links out of the movie table
		mlinks = [link.find('a').get('href') for link in found_movies.find_all('td', class_='result_text')]

		return mlinks

	def get_minfo(self, link):
		movie_page = requests.get(self.imdb_link + link)
		new_soup = BeautifulSoup(movie_page.text, 'lxml')
		# print(new_soup.prettify())
		try:
			mname = new_soup.find('h1', class_='').text.strip() # The movie name
			if new_soup.find('span', itemprop='ratingValue'): # Check if the movie is rated
				mrating = new_soup.find('span', itemprop='ratingValue').text.strip()
			else:
				mrating = None 
			msummary = new_soup.find('div', class_='summary_text').text.strip()

			return (mname, mrating, msummary)
		except AttributeError as e:
			print(e)
			return None

	def get_all(self):
		for link in self.get_mlinks():
			try:
				name, rating, summary = self.get_minfo(link)
				print(name, rating)
				print(summary)
				sleep(random.randint(1, 3)) # To avoid overwhelming the website
			except TypeError:
				print("Coundn't extract data")
				continue

if __name__ =='__main__':
	scraper = ImdbSearcher('Game of Thrones')
	scraper.get_all()