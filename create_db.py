import os
from datetime import datetime, timedelta, date

from unidecode import unidecode
from time import sleep
from enum import Enum

from twitter_scraper import *


class Sentiment(Enum):
  POSITIVE = 1
  NEGATIVE = 2
  QUESTION = 3

  def __str__(self):
    return self.name.lower()

  def __repr__(self):
    return self.name.lower()


def scrap_by_interval(
    start_date: str = '2009--01--01',
    end_date: str = '2023--04--01',
    interval: int = 7,                # days
    limit: int = 100,                 # tweets to scrap each interval
    out: str = 'out.bin',             # path to save tweets
    topic: str = '',                  # topic to scrap
    sentiment: Sentiment = None       # sentiment to scrap
):
  """
  doc to write properly...
  """

  tmp = start_date.split('--')
  start_year = int(tmp[0])
  start_month = int(tmp[1])
  start_day = int(tmp[2])
  tmp = end_date.split('--')
  end_year = int(tmp[0])
  end_month = int(tmp[1])
  end_day = int(tmp[2])
  print(f'scraping topic \'{topic}\' from {start_day}/{start_month}/{start_year} '
        f'to {end_day}/{end_month}/{end_year} '
        f'with {interval} days interval\n'
        f'sentiment: {sentiment},output in {out}'
       )

  s: TwitterScraper = TwitterScraper()
  q: SearchQuery = SearchQuery().with_subject(topic).with_limit(limit).with_lang('fr')

  current: date = date(start_year, start_month, start_day)
  delta_days: timedelta = timedelta(days=interval)
  one_day: timedelta = timedelta(days=1)
  next_date: date = current + delta_days - one_day # initialisation bizarre mais bref

  end_date: datetime = date(end_year, end_month, end_day)

  while current < end_date:
    print(f'  from {current} to {next_date}')

    # request
    # q.set_start_date(current.year, current.month, current.day)
    # q.set_end_date(next_date.year, next_date.month, next_date.day)
    q.set_recent_end_date(current.year, current.month, current.day)
    
    match sentiment:
      case Sentiment.POSITIVE:
        q.set_is_positive(True)
      case Sentiment.NEGATIVE:
        q.set_is_positive(False)
      case Sentiment.QUESTION:
        q.set_is_question(True)
      case None:
        pass

    # write in database
    try:
      for t in s.search(q):
        t.write(out)
    except Exception as e:
      print(f'    error: {e}')

    current = next_date + one_day
    next_date += delta_days
  print('done\n')


if __name__ == '__main__':
  try:
    os.mkdir('data')
  except FileExistsError:
    pass

  topics: list[str]
  start_date: str
  end_date: str

  if True:
    topics = [
      'Crédit mutuel',
      'banque',
      'finance',
      'cinéma',
      'critique',
      'jeu vidéo',
      'minecraft',
      'science',
      'informatique',
      'intelligence artificielle',
      'service client',
      'trump',
      'biden',
      'politique',
      'france',
      'états-unis',
      'wall street',
      'bourse',
      'déficite',
      'défense',
      'armée',
      'union européenne',
      'Europe',
      'Macron',
      'ChatGPT',
      'Copilot',
      'Covid',
      'dépression',
      'école d\'ingénieur',
      'carte graphique',
      'ordinateur',
      'sensation',
      'viol',
      'collège',
      'comté',
      'longueur',
      'clause',
      'actionnaire',
      'rénovation',
      'bizarre',
      'épisode',
      'asile',
      'solitude',
      'ultime',
      'allure',
      'excès',
      'stable',
      'roue',
      'morceau',
      'consécutif',
      'terminal',
      'épouvantable',
      'enregistrement',
      'technologique',
      'interdiction',
      'centrale',
      'studio',
      'piège',
      'prétexte',
      'bain',
      'apte',
      'rejet',
      'éthique',
      'touriste',
      'prédécesseur',
      'conception',
      'bien-être',
      'remplacement',
      'suppression',
      'légal',
      'uranium',
      'dépens',
      'imposition',
      'pôle',
      'amélioration',
      'malaise',
      'racine',
      'carton',
      'autoroute',
      'livraison',
      'urbain',
      'répression',
      'grain',
      'aliment',
      'concurrentiel',
      'marée',
      'cynique',
      'désert',
      'agriculteur',
      'ultérieur',
      'sanction',
      'phrase',
      'dispositif',
      'brut',
      'entraînement',
      'bébé',
      'contrevenant',
      'gentil',
      'tribu',
      'otage',
      'symptôme',
      'philosophie',
      'rage',
      'récit',
      'précaution',
      'correspondance',
      'humeur',
      'décor',
      'reproduction',
      'vitre',
      'rappel',
      'coupe',
      'golfe',
      'consultatif',
      'crucial',
      'ménage',
      'propagation',
      'drapeau',
      'dérive',
      'tueur',
      'registre',
      'pervers',
      'voleur',
      'plastique',
      'conviction',
      'inverse',
      'inspiration',
      'cabine',
      'clandestin',
      'volet',
    ]
    start_date = '2023--04--08'
    end_date = '2023--04--15'

  else: # pour tester si ça fonctionne
    topics = ['crédit mutuel', 'banque']
    start_date = '2023--04--08'
    end_date = '2023--04--15'

  for topic in topics:
    for sentiment in [Sentiment.POSITIVE, Sentiment.NEGATIVE, Sentiment.QUESTION]:
      sleep(10) # to avoid being banned
      # remove any non filename-friendly chars from topic (for the db file)
      path_db = os.path.join('data', unidecode(topic.lower()) + f'_{sentiment}.bin')
      scrap_by_interval(start_date=start_date, end_date=end_date, interval=1, out=path_db, topic=topic, sentiment=sentiment)
