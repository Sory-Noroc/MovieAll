# ImdbScraper.py
# Python 3.6.8

import requests
from bs4 import BeautifulSoup
from time import sleep

class ImdbScraper:
	'''Searches Imdb for a specific product'''

	def __init__(self):
		self.imdb_link = 'https://www.imdb.com'

	def get_mlinks(self, keyword):
		'''Extracts result links for searched keyword'''
		self.page = requests.get(f'{self.imdb_link}/find?q={keyword}') # Getting the website url with the movie

		soup = BeautifulSoup(self.page.text, 'lxml') # Parsing the web page to the scraper

		found_movies = soup.find('table', class_='findList') # Finding the movies

		# Getting the links out of the movie table
		movie_links = [link.find('a').get('href') for link in found_movies.find_all('td', class_='result_text')]

		return movie_links

		for link in movie_links:
			movie_page = requests.get(self.imdb_link + link)
			new_soup = BeautifulSoup(movie_page.text, 'lxml')
			# print(new_soup.prettify())
			mname = new_soup.find('h1', class_='').text # The movie name
			if new_soup.find('span', itemprop='ratingValue'): # Check if the movie is rated
				print(f"Rating: {new_soup.find('span', itemprop='ratingValue').text}") 
			print(f"Sumarry: {new_soup.find('div', class_='summary_text').text.strip()}") # Summary
			print()
			sleep(2) # To avoid overwhelming the website

		self.search_again = input("That's it. Search again? [Yes/No] ")

if __name__ =='__main__':
	scraper = ImdbScraper()
	scraper.get_results('Game of Thrones')