import os

from .tweet import Tweet

tweet_id = 0x1234567890ABCDEF
tweet_date = 0xAABBCCDDEEFF0011
tweet_content = 'Hello, world!'

# try to create the data directory
try:
  os.mkdir('data')
except FileExistsError:
  pass

# try to remove the test file
try:
  os.remove(os.path.join('data', 'tweet_test.bin'))
except FileNotFoundError:
  pass


def test_save_tweet() -> None:
  t: Tweet = Tweet(tweet_content, tweet_id, tweet_date)
  t.write(os.path.join('data', 'tweet_test.bin'))
  assert os.path.exists(os.path.join('data', 'tweet_test.bin'))


def test_load_tweet() -> None:
  tweets: list[Tweet] = Tweet.factory(os.path.join('data', 'tweet_test.bin'))
  assert len(tweets) == 1
  assert tweets[0].id == tweet_id
  assert tweets[0].date == tweet_date
  assert tweets[0].content == tweet_content


def test_save_multiple_tweets() -> None:
  t1: Tweet = Tweet(tweet_content, tweet_id, tweet_date)
  t2: Tweet = Tweet(tweet_content, tweet_id, tweet_date)
  t1.write(os.path.join('data', 'tweet_test.bin'))
  t2.write(os.path.join('data', 'tweet_test.bin'))
  assert os.path.exists(os.path.join('data', 'tweet_test.bin'))


def test_load_multiple_tweets() -> None:
  tweets: list[Tweet] = Tweet.factory(os.path.join('data', 'tweet_test.bin'))
  for tweet in tweets:
    assert tweet.id == tweet_id
    assert tweet.date == tweet_date
    assert tweet.content == tweet_content
