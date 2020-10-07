import numpy as np
from scipy.optimize import linprog
import csv

prices = np.array(csv.reader("Blank.numbers"))