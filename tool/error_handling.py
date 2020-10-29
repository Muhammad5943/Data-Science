def kotak(x):
    try:
        return x ** (0.5)
    except:
        print("x harus integer ato float")

print(kotak(4))
print(kotak("hai"))