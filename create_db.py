from twitter_scraper import *
import os
import numpy as np
from datetime import datetime, timedelta, date


def next_date(y:int,m:int,d:int,add_days:int=1):
    pass


def scrap_by_interval(
    start_date:str="2009--01--01",
    end_date:str="2023--04--01",
    interval:int=7, # days
    limit:int=100,  # tweets to scrap each interval
    # sleep_time:int=0, # delay between 2 requests
    out:str="out.bin", # path to save tweets
    topic:str=""  # topic to scrap
    ):
    """
    doc to write properly...
    """
    tmp = start_date.split("--")
    start_year = int(tmp[0])
    start_month = int(tmp[1])
    start_day = int(tmp[2])
    tmp = end_date.split("--")
    end_year = int(tmp[0])
    end_month = int(tmp[1])
    end_day = int(tmp[2])
    print(f"scraping topic \"{topic}\" from {start_day}/{start_month}/{start_year} "
          f"to {end_day}/{end_month}/{end_year} "
          f"with {interval} days interval\n"
          f"output in {out}")
    
    s: TwitterScraper = TwitterScraper()
    q: SearchQuery = SearchQuery().with_subject(topic).with_limit(limit)

    # tweets_seen:set[np.int64] = set()

    current:date = date(start_year,start_month,start_day)
    delta_days:timedelta = timedelta(days=interval)
    one_day:timedelta = timedelta(days=1)
    next_date:date = current + delta_days - one_day # initialisation bizarre mais bref

    end_date:datetime = date(end_year,end_month,end_day)

    while current < end_date:
        print(f"  from {current} to {next_date}")
        
        # request
        q.set_start_date(current.year, current.month, current.day)
        q.set_end_date(next_date.year, next_date.month, next_date.day)
        r: list[Tweet] = s.search(q) 

        # duplicate verification
        #TODO

        # write in database
        for t in r:
            t.write(out)
    
        current = next_date + one_day
        next_date += delta_days

    print("done\n")

if __name__ == '__main__':
    try:
        os.mkdir('data')
    except FileExistsError:
        pass
    
    if False:
        topics = [
            "Crédit mutuel",
            "banque",
            "finance",
            "cinéma",
            "critique",
            "jeu vidéo",
            "minecraft",
            "science",
            "informatique",
            "intelligence artificielle",
            "service client",
            "trump",
            "biden",
            "politique",
            "france",
            "états-unis"
        #...
        ]
        start_date="2009--01--01"
        end_date="2023--04--01"

    else: # pour tester si ça fonctionne
        topics = [
            "crédit mutuel",
            "banque"
        ]
        start_date="2020--01--01"
        end_date  ="2020--03--20"

    for topic in topics:
        # remove any non filename-friendly chars from topic (for the db file)
        path_db = os.path.join('data', f"{''.join(x for x in topic if x.isalnum() and x.isascii())}.bin")
        scrap_by_interval(
            start_date=start_date,
            end_date=end_date,
            interval=7,
            out=path_db,
            topic=topic
        )