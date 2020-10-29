import numpy as np

np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])

bmi = np_weight / np_height ** 2
print(bmi)

print("Menampilkan nilai lebih dari 23 (hasil boolean)")
print(bmi > 23)

print("Menampilkan nilai lebih dari 23")
print(bmi[bmi > 23])

logic_and = np.logical_and(bmi > 21, bmi < 22)
print(logic_and)

a = bmi[np.logical_and(bmi > 21, bmi < 22)]
print(a)