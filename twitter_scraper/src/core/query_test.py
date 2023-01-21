from .query import SearchQuery


def test_blank_param() -> None:
  p: SearchQuery = SearchQuery()
  assert p is not None
  assert p.lang is None
  assert p.start_date is None
  assert p.end_date is None


def test_lang_param() -> None:
  p: SearchQuery = SearchQuery().with_lang('en')
  assert p is not None
  assert p.lang == 'en'
  assert p.start_date is None
  assert p.end_date is None


def test_copy() -> None:
  p: SearchQuery = SearchQuery()
  p1 = p.with_lang('en')
  assert p.lang is None
  assert p1.lang == 'en'
  p2 = SearchQuery(p1)
  assert p2.lang == 'en'


def test_set() -> None:
  p: SearchQuery = SearchQuery()
  p1 = p.with_lang('en')
  p.set_lang('fr')
  assert p.lang == 'fr' and p1.lang == 'en'
  p1.set_lang('de')
  assert p.lang == 'fr' and p1.lang == 'de'
