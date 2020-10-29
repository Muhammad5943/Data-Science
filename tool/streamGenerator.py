def read_large_file(file_object):
    """ A generator function to read file lazily """

    while True:
        # read a line from the file
        data = file_object.readline()

        # break if this the end of the file
        if not data:
            break

        # yield data of the line
        yield data

# initiate an empty dictionary
counts_dict = {}

# open connection to the file
with open("/home/muhammad/apps/Learn_python/DataScience/tool/world_dev_ind.csv") as file:
    
    for line in read_large_file(file):
        row = line.split(',')
        first_col = row[0]

        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1

print(counts_dict)