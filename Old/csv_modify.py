from pandas import read_csv

df = read_csv("MyProtein.csv")

for column in df:
	if column != 'name':
		factor = float(df[column][0])
		for i in range(len(df[column])):
			df[column][i] = float(df[column][i])/factor

df.to_csv("experiment.csv", index = False)