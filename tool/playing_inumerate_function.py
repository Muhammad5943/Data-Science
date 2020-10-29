avenger = ["Hawkeye","Batman","Iron man","Spiderman","Superman"]

e = enumerate(avenger)
print(type(e))

""" e_list = list(e)
print(e_list) """

# index dari angka 0
""" for i, value in e:
    print(i,value) """

# index dari angka 10
for i,item in enumerate(avenger, start=10):
    print(i,item)

names = ["Borton","Banner","Stark","Parker","Karl"]

# combine 2 list
for z1, z2 in zip(avenger, names):
    print(z1, z2)

# combine 2 list with different output
z = zip(avenger, names)
print(*z)