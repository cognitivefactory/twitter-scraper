from .scraper import TwitterScraper


def test_connect() -> None:
  s: TwitterScraper = TwitterScraper()
  assert s is not None
