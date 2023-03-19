from typing import Callable, Iterable

from multiprocessing import Pool

import numpy as np

__all__ = ['Tweet']


class Tweet:

  EOT = 0xB16B00B5_1BADB002  # end of Tweet marker
  WORD_SIZE = 16  # size of word in bytes

  def __init__(self, content: str, tweet_id: np.int64 = 0, tweet_date: np.int64 = 0) -> None:
    self.__content = content
    self.__id = tweet_id
    self.__date = 0 if tweet_date is None else tweet_date

  @property
  def content(self) -> str:
    """
    get content of tweet\\
    this is read-only
    """
    return self.__content

  def __str__(self) -> str:
    return f'id:\n{self.__id}\ndate:\n{self.__date}\ncontent:\n{self.__content}'

  def __repr__(self) -> str:
    return self.__str__()

  def __eq__(self, other: 'Tweet') -> bool:
    return self.__id == other.id if self.__id != 0 and other.id != 0 else self.__content == other.content

  def __hash__(self) -> int:
    return hash(self.__id) if self.__id != 0 else hash(self.__content)

  def write(self, path: str) -> None:
    """
    write tweet to file
    
    ## Parameters
    ```py
      path : str
    ```
    """
    siz = self.WORD_SIZE
    # write in binary mode
    with open(path, 'ab') as f:
      # write id, date, content
      f.write(self.__id.to_bytes(siz, 'big'))
      f.write(self.__date.to_bytes(siz, 'big'))
      f.write(self.__content.encode('utf-8'))
      # write EOT marker
      f.write(Tweet.EOT.to_bytes(siz, 'big'))

  @classmethod
  def factory(cls, path: str) -> list['Tweet']:
    """
    read tweets from file
    
    ## Parameters
    ```py
    >>> path : str
    ```
    
    ## Returns
    ```py
    list[Tweet]
    ```
    """
    # read in binary mode
    with open(path, 'rb') as f:
      # read all bytes
      data = f.read()
      # split by EOT marker
      tweets = data.split(Tweet.EOT.to_bytes(cls.WORD_SIZE, 'big'))
      # remove last empty element
      tweets = tweets[:-1]
      # create Tweet objects
      tweets = [Tweet.__from_bytes(tweet) for tweet in tweets]
      return tweets

  @classmethod
  def __from_bytes(cls, data: bytes) -> 'Tweet':
    """
    create Tweet object from bytes
    
    ## Parameters
    ```py
      data : bytes
    ```
    
    ## Returns
    ```py
      Tweet
    ```
    """
    siz = cls.WORD_SIZE
    # split data into id, date and content
    tweet_id = int.from_bytes(data[:siz], 'big')
    tweet_date = int.from_bytes(data[siz:siz * 2], 'big')
    content = data[siz * 2:].decode('utf-8')
    # create Tweet object
    return Tweet(content, tweet_id, tweet_date)

  def process_content(self, f: Callable[[str], str]) -> None:
    """
    process tweet content in place
    
    ## Parameters
    ```py
    >>> f : callable[[str], str]
    ```
    """
    self.__content = f(self.__content)

  @classmethod
  def process_contents(cls, tweets: Iterable['Tweet'], f: Callable[[str], str], threads: int = 4) -> None:
    """
    process multiple tweet contents in place

    ## Parameters
    ```py
    >>> tweets : list[Tweet]
    ```
    ```py
    >>> f : callable[[str], str]
    ```
    ```py
    >>> threads : int, (optional)
    ```
    """
    if threads <= 1:
      for tweet in tweets:
        tweet.process_content(f)
    else:
      with Pool(threads) as p:
        p.map(lambda tweet: tweet.process_content(f), tweets)
