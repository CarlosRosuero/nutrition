from pandas import read_csv

filename = 'Data/MyProtein/prices.csv'

df = read_csv(filename, index_col = 'name')

for name in df.index:
	df.loc[name, 'final'] = round((1 - df.loc[name, 'discount'] / 100) * df.loc[name, 'rrp'] / df.loc[name, 'amount'], 7)

df.to_csv(filename)