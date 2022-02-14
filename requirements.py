weight = 79

constants = {
    'Energy [kcal]' : 3000,
    'Fat [g]'    : 75
}

energy = constants['Energy [kcal]']


aminoacids = {
    'Histidine [g]'     : 0.018,             
    'Isoleucine [g]'    : 0.03,
    'Leucine [g]'       : 0.059,
    'Lysine [g]'        : 0.051,
    'Methionine [g]'    : 0.016,
    'Cysteine [g]'      : 0.006,
    'Met + Cys [g]'     : 0.025,
    'Phenylalanine [g]' : 0,
    'Tyrosine [g]'      : 0,
    'Phe + Tyr [g]'     : 0.047,
    'Threonine [g]'     : 0.027,
    'Tryptophan [g]'    : 0.007,
    'Valine [g]'        : 0.039
}


ranges = {
    'SFA [g]'       : ( 0 , min( 0.05 * energy / 9 , 20 ) ),
    'MUFA [g]'      : ( 0.15 * energy / 9 , 0.2 * energy / 9 ),
    'MUFA [g]'      : ( 0 , 0.2 * energy / 9 ),
    'PUFA [g]'      : ( 0.05 * energy / 9 , 0.1 * energy / 9 ),
    'Omega 6 [g]'   : ( max( 0.05 * energy / 9 , 17 ) , 0.1 * energy / 9 ),
    'Omega 3 [g]'   : ( max( 0.006 * energy / 9 , 1.6 ) , 0.012 * energy / 9 ),
    'EPA + DHA [g]' : ( 0.5 , 0.012 * energy / 9 ),
    'EPA [g]'       : ( 0.0006 * energy / 9 , min( 0.01 * energy / 9 , 0.9 ) ),
    'DHA [g]'       : ( 0.0006 * energy / 9 , min( 0.01 * energy / 9 , 0.6 ) ),

    'Carbohydrates [g]' : ( 0.55 * energy / 4 , 0.6 * energy / 4 ),
    'Sugar [g]'         : ( 0 , 30 ),
    'Fibre [g]'         : ( max( 0.01445 * energy , 38 ) , 50 ),
    
    'Protein [g]' : ( 2.4244 * weight , 3.3 * weight ),

    'Vitamin A [RAE]' : ( 1300 , 2700 ),
    'Vitamin D [μg]' : ( 15 , 50 ),
    'Vitamin E [mg]' : ( 15 , 300 ),
    'Vitamin K [μg]' : ( 120 , 1000 ),
    'Vitamin C [mg]' : ( 155 , 1800 ),
    'Vitamin B1 (Thiamine) [mg]'         : ( max( 1.4 , 0.00041867 * energy ) , 100 ),
    'Vitamin B2 (Riboflavin) [mg]'       : ( 2 , 40 ),
    'Vitamin B3 (Niacin) [mg]'           : ( max( 16 , 0.00669876 * energy ) , 500 ),
    'Vitamin B4 (Choline) [mg]'          : ( 550 , 3000 ),
    'Vitamin B5 (Pantothenic Acid) [mg]' : ( 5 , 10000 ),
    'Vitamin B6 (Pyridoxine) [mg]'       : ( 1.7 , 80 ),
    'Vitamin B8 (Biotin) [μg]'           : ( 50 , 970 ),
    'Vitamin B9 (Folate) [μg]'           : ( 400 , 800 ),
    'Vitamin B12 (Cobalamines) [μg]'     : ( 4 , 1000 ),

    'Calcium [mg]'    : ( 1300 , 2500 ),
    'Chloride [mg]'   : ( 2300 , 3600 ),
    'Chromium [μg]'   : ( 35 , 200 ),
    'Copper [mg]'     : ( 1.6 , 8 ),
    # 'Fluoride [mg]'   : ( 3.4 , 10 ),
    'Fluoride [mg]'   : ( 0 , 10 ),
    'Iodine [μg]'     : ( 150 , 900 ),
    'Iron [mg]'       : ( 11 , 45 ),
    'Magnesium [mg]'  : ( 470 , 5000 ),
    'Manganese [mg]'  : ( 3 , 9 ),
    'Molybdenum [μg]' : ( 65 , 1700 ),
    # 'Phosphorus [mg]' : ( 1250 , 4000 ),
    'Phosphorus [mg]' : ( 0 , 4000 ),
    'Potassium [mg]'  : ( 4700 , 12500 ),
    'Selenium [μg]'   : ( 70 , 400 ),
    'Sodium [mg]'     : ( 1500 , 2300 ),
    'Zinc [mg]'       : ( 16.3 , 34 )
}