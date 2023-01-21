__all__ = ['SearchQuery']


class SearchQuery:

  def __init__(self) -> None:
    self.subject: str = None
    self.hashtags: set[str] = []

    self.lang: str = None

    self.start_date: str = None
    self.end_date: str = None

    self.limit: int = None

  def copy(self) -> 'SearchQuery':
    p = SearchQuery()
    p.subject = self.subject
    p.hashtags = self.hashtags.copy()
    p.lang = self.lang
    p.start_date = self.start_date
    p.end_date = self.end_date
    p.limit = self.limit
    return p

  def with_lang(self, lang: str) -> 'SearchQuery':
    new = self.copy()
    new.lang = lang
    return new

  def set_lang(self, lang: str) -> None:
    self.lang = lang

  def with_start_date(self, year: int, month: int, day: int) -> 'SearchQuery':
    new = self.copy()
    new.start_date = f'{year}-{month}-{day}'
    return new

  def set_start_date(self, year: int, month: int, day: int) -> None:
    self.start_date = f'{year}-{month}-{day}'

  def with_end_date(self, year: int, month: int, day: int) -> 'SearchQuery':
    new = self.copy()
    new.end_date = f'{year}-{month}-{day}'
    return new

  def set_end_date(self, year: int, month: int, day: int) -> None:
    self.end_date = f'{year}-{month}-{day}'

  def with_limit(self, limit: int) -> 'SearchQuery':
    new = self.copy()
    new.limit = limit
    return new

  def set_limit(self, limit: int) -> None:
    self.limit = limit

  def with_hashtag(self, hashtag: str) -> 'SearchQuery':
    new = self.copy()
    new.hashtags.add(hashtag)
    return new

  def set_hashtag(self, hashtag: str) -> None:
    self.hashtags.add(hashtag)

  def with_hashtags(self, hashtags: list[str]) -> 'SearchQuery':
    new = self.copy()
    new.hashtags.update(hashtags)
    return new

  def set_hashtags(self, hashtags: list[str]) -> None:
    self.hashtags.update(hashtags)

  def with_subject(self, subject: str) -> 'SearchQuery':
    new = self.copy()
    new.subject = subject
    return new

  def set_subject(self, subject: str) -> None:
    self.subject = subject
