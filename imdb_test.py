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
	a = get_tag('a', class_='ipc-list__item nav-link NavLink-sc-19k0khm-0 dvLykY ipc-list__item--indent-one')
	assert a[1]['href'] == '/chart/top/?ref_=nv_mv_250'
	with pytest.raises(ValueError):
		get_tag(20)

def test_soup():
	s = get_soup(main_link)
	assert isinstance(s, str)
	assert s.startswith('<')

