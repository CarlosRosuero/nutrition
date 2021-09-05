from pulp import LpProblem, lpSum, LpVariable, LpInteger, getSolver, LpConstraint, LpConstraintLE, LpConstraintGE
from pandas import read_csv
from requirements import constants, ranges, aminoacids


nutrients = read_csv('Data/MyProtein/nutrients.csv', index_col = 'Name')

prices = read_csv('Data/MyProtein/prices.csv', index_col = 'name')

objects = [LpVariable(item, 0, None, LpInteger) for item in nutrients.index]

model = LpProblem('Nutrition') 

model += lpSum([float(a) * b for a,b in zip(prices['final'], objects)])

for nutrient in nutrients:
	if nutrient in constants:
		model += LpConstraint(lpSum([a * b for a,b in zip(nutrients[nutrient], objects)]) == constants[nutrient], name = nutrient)
	elif nutrient in aminoacids:
		model += LpConstraint(lpSum([a * b for a,b in zip(nutrients[nutrient], objects)]) - lpSum([aminoacids[nutrient] * a * b for a,b in zip(nutrients['Protein [g]'], objects)]), LpConstraintGE, 'Minimum ' + nutrient, 0)
	elif nutrient in ranges:
		model += LpConstraint(lpSum([a * b for a,b in zip(nutrients[nutrient], objects)]), LpConstraintLE, 'Maximum ' + nutrient, ranges[nutrient][1])
		model += LpConstraint(lpSum([a * b for a,b in zip(nutrients[nutrient], objects)]), LpConstraintGE, 'Minimum ' + nutrient, ranges[nutrient][0])
	else:
		print('Error with', nutrient)


# print(model)

model.solve(getSolver('GUROBI'))

for v in model.variables():
    if v.varValue > 0:
        print(v.name, '=', int(v.varValue))