import numpy as np

world = {
    "Afganistan":30.55, 
    "Albania":2.77, 
    "Algeria":39.21
}

# bentuk 1
""" for key, value in world.items():
    print(key + " -- " + str(value)) """

# bentuk 2
""" for k, i in world.items():
    print(k + " -- " + str(i)) """

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_height ** 2
# print(bmi)

# menampilkan perulangan dari setiap value bmi
""" for val in bmi:
    print(val) """

# menampilkan perulangan 2D dengan memaksukan 2 buah list
""" meas = np.array([np_height, np_weight])
for val in meas:
    print(val) """

# menampilksan setiam hasil perulangan dari penggabungan array 2D menjadi value sendiri-sendiri
meas = np.array([np_height, np_weight])
for val in np.nditer(meas):
    print(val)