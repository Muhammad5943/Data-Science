import pandas as pd
import numpy as np

dict = {
    "country": ["Brazil","Rusia","India","China","South Africa"],
    "capital": ["Brasilia","Moscow","New Delhi","Beijing","Pretoria"],
    "area": [8.516, 17.100, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
}

brics = pd.DataFrame(dict)

# menambah kolom lable
brics.index = ["BR", "RU", "IN", "CH", "SA"]

brics = pd.read_csv("/home/muhammad/apps/Learn_python/DataScience/brics.csv", index_col = 0)
brics_inde = brics[["country", "area", "population"]]

is_huge = brics["area"] > 8

between_8_10 = np.logical_and(is_huge, brics["area"] < 10)

# print(is_huge)
# print(brics[is_huge])
print(between_8_10)
print(brics[between_8_10])