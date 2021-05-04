import pytest
from ImdbScraper import ImdbSearcher
from tools import *

s = ImdbSearcher('Minority Report')
main_link = 'https://www.imdb.com/'

def test_init():
	assert ImdbSearcher('test input words').keyword == 'test+input+words'

def test_mlinks():
	assert s.get_mlinks(7) == []
	links = s.get_mlinks()
	assert isinstance(links, list)
	assert len(links) > 0
	assert s.get_minfo(links[0])

def test_get_tags():
	testclass = 'ipc-list__item nav-link NavLink-sc-19k0khm-0 dvLykY ipc-list__item--indent-one'
	a = get_tags('a', class_=testclass)
	assert a[0]['href'] == 'https://www.imdb.com/calendar/?ref_=nv_mv_cal'
	assert a[2]['href'] == '/chart/top/?ref_=nv_mv_250'

	base = 'https://www.imdb.com/search/title-text/?plot=friendship'
	a = get_tags('h3', link=base, class_='lister-item-header')
	assert len(a) == 50
	with pytest.raises(ValueError):
		get_tags(20)

def test_soup():
	s = get_soup(main_link)
	assert s

def test_get_link():
	s = get_soup()
	tag = s.find('a')
	assert get_link(tag) == '/?ref_=nv_home'
	assert get_link(tag, full=True) == 'https://www.imdb.com/?ref_=nv_home'

def test_get_stars():
	# The Godfather
	link = 'https://www.imdb.com/title/tt0068646/?ref_=hm_tpks_tt_i_5_pd_tp1_cp'
	soup = get_soup(link)
	assert len(get_stars(soup)) == 3
	with pytest.raises(AttributeError):
		get_stars('fake soup')

def test_get_movie_info():
	assert get_movie_info(link='https://www.imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=R15M8ZM0CQGWP8JXH701&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1') == {
	'title': 'The Shawshank Redemption', 
	'rating': '9.3', 
	'summary': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
	'year': '1994',
	'stars': {
		'Bob Gunton': 'https://www.imdb.com/name/nm0348409/',
		'Morgan Freeman': 'https://www.imdb.com/name/nm0000151/',                                                                                     
    	'Tim Robbins': 'https://www.imdb.com/name/nm0000209/'
    	},
	}

	link = 'https://www.imdb.com/title/tt0468569/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=GATJM3JZ1W297Y3KQ843&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_4'
	assert get_movie_info(link) == {
	'title': 'The Dark Knight', 
	'rating': '9.0', 
	'summary': 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.',
	'year': '2008',
	'stars': {
		'Aaron Eckhart': 'https://www.imdb.com/name/nm0001173/',
		'Christian Bale': 'https://www.imdb.com/name/nm0000288/',
		'Heath Ledger': 'https://www.imdb.com/name/nm0005132/' 
		},
	}

def test_search_movies():
	assert len(search_movies('plot', 'friendship')) == 50
