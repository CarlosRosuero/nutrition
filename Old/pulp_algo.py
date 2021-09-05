from pulp import LpProblem, LpStatus, lpSum, LpVariable, LpInteger, getSolver, LpConstraint, LpConstraintLE, LpConstraintGE
from csv import reader
from requirements import requirements, energy, fat, toFloat

model = LpProblem('Nutrition')

data = []

rows = reader(open('units.csv'))

for row in rows:
    data.append([toFloat(x) for x in row])

items = [''.join(char for char in item if char.isalpha()) for item in data[0][1:]]

objects = []

for item in items:
    tmp = LpVariable(item, 0, None, LpInteger)
    objects.append(tmp)

model += lpSum([a * b for (a,b) in zip(data[1][1:], objects)])

model += LpConstraint(lpSum([a * b for (a,b) in zip(data[2][1:], objects)]) == energy, name = 'Energy')
model += LpConstraint(lpSum([a * b for (a,b) in zip(data[3][1:], objects)]) == fat, name = 'Fat')

for nutrient in data[4:16] + data[29:-1]:
    model += LpConstraint(lpSum([a * b for (a,b) in zip(nutrient[1:], objects)]), LpConstraintLE, 'Maximum ' + nutrient[0], requirements[nutrient[0]][1])
    model += LpConstraint(lpSum([a * b for (a,b) in zip(nutrient[1:], objects)]), LpConstraintGE, 'Minimum ' + nutrient[0], requirements[nutrient[0]][0])

for nutrient in data[16:29]:
    model += LpConstraint(lpSum([a * b for (a,b) in zip(nutrient[1:], objects)]) - lpSum([requirements[nutrient[0]] * a * b for (a,b) in zip(data[15][1:], objects)]), LpConstraintGE, 'Minimum ' + nutrient[0], 0)

print(model)

model.solve(getSolver('GUROBI'))

print("Status: ", LpStatus[model.status])

for v in model.variables():
    if v.varValue > 0:
        print(v.name, '=', int(v.varValue))