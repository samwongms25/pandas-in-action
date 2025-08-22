import pandas as pd
import numpy as np


a = pd.read_csv('google_stocks.csv', parse_dates=['Date'], index_col = 'Date').squeeze("columns")
print(a, "\n")
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

print(a.value_counts(normalize=True).head(15), "\n\n")
print(a.value_counts(normalize=False).head(15), "\n\n")
print(a.value_counts(normalize=True).tail(15), "\n\n")
print(a.value_counts(normalize=False).tail(15), "\n\n")
print("****************************************************")

print("\n", "min", a.min(), "\n", "max", a.max(), "\n")
#b = [0, 200, 400, 600, 800, 1000, 1200, 1400]
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
df = pd.DataFrame(a)
print("\n", df['Close'].value_counts(bins=3))
print("\n", df['Close'].value_counts(bins=3, sort = False), "\n")




