import pandas as pd
import numpy as np


data_file = pd.read_csv("data.csv")
matching_file = pd.read_csv("matchings.csv")
currencies_file = pd.read_csv("currencies.csv")
#print(data_file)
#print(currencies_file)
#print(matching_file)

merged = pd.merge(matching_file, data_file, on='matching_id') #usecols=['price','currency']
print(merged)
merged2 = pd.merge(merged,currencies_file, on='currency')
#print(merged2)

merged2['TotalCostInPLN']= merged2['ratio'] * merged2['price'] * merged2['quantity']
print(type(merged2))
grouped = merged2.groupby('matching_id')
print(grouped)
#grouped = grouped.agg("TotalCostInPLN",lambda(x):  )