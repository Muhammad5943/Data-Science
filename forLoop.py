fam = [1.73, 1.68, 1.71, 1.89]
""" print(fam)
print(fam[0])
print(fam[1])
print(fam[2])
print(fam[3]) """

for height in fam:
    print(height)

for index, height in enumerate(fam):
    print("index" + "[" + str(index) + "]" + ": " + str(height))