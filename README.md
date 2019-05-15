# selenium-wpupdater

## Prerequisites

- Python 3.6
- [Pipenv](https://github.com/pypa/pipenv)
- [ChromeDriver](http://chromedriver.chromium.org/downloads)

## Installation

1. Download and extract the [zip file](https://github.com/bertdida/selenium-wpupdater/archive/master.zip) or use Git to clone this repository.
2. Inside the directory open a terminal and run:

    ```shell
    pipenv install
    ```

## Usage

1. Create `accounts.csv` file; this should contain the WordPress URLs, usernames and passwords. Check [test_accounts.csv](https://github.com/bertdida/selenium-wpupdater/blob/master/test_accounts.csv) for example.
2. Open a terminal and run the following:

   ```shell
   pipenv shell
   python wpupdater.py
   ```

