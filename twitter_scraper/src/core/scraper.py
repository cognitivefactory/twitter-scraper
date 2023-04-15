import os
import datetime
from dataclasses import dataclass

import tweepy
import numpy as np

from dotenv import load_dotenv

from ..classes.tweet import Tweet
from .query import SearchQuery

__all__ = ['TwitterScraper', 'TweetInfo']


@dataclass
class TweetInfo:
  id: np.int64
  retweet_count: int
  reply_count: int
  like_count: int


class TwitterScraper:

  def __init__(self) -> None:

    load_dotenv()
    # api_key = os.getenv('API_KEY')
    # api_key_secret = os.getenv('API_KEY_SECRET')
    bearer_token = os.getenv('BEARER_TOKEN')
    assert bearer_token is not None, 'No bearer token found'

    self.__client = tweepy.Client(bearer_token=bearer_token)


  def get_tweet_info(self, tweet: Tweet | np.int64) -> TweetInfo:
    tweet_id = tweet if isinstance(tweet, (np.int64, int)) else tweet.id

    r: tweepy.Response = self.__client.get_tweet(tweet_id, expansions='author_id,attachments.poll_ids,attachments.media_keys,geo.place_id,in_reply_to_user_id,referenced_tweets.id,entities.mentions.username,referenced_tweets.id.author_id', tweet_fields='created_at,public_metrics,author_id,attachments,context_annotations,conversation_id,entities,geo,in_reply_to_user_id,lang,possibly_sensitive,referenced_tweets,source,text,withheld', user_fields='created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld', place_fields='contained_within,country,country_code,full_name,geo,id,name,place_type', poll_fields='duration_minutes,end_datetime,id,options,voting_status', media_fields='duration_ms,height,media_key,preview_image_url,type,url,width,public_metrics,non_public_metrics,organic_metrics,promoted_metrics,alt_text')

    assert r is not None, 'No response from Twitter API'
    assert isinstance(r, tweepy.Response), 'Invalid response from Twitter API'


    public_metrics: dict[str, int|str]
    is_valid = True
    try:
      public_metrics = r.data['public_metrics']
    except KeyError:
      is_valid = False
    assert isinstance(public_metrics, dict), 'Invalid public metrics from Twitter API'

    if not is_valid:
      return TweetInfo(-1, 0, 0, 0)

    return TweetInfo(tweet_id,
                     public_metrics['retweet_count'],
                     public_metrics['reply_count'],
                     public_metrics['like_count'],
                    )


  def search(self, query: SearchQuery) -> set[Tweet]:
    lang = query.lang if query.lang is not None else 'en'
    start_date = query.start_date if query.start_date is not None else None
    end_date = query.end_date if query.end_date is not None else None
    recent_end_date = query.recent_end_date if query.recent_end_date is not None else None
    limit = query.limit if query.limit is not None else 100

    if recent_end_date is not None:
      start_date = end_date = None

    assert query.subject is not None or len(query.keywords) > 0, 'Query must have a subject or keywords'

    dated_query = True
    final_query = ''

    if query.subject is not None:
      final_query += f'"{query.subject}"'
    if len(query.keywords) > 0:
      final_query += f' {" OR ".join(query.keywords)}'

    final_query += f' {" @".join(query.tags)}' if len(query.tags) > 0 else ''
    final_query += f'#{" #".join(query.hashtags)}' if len(query.hashtags) > 0 else ''

    if query.is_question:
      final_query += ' ?'
    elif query.is_positive:
      final_query += ' :)'
    elif query.is_negative:
      final_query += ' :('

    if query.is_retweet:
      final_query += ' is:retweet'
    elif query.is_reply:
      final_query += ' is:reply'

    final_query += f' lang:{lang}'

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
      r = self.__client.search_all_tweets(query=final_query, max_results=limit, start_time=start_date, end_time=end_date)
    else:
      assert start_date is None and end_date is None
      r = self.__client.search_recent_tweets(query=final_query, max_results=limit, end_time=recent_end_date+'T23:59:59Z')

    assert r is not None, 'No response from Twitter API'
    assert isinstance(r, tweepy.Response), 'Invalid response from Twitter API'
    assert isinstance(r.data, list), 'Invalid response data from Twitter API'
    return set(Tweet(t.text, t.id, t.created_at) for t in r.data)
