import requests
from bs4 import BeautifulSoup
import selenium

categories = [
    "protein",
    "healthy-food-drinks",
    "vitamins-minerals",
    "amino-acids",
    "carbohydrates"
]

urls = ["https://www.myprotein.com/nutrition/" + category + ".list?pageNumber=" + str(page) for page in [1,2,3] for category in categories]
print(urls)

def getMPLinks(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    items = soup.find_all('li', class_ = 'productListProducts_product')
    return [ item.find('a')['href'] for item in items ]

print([item for category in list(map(getMPLinks, urls)) for item in category])