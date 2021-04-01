import pytest
from ImdbScraper import ImdbSearcher

s = ImdbSearcher('Minority Report')

def test_init():
	assert ImdbSearcher('hi there').keyword == 'hi+there'

def test_mlinks():
	assert s.get_mlinks(7) == []
	links = s.get_mlinks()
	assert isinstance(links, list)
	assert len(links) > 0
	assert s.get_minfo()