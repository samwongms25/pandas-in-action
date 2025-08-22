
import pandas as pd
import numpy as np
from numpy.ma.core import squeeze

a = pd.read_csv('google_stocks.csv', parse_dates=['Date'], index_col = 'Close').squeeze("columns")

print(a.value_counts(normalize=False).head(5), "\n\n")
print(a.value_counts(normalize=True).head(5), "\n\n")
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print(a.value_counts(normalize=False).tail(5), "\n\n")
print(a.value_counts(normalize=True).tail(5), "\n\n")
print("****************************************************")
print(a.sort_values().head(10), '\n\n')
print(a.sort_values().tail(10), "\n\n")
print("####################################################")
print("\n", "min", a.min(), "\n","max", a.max(), "\n")
