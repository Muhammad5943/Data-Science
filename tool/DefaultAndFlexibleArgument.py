# Default Arrgument
""" def power(nomor, pow=1):
    
    hasil = nomor ** pow
    return hasil

print(power(9,2))
print(power(9)) """

# Flexible Argumment
def add_all(*args):
    sum_all = 0
    for angka in args:
        sum_all += angka
    return sum_all

print(add_all(1,2,3))