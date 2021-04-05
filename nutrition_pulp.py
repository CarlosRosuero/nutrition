from pulp import LpMaximize, LpMinimize, LpProblem, LpStatus, lpSum, LpVariable
import csv
from string import punctuation

def toFloat(x):
    if x=='':
        return 0
    else:
        try:
            return float(x)
        except:
            return x

model = LpProblem( name = "nutrition", sense = LpMinimize )

data = []
with open("MyProtein.csv") as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        data.append([toFloat(x) for x in row])

print(data[0])

items = [''.join(char for char in item if char.isalpha()) for item in data[0][1:]]

print(items)

objects = []

for item in items:
    exec(item + " = LpVariable(item, 0, cat = \"Integer\")")
    exec("objects.append(" + item + ")")

for nutrient in data[4:-1]:
    model += (lpSum([a * b for (a,b) in zip(nutrient[1:], objects)]) <= , nutrient[0])

print(model)