from pandas import read_csv
from requests import get
from bs4 import BeautifulSoup
from re import sub
from selenium.webdriver import ChromeOptions, Chrome
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException


options = ChromeOptions()

options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
# options.add_argument('--headless')

driver = Chrome(options = options)

df = read_csv('~/nutrition/Data/MyProtein/prices.csv', index_col = 'name')

for name in df.index:
	driver.get('https://www.myprotein.com/' + df.loc[name, 'link'])

	sizes = {int(1000 * float(size.get_attribute('textContent').split()[0])) if size.get_attribute('textContent').split()[1] == 'kg' else int(size.get_attribute('textContent').split()[0]) : size for size in driver.find_elements_by_class_name('athenaProductVariations_box')}
	biggest = sizes[max(sizes)]

	clicked = False

	while not clicked:
		try:
			biggest.click()
			df.loc[name, 'price'] = sub('[^\.0-9]+', '', driver.find_element_by_class_name('productPrice_price').text)
			clicked = True
		except (ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException):
			
			try:
				driver.find_element_by_class_name('epopupClose').click()
			except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException):
				pass
			try:
				driver.find_element_by_class_name('emailReengagement').click()
			except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException):
				pass
			try:
				driver.find_element_by_class_name('cookie_modal_button').click()
			except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException):
				pass




	# df.loc[name, 'price'] = sub('[^\.0-9]+', '', BeautifulSoup(get('https://www.myprotein.com/' + df.loc[name, 'link']).content, 'lxml').find('p', class_ = 'productPrice_price').text)

# df.to_csv('~/nutrition/Data/MyProtein/prices.csv')