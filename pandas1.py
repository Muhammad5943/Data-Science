import pandas as pd

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
# print(brics_inde)
# print(brics[1:4])

# Menampilkan semua data pada tabel menggunakan label
""" print("menampulkan data berdasarkan index/ lable")
local = brics.loc[["RU","IN","CH"]]
print(local)  """

# Menampilkan baris dan kolom tertentu dari table
""" local = brics.loc[["RU","IN","CH"],["country","capital"]]
print(local) """

# Menampilkan baris dan kolom menggunakan index yang ada pada kolom
# (object).ilog[[baris],[kolom]]
local = brics.iloc[[1,2],[1,2]]
print(local)
