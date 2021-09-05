import numpy as np
from scipy.optimize import linprog
import csv
from requirements import requirements, energy

def toFloat(x):
    if x=='':
        return 0
    else:
        try:
            return float(x)
        except:
            return x

data = []
with open("MyProtein.csv") as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        data.append([toFloat(x) for x in row])

nutrients_max = []

for row in data[4:-1]:
    exec(row[0] + ' = row[1:]')
    exec('nutrients_max.append(' + row[0] + ')')

nutrients_min = [[-x for x in row] for row in nutrients_max]

nutrients = nutrients_max + nutrients_min

prices = data[2][1:]

limits = [ requirements[key][1] for key in requirements ] + [ -requirements[key][0] for key in requirements ]

for key in requirements:
    print(key + str(requirements[key]))

print(len(nutrients))
print(len(limits))

result = linprog(np.array(prices), A_ub=np.array(nutrients), b_ub=np.array(limits), A_eq=[data[3][1:]], b_eq=np.array(energy))

for pair in zip(result.x, data[0][1:], data[2][1:]):
    if pair[0] > 0.01:
        print(pair)

print(result.success)

print(result.fun)