import re
import string

from enum import Enum
from typing_extensions import override

import nltk
from spellchecker import SpellChecker

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer


__all__ = ['TweetPreprocessor', 'TweetPreprocessorLanguage']


class TweetPreprocessorLanguage(Enum):
  ENGLISH = 1
  FRENCH = 2

  @override
  def value(self) -> str:
    match self:
      case TweetPreprocessorLanguage.ENGLISH:
        return "english"
      case TweetPreprocessorLanguage.FRENCH:
        return "french"
    raise NotImplementedError

  def short_value(self) -> str:
    match self:
      case TweetPreprocessorLanguage.ENGLISH:
        return "en"
      case TweetPreprocessorLanguage.FRENCH:
        return "fr"
    raise NotImplementedError

  @staticmethod
  def from_string(value: str) -> 'TweetPreprocessorLanguage':
    match value.lower():
      case "english" | "en":
        return TweetPreprocessorLanguage.ENGLISH
      case "french" | "fr":
        return TweetPreprocessorLanguage.FRENCH
    raise NotImplementedError


class TweetPreprocessor:
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

  def __init__(self, language: TweetPreprocessorLanguage | str = TweetPreprocessorLanguage.ENGLISH):
    # some nltk stuff (did not investigate)
    nltk.download('punkt', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download("omw-1.4", quiet=True)

    self.__language = TweetPreprocessorLanguage.from_string(language)\
                      if isinstance(language, str) else language

    # spellchecker
    self.__s = SpellChecker(language=self.__language.short_value())

    # stemmer and lemmatizer
    self.__ps = PorterStemmer()
    self.__wnl = WordNetLemmatizer()


  def __tokenize(self, x: str) -> list[str]:
    return word_tokenize(x, language=self.__language.value())


  def run(  # pylint: disable=too-many-arguments
      self,
      content: str,
      lowercased: bool = True,
      remove_mentions_and_hastags: bool = False,
      remove_mentions_and_hastags_symbol: bool = True,
      remove_urls: bool = True,
      remove_emojis: bool = True,
      remove_punctuation: bool = True,
      strip: bool = True,
      attempt_spell_correction: bool = False,
      apply_stemming: bool = False,
      apply_lemmatization: bool = False,
      return_tokens: bool = False,
  ) -> str | list[str]:
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
    ```py
    >>> apply_stemming : bool, (optional)
    ```
    apply stemming to the content\\
    defaults to `False`
    ```py
    >>> apply_lemmatization : bool, (optional)
    ```
    apply lemmatization to the content\\
    note that this is a slow process and is not compatible with stemming\\
    defaults to `False`
    ```py
    >>> return_tokens : bool, (optional)
    ```
    set the return type to a list of tokens\\
    defaults to `False`

    ## Returns
    ```py
    str | list[str] : new content
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
      tweet = re.sub(self.EMOJI_PATTERN, '', tweet)

    if remove_punctuation:
      tweet = tweet.translate(str.maketrans('', '', string.punctuation))

    if strip:
      tweet = re.sub(r'\s+', ' ', tweet).strip()

    if attempt_spell_correction:
      tweet = ' '.join(self.__s.correction(word) for word in tweet.split())

    if apply_stemming:
      tweet = ' '.join(self.__ps.stem(word) for word in tweet.split())
    elif apply_lemmatization:
      tweet = ' '.join(self.__wnl.lemmatize(word) for word in tweet.split())

    return tweet if not return_tokens else self.__tokenize(tweet)
