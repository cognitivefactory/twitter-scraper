import os
import datetime

import tweepy

from dotenv import load_dotenv

from ..classes.tweet import Tweet
from .params import SearchParams

__all__ = ['TwitterScraper']


class TwitterScraper:

  def __init__(self, params: SearchParams = None) -> None:

    load_dotenv()
    # api_key = os.getenv('API_KEY')
    # api_key_secret = os.getenv('API_KEY_SECRET')
    bearer_token = os.getenv('BEARER_TOKEN')

    self._params = params
    self._client = tweepy.Client(bearer_token=bearer_token)


  def search(self, query: str, limit: int = 100) -> list[Tweet]:
    lang = self._params.lang if self._params else 'en'
    start_date = self._params.start_date if self._params else None
    end_date = self._params.end_date if self._params else None
    dated_query = True
    query = f'{query} lang:{lang}'
    r: tweepy.Response
    match start_date, end_date:
      case None, None:
        dated_query = False
      case _, None:
        end_date = datetime.datetime.now().strftime('%Y-%m-%d')
      case None, _:
        start_date = (datetime.datetime.strptime(end_date, '%Y-%m-%d') - datetime.timedelta(days=30)).strftime('%Y-%m-%d')
      case _, _:
        pass

    if dated_query:
      assert start_date is not None and end_date is not None
      r = self._client.search_all_tweets(query=query, max_results=limit, start_time=start_date, end_time=end_date)
    else:
      assert start_date is None and end_date is None
      r = self._client.search_recent_tweets(query=query, max_results=limit)

    assert r is not None, 'No response from Twitter API'
    assert isinstance(r, tweepy.Response), 'Invalid response from Twitter API'
    assert isinstance(r.data, list), 'Invalid response data from Twitter API'
    return [Tweet(t.text, t.id) for t in r.data]
