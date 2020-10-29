# Thats the ways to read txt file on python

""" namaFile = 'lorem-ipsum.txt'
file = open(namaFile, mode='r')
text = file.read()
file.close()

print(text) """

# menggunakan text manager
with open('lorem-ipsum.txt','r') as file:
    print(file.read())