# cara 1
""" nums = [12,8,21,3,16]
new_nums = []
for num in nums:
    new_nums.append(num + 1)

print(new_nums) """

# cara 2
nums = [12,8,21,3,16]
new_nums = [num + 1 for num in nums]
print(new_nums)

# menampilkan data berdasarkan range data
result = [num for num in range(11)]
print(result)