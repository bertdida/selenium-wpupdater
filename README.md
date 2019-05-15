# selenium-wpupdater
This project helps you automate WordPress' version, plugins, and themes updates.

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

1. Rename `test_accounts.csv` to remove `test_` then update its contents for the relevant details.
2. On the terminal run:

   ```shell
   pipenv shell
   python wpupdater.py
   ```

## Author

Herbert Verdida / [@bertdida](https://twitter.com/bertdida)

