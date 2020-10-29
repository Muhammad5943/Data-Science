# looping example
""" employees = ["Alan","Satria","Fony","Khairin","Aby"]

for employee in employees:
    print(employee)

for letter in "NIOMIC":
    print(letter) """

# Iteration
word = "Da"
it = iter(word)

print(next(it))
print(next(it))

Word = "NIOMIC"
ite = iter(Word)

print(*ite)

# to display key and value you must add items() in the end of the data variable
dict = {
    "country": "Indonesia",
    "capital": "Jakarta"
}

for k, v in dict.items():
    print(k + " : " + v)

file = open("/home/muhammad/apps/Learn_python/DataScience/tool/file.txt")
it = iter(file)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) // it will throw an error