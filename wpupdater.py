import csv
import time
from selenium import webdriver
from urllib.request import urlopen, URLError, HTTPError

CHROMEDRIVER_PATH = "chromedriver_win32\\chromedriver.exe"
ACCOUNTS_PATH = "accounts.csv"


def query_selector(selector):
    """I want to do if statements rather than multiple
    try...catch for NoSuchElementException. So
    find_elements_by_css_selector is used instead of
    find_element_by_css_selector.
    """
    global driver

    elements = driver.find_elements_by_css_selector(selector)
    return elements[0] if elements else None


driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)

with open(ACCOUNTS_PATH) as file:
    accounts = [dict(r) for r in csv.DictReader(file)]

for account in accounts:
    url = account["url"]
    username = account["username"]
    password = account["password"]

    login_url = "{}/wp-login.php".format(url.rstrip("/"))

    try:
        urlopen(login_url)
    except (URLError, HTTPError) as e:
        print(e.reason, login_url)
        continue

    driver.get(login_url)
    assert "Log In" in driver.title

    form = query_selector("#loginform")
    form_action = form.get_attribute("action")

    # fix for cookie issue
    if login_url != form_action:
        driver.get(form_action)

    time.sleep(1)

    user_field = query_selector("#user_login")
    pass_field = query_selector("#user_pass")

    user_field.send_keys(username)
    pass_field.send_keys(password)
    pass_field.submit()
    driver.refresh()  # fix for cookie issue

    assert "Dashboard" in driver.title

    dashboard_url = driver.current_url
    # remove query string
    dashboard_url = dashboard_url[:dashboard_url.find("?")]

    updates_url = "{}/update-core.php".format(dashboard_url.rstrip("/"))
    driver.get(updates_url)

    assert "WordPress Updates" in driver.title

    version_button = query_selector("#upgrade[value=\"Update Now\"]")
    plugins_table = query_selector("#update-plugins-table")
    themes_table = query_selector("#update-themes-table")

    if version_button:
        version_button.click()
        driver.get(updates_url)

    if plugins_table:
        query_selector("#plugins-select-all").click()
        query_selector("#upgrade-plugins").click()
        driver.get(updates_url)

    if themes_table:
        query_selector("#themes-select-all").click()
        query_selector("#upgrade-themes").click()

    logout_link = query_selector("a[href*=\"logout\"]")
    logout_url = logout_link.get_attribute("href")
    driver.get(logout_url)
