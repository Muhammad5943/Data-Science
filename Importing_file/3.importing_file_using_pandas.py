import pandas as pd

filename = 'titanic.csv'
data = pd.read_csv(filename)
print(data.head())