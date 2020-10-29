import pandas as pd

# cara 1
""" result = []

for chunk in pd.read_csv("/home/muhammad/apps/Learn_python/DataScience/tool/data.csv", chunksize = 1000):
    result.append(sum(chunk['x']))

total = sum(result)
print(total) """

# cara 2
total = 0

for chunk in pd.read_csv("/home/muhammad/apps/Learn_python/DataScience/tool/data.csv", chunksize = 1000):
    total += sum(chunk["x"])

print(total)
