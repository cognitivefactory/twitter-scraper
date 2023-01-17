__all__ = ['SearchParams']


class SearchParams:

  def __init__(self) -> None:
    self.lang: str = None
    self.start_date: str = None
    self.end_date: str = None

  def copy(self) -> 'SearchParams':
    p = SearchParams()
    p.lang = self.lang
    p.start_date = self.start_date
    p.end_date = self.end_date
    return p

  def with_lang(self, lang: str) -> 'SearchParams':
    new = self.copy()
    new.lang = lang
    return new

  def with_start_date(self, year: int, month: int, day: int) -> 'SearchParams':
    new = self.copy()
    new.start_date = f'{year}-{month}-{day}'
    return new

  def with_end_date(self, year: int, month: int, day: int) -> 'SearchParams':
    new = self.copy()
    new.end_date = f'{year}-{month}-{day}'
    return new
