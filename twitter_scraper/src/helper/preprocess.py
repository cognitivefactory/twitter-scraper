import re
import string

from spellchecker import SpellChecker

__all__ = ['tweet_preprocess']

s = SpellChecker(language={'en', 'fr'})

EMOJI_PATTERN = re.compile("["
                           "\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "\U0001F300-\U0001F5FF"  # symbols & pictographs
                           "\U0001F600-\U0001F64F"  # emoticons
                           "\U0001F680-\U0001F6FF"  # transport & map symbols
                           "\U0001F700-\U0001F77F"  # alchemical symbols
                           "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                           "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                           "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                           "\U0001FA00-\U0001FA6F"  # Chess Symbols
                           "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                           "\U00002702-\U000027B0"  # Dingbats
                           "\U000024C2-\U0001F251"
                           "]+")


def tweet_preprocess(
    content: str,
    lowercased: bool = True,
    remove_mentions_and_hastags: bool = True,
    remove_mentions_and_hastags_symbol: bool = True,
    remove_urls: bool = True,
    remove_emojis: bool = True,
    remove_punctuation: bool = True,
    strip: bool = True,
    attempt_spell_correction: bool = False,
    # apply_stemming: bool = False,
    # apply_lemmatization: bool = False,
) -> str:
  """
  standard function to preprocess tweets

  ## Parameters
  ```py
  >>> content : str
  ```
  content of the tweet, mandatory (will be copied)
  ```py
  >>> lowercased : bool, (optional)
  ```
  if the content should be turned into lowercase first, advised\\
  defaults to `True`
  ```py
  >>> remove_mentions_and_hastags : bool, (optional)
  ```
  remove all '@' and '#' and following attached word\\
  defaults to `True`
  ```py
  >>> remove_mentions_and_hastags_symbol : bool, (optional)
  ```
  remove all '@' and '#'\\
  defaults to `True`
  ```py
  >>> remove_urls : bool, (optional)
  ```
  remove all links\\
  defaults to `True`
  ```py
  >>> remove_emojis : bool, (optional)
  ```
  remove all emojis\\
  defaults to `True`
  ```py
  >>> remove_punctuation : bool, (optional)
  ```
  remove all punctuation (`!"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~` and backtick)\\
  defaults to `True`
  ```py
  >>> strip : bool, (optional)
  ```
  remove duplicate whitespace and strip the content\\
  defaults to `True`
  ```py
  >>> attempt_spell_correction : bool, (optional)
  ```
  attempts spell correction using default fr and en dictionnary\\
  note that this is a very slow process
  and will replace all whitespace with a single space\\
  defaults to `False`

  ## Returns
  ```py
  str : new content
  ```
  """
  tweet = content.lower() if lowercased else content[::]

  if remove_mentions_and_hastags:
    tweet = re.sub(r'[@#]\w+', '', tweet)
  elif remove_mentions_and_hastags_symbol:
    tweet = re.sub(r'[@#]', '', tweet)

  if remove_urls:
    tweet = re.sub(r'\S*https?:\S*', '', tweet)

  if remove_emojis:
    tweet = re.sub(EMOJI_PATTERN, '', tweet)

  if remove_punctuation:
    tweet = tweet.translate(str.maketrans('', '', string.punctuation))

  if strip:
    tweet = re.sub(r'\s+', ' ', tweet).strip()

  if attempt_spell_correction:
    tweet = ' '.join(s.correction(word) for word in tweet.split())

  return tweet
