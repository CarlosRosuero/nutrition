from pandas import read_csv
from os import scandir


for folder in scandir('/home/carlos/nutrition/Data'):

	file = folder.path + '/prices.csv'

	prices = read_csv(file, index_col = 'name')

	prices['final'] = round((1 - prices['discount'] / 100) * prices['price'] / prices['amount'], 7)

	prices.to_csv(file)