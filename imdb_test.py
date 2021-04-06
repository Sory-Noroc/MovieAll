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

def test_req():
	testclass = 'ipc-list__item nav-link NavLink-sc-19k0khm-0 dvLykY ipc-list__item--indent-one'
	a = get_tag('a', class_=testclass)
	assert a[0]['href'] == 'https://www.imdb.com/calendar/?ref_=nv_mv_cal'
	assert a[2]['href'] == '/chart/top/?ref_=nv_mv_250'
	with pytest.raises(ValueError):
		get_tag(20)

def test_soup():
	s = get_soup(main_link)
	assert s

def test_get_link():
	s = get_soup()
	tag = s.find('a')
	assert get_link(tag) == '/?ref_=nv_home'
	assert get_link(tag, full=True) == 'https://www.imdb.com/?ref_=nv_home'

def test_get_movie_info():
	assert get_movie_info(link='https://www.imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=R15M8ZM0CQGWP8JXH701&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1') == {
	'title': 'The Shawshank Redemption', 
	'rating': '9.3', 
	'summary': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
	'year': '1994'
	}

	link = 'https://www.imdb.com/title/tt0468569/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=GATJM3JZ1W297Y3KQ843&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_4'
	assert get_movie_info(link) == {
	'title': 'The Dark Knight', 
	'rating': '9.0', 
	'summary': 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.',
	'year': '2008'
	}
