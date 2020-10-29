bil = [num ** 2 for num in range(10) if num %2 == 0]
print(bil)

bil2 = [num ** 2 if num %2 == 0 else 0 for num in range(10)]
print(bil2)

pos_neg = {num: -num for num in range(10)}
print(pos_neg)
print(type(pos_neg))