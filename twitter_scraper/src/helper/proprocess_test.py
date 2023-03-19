from .preprocess import tweet_preprocess


def test_lowercased():
  assert tweet_preprocess("Hello World", lowercased=False) == "Hello World"
  assert tweet_preprocess("Hello World", lowercased=True) == "hello world"


def test_remove_mentions_and_hastags_symbol():
  assert tweet_preprocess("Hello @World",
                          lowercased=False,
                          remove_punctuation=False,
                          remove_mentions_and_hastags=False,
                          remove_mentions_and_hastags_symbol=False) == "Hello @World"
  assert tweet_preprocess("Hello @World",
                          lowercased=False,
                          remove_punctuation=False,
                          remove_mentions_and_hastags=False,
                          remove_mentions_and_hastags_symbol=True) == "Hello World"
  assert tweet_preprocess("Hello #World",
                          lowercased=False,
                          remove_punctuation=False,
                          remove_mentions_and_hastags=False,
                          remove_mentions_and_hastags_symbol=False) == "Hello #World"
  assert tweet_preprocess("Hello #World",
                          lowercased=False,
                          remove_punctuation=False,
                          remove_mentions_and_hastags=False,
                          remove_mentions_and_hastags_symbol=True) == "Hello World"


def test_remove_mentions_and_hastags():
  assert tweet_preprocess("Hello @World",
                          lowercased=False,
                          remove_punctuation=False,
                          remove_mentions_and_hastags=False,
                          remove_mentions_and_hastags_symbol=False) == "Hello @World"
  assert tweet_preprocess("Hello @World",
                          lowercased=False,
                          remove_punctuation=False,
                          remove_mentions_and_hastags=True,
                          remove_mentions_and_hastags_symbol=False) == "Hello"
  assert tweet_preprocess("Hello #World",
                          lowercased=False,
                          remove_punctuation=False,
                          remove_mentions_and_hastags=False,
                          remove_mentions_and_hastags_symbol=False) == "Hello #World"
  assert tweet_preprocess("Hello #World",
                          lowercased=False,
                          remove_punctuation=False,
                          remove_mentions_and_hastags=True,
                          remove_mentions_and_hastags_symbol=False) == "Hello"


def test_remove_urls():
  assert tweet_preprocess("Hello https://www.google.com",
                          lowercased=False,
                          remove_punctuation=False,
                          remove_urls=False) == "Hello https://www.google.com"
  assert tweet_preprocess("Hello https://www.google.com",
                          lowercased=False,
                          remove_punctuation=False,
                          remove_urls=True) == "Hello"


def test_remove_emojis():
  assert tweet_preprocess("Hello 😊", lowercased=False, remove_emojis=False) == "Hello 😊"
  assert tweet_preprocess("Hello 😊", lowercased=False, remove_emojis=True) == "Hello"


def test_remove_punctuation():
  assert tweet_preprocess("Hello, World!", lowercased=False, remove_punctuation=False) == "Hello, World!"
  assert tweet_preprocess("Hello, World!", lowercased=False, remove_punctuation=True) == "Hello World"


def test_strip():
  assert tweet_preprocess("Hello World", lowercased=False, strip=False) == "Hello World"
  assert tweet_preprocess("Hello World", lowercased=False, strip=True) == "Hello World"
  assert tweet_preprocess("Hello  World", lowercased=False, strip=False) == "Hello  World"
  assert tweet_preprocess("Hello  World", lowercased=False, strip=True) == "Hello World"


def test_attempt_spell_correction():
  assert tweet_preprocess("Hello World", lowercased=False, attempt_spell_correction=False) == "Hello World"
  assert tweet_preprocess("Hello World", lowercased=False, attempt_spell_correction=True) == "Hello World"
