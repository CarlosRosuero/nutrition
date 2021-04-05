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

weight = 73

energy = 3000

limits_dict = {
    'fat' : ( 0.2 * energy / 9 , 75 ),                                   # 0.89  0
    'sfa' : ( 0 , min( 0.05 * energy / 9 , 20 ) ),                       # 0     0
    # 'mufa' : ( 0.15 * energy / 9 , 0.2 * energy / 9 ),
    'mufa' : ( 0 , 0.2 * energy / 9 ),                                   # 0     0
    'pufa' : ( 0.05 * energy / 9 , 0.1 * energy / 9 ),                   # 0.49  0
    # 'omega6' : ( max( 0.05 * energy / 9 , 17 ) , 0.1 * energy / 9 ),   
    'omega6' : ( 0 , 0.1 * energy / 9 ),                                 # 0     0
    'omega3' : ( max( 0.006 * energy / 9 , 1.6 ) , 0.012 * energy / 9 ), # 0     0.18
    'epa_dha' : ( 0.5 , 0.012 * energy / 9 ),                            # 0     0
    'epa' : ( 0.0006 * energy / 9 , min( 0.01 * energy / 9 , 0.9 ) ),    # 0     0
    'dha' : ( 0.0006 * energy / 9 , min( 0.01 * energy / 9 , 0.6 ) ),    # 0     0

    'carbs' : ( 0.55 * energy / 4 , 0.6 * energy / 4 ),                  # 1.05  0
    'sugar' : ( 0 , 30 ),                                                # 0     0
    'fibre' : ( max( 0.01445 * energy , 38 ) , 50 ),                     # 1.03  0
    
    'protein' : ( 2.4244 * weight , 3.3 * weight ),                      # 0.52  0
    # 'histidine' : ( 0.018 * 3.3 * weight , 3.3 * weight ),             
    'histidine' : ( 0 , 3.3 * weight ),
    'isoleucine' : ( 0.03 * 3.3 * weight , 3.3 * weight ),
    'leucine' : ( 0.059 * 3.3 * weight , 3.3 * weight ),
    'lysine' : ( 0.051 * 3.3 * weight , 3.3 * weight ),
    'methionine' : ( 0.016 * 3.3 * weight , 3.3 * weight ),
    'cysteine' : ( 0.006 * 3.3 * weight , 3.3 * weight ),
    'met_cys' : ( 0.025 * 3.3 * weight , 3.3 * weight ),                 # Can save 0.36
    'phenylalanine' : ( 0 , 3.3 * weight ),
    'tyrosine' : ( 0 , 3.3 * weight ),
    'phe_tyr' : ( 0.047 * 3.3 * weight , 3.3 * weight ),
    'threonine' : ( 0.027 * 3.3 * weight , 3.3 * weight ),
    'tryptophan' : ( 0.007 * 3.3 * weight , 3.3 * weight ),
    'valine' : ( 0.039 * 3.3 * weight , 3.3 * weight ),

    'vitamina' : ( 1300 , 2700 ),
    'vitamind' : ( 15 , 50 ),
    'vitamine' : ( 15 , 300 ),
    'vitamink' : ( 120 , 1000 ),                                         # Can save 0.03
    'vitaminc' : ( 155 , 1800 ),
    'vitaminb1' : ( max( 1.4 , 0.00041867 * energy ) , 100 ),
    'vitaminb2' : ( 2 , 40 ),
    'vitaminb3' : ( max( 16 , 0.00669876 * energy ) , 500 ),
    'vitaminb4' : ( 550 , 3000 ),                                        # Can save 0.36
    'vitaminb5' : ( 5 , 10000 ),
    'vitaminb6' : ( 1.7 , 80 ),
    'vitaminb8' : ( 50 , 970 ),
    'vitaminb9' : ( 400 , 800 ),
    'vitaminb12' : ( 4 , 1000 ),

    'calcium' : ( 1300 , 2500 ),
    'chloride' : ( 2300 , 3600 ),
    'chromium' : ( 35 , 200 ),
    'copper' : ( 1.6 , 8 ),
    # 'fluoride' : ( 3.4 , 10 ),                                         # Can save 1.24
    'fluoride' : ( 0 , 10 ),
    'iodine' : ( 150 , 900 ),
    'iron' : ( 11 , 45 ),
    'magnesium' : ( 470 , 5000 ),
    'manganese' : ( 3 , 9 ),
    'molybdenum' : ( 65 , 1700 ),
    # 'phosphorus' : ( 1250 , 4000 ),                                    # Can save 1.62
    'phosphorus' : ( 0 , 4000 ),
    'potassium' : ( 4700 , 12500 ),                                      # Can save 0.41
    'selenium' : ( 70 , 400 ),
    'sodium' : ( 1500 , 2300 ),
    'zinc' : ( 16.3 , 34 )
}

limits = [ limits_dict[key][1] for key in limits_dict ] + [ -limits_dict[key][0] for key in limits_dict ]

for key in limits_dict:
    print(key + str(limits_dict[key]))

print(len(nutrients))
print(len(limits))

result = linprog(np.array(prices), A_ub=np.array(nutrients), b_ub=np.array(limits), A_eq=[data[3][1:]], b_eq=np.array(energy))

for pair in zip(result.x, data[0][1:], data[2][1:]):
    if pair[0] > 0.01:
        print(pair)

print(result.success)

print(result.fun)