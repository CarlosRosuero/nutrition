from pandas import read_csv
from re import sub
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException
from webdriver_manager.firefox import GeckoDriverManager


options = FirefoxOptions()

options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--no-sandbox')
options.add_argument('--headless')


driver = Firefox(service = Service(GeckoDriverManager().install()))