# global scope
hasil = 10

def kotak(nilai1, nilai2):
    """ 
    Scope 
    local scope
    """
    hasil = nilai1 ** nilai2
    return hasil

# print(kotak(3, 2))
# print(hasil)

def kotak(nilai):
    nilai_baru2 = hasil ** 2
    return nilai_baru2

print(kotak(3))