import numpy as np

__all__ = ['Tweet']


class Tweet:

  EOT = 0xB16B00B51BADB002  # end of Tweet marker
  WORD_SIZE = 16  # size of word in bytes

  def __init__(self, content: str, tweet_id: np.int64 = 0, tweet_date: np.int64 = 0) -> None:
    self.content = content
    self.id = tweet_id
    self.date = tweet_date

  def __str__(self) -> str:
    return self.content

  def __repr__(self) -> str:
    return self.__str__()

  def __eq__(self, other: 'Tweet') -> bool:
    return self.id == other.id

  def __hash__(self) -> int:
    return hash(self.id)

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
      f.write(self.id.to_bytes(siz, 'big'))
      f.write(self.date.to_bytes(siz, 'big'))
      f.write(self.content.encode('utf-8'))
      # write EOT marker
      f.write(Tweet.EOT.to_bytes(siz, 'big'))

  @classmethod
  def factory(cls, path: str) -> list['Tweet']:
    """
    read tweets from file
    
    ## Parameters
    ```py
      path : str
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
      tweets = [Tweet._from_bytes(tweet) for tweet in tweets]
      return tweets

  @classmethod
  def _from_bytes(cls, data: bytes) -> 'Tweet':
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
