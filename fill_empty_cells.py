from pandas import read_csv
from tkinter.filedialog import askopenfilename

file = '~/nutrition/Data/Aldi/nutrients.csv'

read_csv(file).fillna(0).to_csv(file, index = False)