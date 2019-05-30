# selenium-wpupdater

This project helps you update WordPress (WP) automatically. It does this by parsing a file that contains WP URLs with their corresponding username and password, then simulate the following for each data set:

1. Opens a browser
2. Logs in to WP dashboard
3. Checks to see if any of core, plugin, and theme updates are available — if yes do update
4. Logs out from the dashboard

## Prerequisites

- Python 2.7 or above
- [Pipenv](https://github.com/pypa/pipenv)
- [ChromeDriver](http://chromedriver.chromium.org/downloads)

## Installation

1. Download and extract the [zip file](https://github.com/bertdida/selenium-wpupdater/archive/master.zip) or use Git to clone this repository.
2. Inside the directory open a terminal and run:

    ```shell
    pipenv install
    ```

## Usage

1. Edit **wpupdater.py** and set `CHROMEDRIVER_PATH` to your driver's executable path.
2. Rename **test_accounts.csv** to remove **test_** then update its contents for the appropriate data.
3. On the terminal run:

   ```shell
   pipenv shell
   python wpupdater.py
   ```

## Author

Herbert Verdida / [@bertdida](https://twitter.com/bertdida)

