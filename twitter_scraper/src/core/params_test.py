from .params import SearchParams

def test_blank_param() -> None:
  p: SearchParams = SearchParams()
  assert p is not None
  assert p.lang is None
  assert p.start_date is None
  assert p.end_date is None


def test_lang_param() -> None:
  p: SearchParams = SearchParams().with_lang('en')
  assert p is not None
  assert p.lang == 'en'
  assert p.start_date is None
  assert p.end_date is None


def test_copy() -> None:
  p: SearchParams = SearchParams()
  p1 = p.with_lang('en')
  assert p.lang is None
  assert p1.lang == 'en'
  p2 = p1.copy()
  assert p2.lang == 'en'
