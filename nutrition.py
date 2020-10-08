import numpy as np
from scipy.optimize import linprog
import csv

def toFloat(x):
    if x=='':
        return 0
    else:
        try:
            return float(x)
        except:
            return x

data = []
with open("Blank.csv") as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        data.append([toFloat(x) for x in row[1:]])

prices = data[2]
energy = data[3]
fat = data[4]
saturates = data[5]
carbs = data[6]
fibre = data[7]
protein = data[8]
salt = data[9]
vitb12 = data[10]
calcium = data[11]
omega3 = data[12]
thiamin = data[13]
potassium = data[14]
vita = data[15]
vitc = data[16]

nutrients1 = [fat, saturates, carbs, protein, salt, calcium, omega3, vita, vitc]

nutrients2 = [[-x for x in row] for row in [fat, carbs, fibre, protein, omega3, thiamin, potassium, vita, vitc]]

nutrients = nutrients1 + nutrients2

print(nutrients)

weight = 76
energy_goal = 16*2.204*weight
fat_min = .2*energy_goal/9
fat_max = 75
saturates_max = min(.05*energy_goal/9,20)
carbs_min = .45*energy_goal/4
carbs_max = .6*energy_goal/4
fibre_min = 38
protein_min = 2.4244*weight
protein_max = 3.3*weight
salt_max = 6
calcium_max = 2500
omega3_min = max(.006*energy_goal/9, 1.6)
omega3_max = .012*energy_goal/9
thiamin_min = 1.4
potassium_min = 4700
vita_min = 1300
vita_max = 2700
vitc_min = 125
vitc_max = 1800

limits = [fat_max,saturates_max,carbs_max,protein_max,salt_max,calcium_max,omega3_max,vita_max, vitc_max, -fat_min,-carbs_min,-fibre_min,-protein_min,-omega3_min,-thiamin_min,-potassium_min,-vita_min, -vitc_min]

print(limits)

print(len(nutrients))
print(len(limits))

result = linprog(prices, A_ub=np.array(nutrients), b_ub=np.array(limits), A_eq=[data[3]], b_eq=np.array([energy_goal]))

print(result)

print(tuple(zip(result.x, data[0])))