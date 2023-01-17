# Twitter Scraper

[![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg)
[![Python application](https://github.com/cognitivefactory/twitter-scraper/actions/workflows/python-app.yml/badge.svg)](https://github.com/cognitivefactory/twitter-scraper/actions/workflows/python-app.yml)
[![Pylint](https://github.com/cognitivefactory/twitter-scraper/actions/workflows/pylint.yml/badge.svg)](https://github.com/cognitivefactory/twitter-scraper/actions/workflows/pylint.yml)
[![GitHub version](https://badge.fury.io/gh/cognitivefactory%2Ftwitter-scraper.svg)](https://github.com/cognitivefactory/twitter-scraper)
[![Author](https://img.shields.io/badge/author-@ThomasByr-blue)](https://github.com/ThomasByr)

1. [✏️ Setup](#️-setup)
2. [💁 More infos and Usage](#-more-infos-and-usage)
3. [🧪 Testing](#-testing)
4. [🧑‍🏫 Contributing](#-contributing)
5. [⚖️ License](#️-license)
6. [🔄 Changelog](#-changelog)
7. [🐛 Bugs \& TODO](#-bugs--todo)

## ✏️ Setup

> **Note:** This project is currently under development. It is not yet ready for production.

Please install first the required packages with the following command:

```ps1
pip install --upgrade -r requirements.txt
```

Then you should setup a Twitter developer account and create a new app to get your API keys. You can find more information [here](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

Then you should create a new file named `.env` in the root directory of the project and add the following lines (based on [.env.example](.env.example)):

```txt
API_KEY =
API_KEY_SECRET =
BEARER_TOKEN =
```

## 💁 More infos and Usage

## 🧪 Testing

Oh god! Please don't... Still, make sure you have `pytest` installed and run the following command:

```ps1
pytest .\twitter-scraper\
```

You can also use the vscode UI to run the tests.

## 🧑‍🏫 Contributing

If you ever want to contribute, please begin by reading our [Contributing Guidelines](.github/CONTRIBUTING.md).

> The standard procedure is :
>
> ```txt
> fork -> git branch -> push -> pull request
> ```
>
> Note that we won't accept any PR :
>
> - that does not follow our Contributing Guidelines
> - that is not sufficiently commented or isn't well formated
> - without any proper test suite
> - with a failing or incomplete test suite

Happy coding ! 🙂

## ⚖️ License

This project is licensed under the [CeCILL-C FREE SOFTWARE LICENSE AGREEMENT](LICENSE). For more information, please refer to the [official website](https://cecill.info/licences/Licence_CeCILL-C_V1-en.html).

## 🔄 Changelog

See [changelog.md](changelog.md) for more information.

```mermaid
gantt
    title Main Versions
    dateFormat YYYY-MM-DD

    section source Code (v0)
    v0.1 : 2023-01-16, 1d
    v0.2 :             2d
    v0.3 :             2d
```

<details>
  <summary>  Beta first minor release (click here to expand) </summary>

**v0.1.0** first release

</details>

## 🐛 Bugs & TODO

**known bugs** (final correction patch version) [see Issues](https://github.com/?)

**todo** (first implementation version)
