# [2 * num for num in range(10)] (general list)
# (2 * num for num in range(10)) (generator expression)

""" generator = (2 * num for num in range(6))
print(generator)
"""
# result = (num for num in range(6))
# hasil vertikal (kurang rapi)
""" for num in result:
    print(num) """

# hasil horizontal (rapi)
""" listType = list(result)
print(listType) """

""" print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result)) """

# cara tidak efektif untuk membuat iterator dengan value yang besar
# [num for num in range(10 ** 10000000)] (meemakan waktu sang sangat lama)

# cara yang efektif adalah menggunakan generatot expression
""" generator_exp = (num for num in range(10 ** 10000000))
print(generator_exp) """

# memunculkan nilai dari generator expression
""" even_nums = (nums for nums in range(10) if nums %2 == 0)
print(list(even_nums)) """

def num_sequence(n):
    """ generate values from 0 to n """
    i = 0
    while i + 1 < n:
        yield i
        i += 1

result = num_sequence(6)
print(type(result))

for item in result:
    print(item)


