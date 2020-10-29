import pandas as pd

brics = pd.read_csv("/home/muhammad/apps/Learn_python/DataScience/brics.csv", index_col = 0)
# print(brics)

# menampilkan semua data dari tabel
""" for lab, row in brics.iterrows():
    print(lab)
    print(row) """

# menampilkan data tertentu dari table
""" for lab, row in brics.iterrows():
    print(lab + ": " + row["capital"]) """

# menambahkan kolom tabel 
for lab, row in brics.iterrows():
    brics.loc[lab, "panjang_karakter"] = len(row["country"])
print(brics)

