# Changelog

<summary>The full history, or so was I told...</summary>

## Beta first minor release

**v0.1** first release

-  added `twitter_scraper` module
-  added some tests
-  made `python -m build` work
-  the notebook is now working properly (even without the `twitter_scraper` pip installed)
-  added a `requirements.txt` file
-  the workflows are now working properly

**v0.2** thought out

- moved `SearchParams` to `SearchQuery`
- query is now a `SearchQuery` object and should be passed to every api call
- handle `subject`

**v0.3** yes, I'm still here

- handle `hastags` and `keywords` (maybe I should add mentions too)
- got something out `python -m build`
- added a `setup.cfg` file
- removed `setup.cfg` file

## Stable Version 1

**v1.0** first stable release

- `collection.abc` instead of `typing` (deprecated)
- lowered the requirements
- min supported python version is now 3.10.6

**v1.1** more queries and less storage

- encoded `tweet.content` into `bytes` for storage
- added retweet and reply selectors to `SearchQuery`
