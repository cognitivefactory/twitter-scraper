from collections.abc import Iterable

__all__ = ['SearchQuery']


class SearchQuery:

  def __init__(self, orig: 'SearchQuery' = None) -> None:

    match orig:
      case None:
        self.subject: str = None
        self.keywords: set[str] = set()
        self.hashtags: set[str] = set()
        self.tags: set[str] = set()

        self.lang: str = None

        self.start_date: str = None
        self.end_date: str = None

        self.limit: int = None
        self.min_likes: int = None
        self.min_retweets: int = None

        self.is_retweet: bool = False
        self.is_reply: bool = False

        self.is_question: bool = False
        self.is_positive: bool = False
        self.is_negative: bool = False

      case _:
        self.subject = orig.subject
        self.keywords = orig.keywords.copy()
        self.hashtags = orig.hashtags.copy()
        self.tags = orig.tags.copy()
        self.lang = orig.lang
        self.start_date = orig.start_date
        self.end_date = orig.end_date
        self.limit = orig.limit
        self.min_likes = orig.min_likes
        self.min_retweets = orig.min_retweets
        self.is_retweet = orig.is_retweet
        self.is_reply = orig.is_reply
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
    new.limit = 10 if limit < 10 else 100 if limit > 100 else limit
    return new

  def set_limit(self, limit: int) -> None:
    self.limit = 10 if limit < 10 else 100 if limit > 100 else limit

  # def with_min_likes(self, min_likes: int) -> 'SearchQuery':
  #   new = SearchQuery(self)
  #   new.min_likes = min_likes
  #   return new

  # def set_min_likes(self, min_likes: int) -> None:
  #   self.min_likes = min_likes

  # def with_min_retweets(self, min_retweets: int) -> 'SearchQuery':
  #   new = SearchQuery(self)
  #   new.min_retweets = min_retweets
  #   return new

  # def set_min_retweets(self, min_retweets: int) -> None:
  #   self.min_retweets = min_retweets

  def with_is_retweet(self, is_retweet: bool) -> 'SearchQuery':
    """Set whether to include retweets in the search results. Incompatible with `*_is_reply`"""
    new = SearchQuery(self)
    new.is_retweet = is_retweet
    return new

  def set_is_retweet(self, is_retweet: bool) -> None:
    """Set whether to include retweets in the search results. Incompatible with `*_is_reply`"""
    self.is_retweet = is_retweet

  def with_is_reply(self, is_reply: bool) -> 'SearchQuery':
    """Set whether to include replies in the search results. Incompatible with `*_is_retweet`"""
    new = SearchQuery(self)
    new.is_reply = is_reply
    return new

  def set_is_reply(self, is_reply: bool) -> None:
    """Set whether to include replies in the search results. Incompatible with `*_is_retweet`"""
    self.is_reply = is_reply

  def with_is_question(self, is_question: bool) -> 'SearchQuery':
    new = SearchQuery(self)
    new.is_question = is_question
    return new

  def set_is_question(self, is_question: bool) -> None:
    self.is_question = is_question

  def with_is_positive(self, is_positive: bool) -> 'SearchQuery':
    new = SearchQuery(self)
    new.is_positive = is_positive
    return new

  def set_is_positive(self, is_positive: bool) -> None:
    self.is_positive = is_positive

  def with_is_negative(self, is_negative: bool) -> 'SearchQuery':
    new = SearchQuery(self)
    new.is_negative = is_negative
    return new

  def set_is_negative(self, is_negative: bool) -> None:
    self.is_negative = is_negative

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

  def with_tag(self, tag: str) -> 'SearchQuery':
    new = SearchQuery(self)
    new.tags.add(tag)
    return new

  def set_tag(self, tag: str) -> None:
    self.tags.add(tag)

  def with_tags(self, tags: Iterable[str]) -> 'SearchQuery':
    new = SearchQuery(self)
    new.tags.update(tags)
    return new

  def set_tags(self, tags: Iterable[str]) -> None:
    self.tags.update(tags)

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
