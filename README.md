# selenium-wpupdater

This project updates your WP (WordPress) automatically. It reads a CSV file that contains WP URLs, usernames and passwords then simulate the following for each data set:

1. Open a browser
2. Login to WP dashboard
3. Check to see if core, plugin, and theme updates are available — if yes do update
4. Logout

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

1. Inside `wpupdater.py`, change `CHROMEDRIVER_PATH` value to your driver's path.
2. Rename `test_accounts.csv` to remove `test_` then update its contents for the relevant details.
3. On the terminal run:

   ```shell
   pipenv shell
   python wpupdater.py
   ```

## Author

Herbert Verdida / [@bertdida](https://twitter.com/bertdida)

