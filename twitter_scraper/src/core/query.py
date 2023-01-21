from typing import Iterable

__all__ = ['SearchQuery']


class SearchQuery:

  def __init__(self, orig: 'SearchQuery' = None) -> None:
    match orig:
      case None:
        self.subject: str = None
        self.keywords: set[str] = set()
        self.hashtags: set[str] = set()

        self.lang: str = None

        self.start_date: str = None
        self.end_date: str = None

        self.limit: int = None
        
        self.is_question: bool = False
        self.is_positive: bool = False
        self.is_negative: bool = False
      case _:
        self.subject = orig.subject
        self.keywords = orig.keywords.copy()
        self.hashtags = orig.hashtags.copy()
        self.lang = orig.lang
        self.start_date = orig.start_date
        self.end_date = orig.end_date
        self.limit = orig.limit
        self.is_question = orig.is_question
        self.is_positive = orig.is_positive
        self.is_negative = orig.is_negative

  def with_lang(self, lang: str) -> 'SearchQuery':
    new = SearchQuery(self)
    new.lang = lang
    return new

  def set_lang(self, lang: str) -> None:
    self.lang = lang

  def with_start_date(self, year: int, month: int, day: int) -> 'SearchQuery':
    new = SearchQuery(self)
    new.start_date = f'{year}-{month}-{day}'
    return new

  def set_start_date(self, year: int, month: int, day: int) -> None:
    self.start_date = f'{year}-{month}-{day}'

  def with_end_date(self, year: int, month: int, day: int) -> 'SearchQuery':
    new = SearchQuery(self)
    new.end_date = f'{year}-{month}-{day}'
    return new

  def set_end_date(self, year: int, month: int, day: int) -> None:
    self.end_date = f'{year}-{month}-{day}'

  def with_limit(self, limit: int) -> 'SearchQuery':
    new = SearchQuery(self)
    new.limit = limit
    return new

  def set_limit(self, limit: int) -> None:
    self.limit = limit

  def with_hashtag(self, hashtag: str) -> 'SearchQuery':
    new = SearchQuery(self)
    new.hashtags.add(hashtag)
    return new

  def set_hashtag(self, hashtag: str) -> None:
    self.hashtags.add(hashtag)

  def with_hashtags(self, hashtags: Iterable[str]) -> 'SearchQuery':
    new = SearchQuery(self)
    new.hashtags.update(hashtags)
    return new

  def set_hashtags(self, hashtags: Iterable[str]) -> None:
    self.hashtags.update(hashtags)

  def with_subject(self, subject: str) -> 'SearchQuery':
    new = SearchQuery(self)
    new.subject = subject
    return new

  def set_subject(self, subject: str) -> None:
    self.subject = subject
  
  def with_keywords(self, keywords: Iterable[str]) -> 'SearchQuery':
    new = SearchQuery(self)
    new.keywords.update(keywords)
    return new
  
  def set_keywords(self, keywords: Iterable[str]) -> None:
    self.keywords.update(keywords)
