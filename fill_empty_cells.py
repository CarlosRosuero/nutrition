from pandas import read_csv
from os import scandir


for folder in scandir('/home/carlos/nutrition/Data'):
	file = folder.path + '/nutrients.csv'
	read_csv(file).fillna(0).to_csv(file, index = False)