import csv
from selenium import webdriver

CHROME_DRIVER_PATH = 'chromedriver_win32\\chromedriver.exe'
ACCOUNTS_PATH = 'test_accounts.csv'


def query_selector(selector):
    elements = query_selector_all(selector)
    return elements[0] if elements else None


def query_selector_all(selector):
    global driver
    return driver.find_elements_by_css_selector(selector)


driver = webdriver.Chrome(CHROME_DRIVER_PATH)

with open(ACCOUNTS_PATH) as file:
    accounts = [dict(r) for r in csv.DictReader(file)]

for account in accounts:

    url = account['url']
    username = account['username']
    password = account['password']

    login_url = '{}/wp-login.php'.format(url.rstrip('/'))
    driver.get(login_url)

    assert 'Log In' in driver.title

    form = query_selector('#loginform')
    form_action = form.get_attribute('action')

    if login_url != form_action:
        driver.get(form_action)

    user_field = query_selector('#user_login')
    pass_field = query_selector('#user_pass')

    user_field.send_keys(username)
    pass_field.send_keys(password)

    driver.implicitly_wait(1)
    pass_field.submit()

    assert 'Dashboard' in driver.title

    dashboard_url = driver.current_url
    updates_url = '{}/update-core.php'.format(dashboard_url.rstrip('/'))
    driver.get(updates_url)

    assert 'WordPress Updates' in driver.title

    button_1 = query_selector('#upgrade[value="Update Now"]')
    button_2 = query_selector('#upgrade-plugins')
    button_3 = query_selector('#upgrade-themes')

    if button_1:
        button_1.click()
        driver.get(updates_url)

    if button_2:
        query_selector('#plugins-select-all').click()
        button_2.click()
        driver.get(updates_url)

    if button_3:
        query_selector('#themes-select-all').click()
        button_3.click()

    logout_link = query_selector('a[href*="logout"]')
    logout_url = logout_link.get_attribute('href')
    driver.get(logout_url)
