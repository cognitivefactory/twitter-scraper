import os
import datetime

import tweepy

from dotenv import load_dotenv

from ..classes.tweet import Tweet
from .query import SearchQuery

__all__ = ['TwitterScraper']


class TwitterScraper:

  def __init__(self) -> None:

    load_dotenv()
    # api_key = os.getenv('API_KEY')
    # api_key_secret = os.getenv('API_KEY_SECRET')
    bearer_token = os.getenv('BEARER_TOKEN')

    self._client = tweepy.Client(bearer_token=bearer_token)


  def search(self, query: SearchQuery) -> list[Tweet]:
    lang = query.lang if query.lang is not None else 'en'
    start_date = query.start_date if query.start_date is not None else None
    end_date = query.end_date if query.end_date is not None else None
    limit = query.limit if query.limit is not None else 100

    dated_query = True
    final_query = f'{query.subject} lang:{lang}'

    r: tweepy.Response = None
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
      r = self._client.search_all_tweets(query=final_query, max_results=limit, start_time=start_date, end_time=end_date)
    else:
      assert start_date is None and end_date is None
      r = self._client.search_recent_tweets(query=final_query, max_results=limit)

    assert r is not None, 'No response from Twitter API'
    assert isinstance(r, tweepy.Response), 'Invalid response from Twitter API'
    assert isinstance(r.data, list), 'Invalid response data from Twitter API'
    return [Tweet(t.text, t.id) for t in r.data]
