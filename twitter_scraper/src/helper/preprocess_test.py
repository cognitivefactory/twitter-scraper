from .preprocess import TweetPreprocessor

tp = TweetPreprocessor()


def test_lowercased():
  assert tp.run("Hello World", lowercased=False) == "Hello World"
  assert tp.run("Hello World", lowercased=True) == "hello world"


def test_remove_mentions_and_hastags_symbol():
  assert tp.run("Hello @World",
                  lowercased=False,
                  remove_punctuation=False,
                  remove_mentions_and_hastags=False,
                  remove_mentions_and_hastags_symbol=False) == "Hello @World"
  assert tp.run("Hello @World",
                  lowercased=False,
                  remove_punctuation=False,
                  remove_mentions_and_hastags=False,
                  remove_mentions_and_hastags_symbol=True) == "Hello World"
  assert tp.run("Hello #World",
                  lowercased=False,
                  remove_punctuation=False,
                  remove_mentions_and_hastags=False,
                  remove_mentions_and_hastags_symbol=False) == "Hello #World"
  assert tp.run("Hello #World",
                  lowercased=False,
                  remove_punctuation=False,
                  remove_mentions_and_hastags=False,
                  remove_mentions_and_hastags_symbol=True) == "Hello World"


def test_remove_mentions_and_hastags():
  assert tp.run("Hello @World",
                  lowercased=False,
                  remove_punctuation=False,
                  remove_mentions_and_hastags=False,
                  remove_mentions_and_hastags_symbol=False) == "Hello @World"
  assert tp.run("Hello @World",
                  lowercased=False,
                  remove_punctuation=False,
                  remove_mentions_and_hastags=True,
                  remove_mentions_and_hastags_symbol=False) == "Hello"
  assert tp.run("Hello #World",
                  lowercased=False,
                  remove_punctuation=False,
                  remove_mentions_and_hastags=False,
                  remove_mentions_and_hastags_symbol=False) == "Hello #World"
  assert tp.run("Hello #World",
                  lowercased=False,
                  remove_punctuation=False,
                  remove_mentions_and_hastags=True,
                  remove_mentions_and_hastags_symbol=False) == "Hello"


def test_remove_urls():
  assert tp.run("Hello https://www.google.com",
                  lowercased=False,
                  remove_punctuation=False,
                  remove_urls=False) == "Hello https://www.google.com"
  assert tp.run("Hello https://www.google.com",
                  lowercased=False,
                  remove_punctuation=False,
                  remove_urls=True) == "Hello"


def test_remove_emojis():
  assert tp.run("Hello 😊", lowercased=False, remove_emojis=False) == "Hello 😊"
  assert tp.run("Hello 😊", lowercased=False, remove_emojis=True) == "Hello"


def test_translate_emojis():
  assert tp.run("Hello 😊", lowercased=False, remove_emojis=False, translate_emojis=False) == "Hello 😊"
  assert tp.run("Hello 😊", lowercased=False, remove_emojis=False, translate_emojis=True) == "Hello blush"


def test_remove_punctuation():
  assert tp.run("Hello, World!", lowercased=False, remove_punctuation=False) == "Hello, World!"
  assert tp.run("Hello, World!", lowercased=False, remove_punctuation=True) == "Hello World"


def test_strip():
  assert tp.run("Hello World", lowercased=False, strip=False) == "Hello World"
  assert tp.run("Hello World", lowercased=False, strip=True) == "Hello World"
  assert tp.run("Hello  World", lowercased=False, strip=False) == "Hello  World"
  assert tp.run("Hello  World", lowercased=False, strip=True) == "Hello World"


def test_attempt_spell_correction():
  assert tp.run("Hello World", lowercased=False, attempt_spell_correction=False) == "Hello World"
  assert tp.run("Hello World", lowercased=False, attempt_spell_correction=True) == "Hello World"


def test_apply_stemming():
  assert tp.run("programmer", apply_stemming=False) == "programmer"
  assert tp.run("programmer", apply_stemming=True) == "programm"


def test_apply_lemmatization():
  assert tp.run("programmer", apply_lemmatization=False) == "programmer"
  assert tp.run("programmer", apply_lemmatization=True) == "programmer"


def test_return_tokens():
  match tp.run("Hello World", return_tokens=False):
    case str(_):
      pass
    case _:
      raise AssertionError("Should be a string")
  match tp.run("Hello World", return_tokens=True):
    case list(l):
      match l:
        case [str(_), *_]:
          pass
        case _:
          raise AssertionError("Should be a list of strings")
    case _:
      raise AssertionError("Should be a list")
