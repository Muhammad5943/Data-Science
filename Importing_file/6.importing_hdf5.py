import h5py

filename = 'H-H1_LOSC_4_V1-815411200-4096.hdf5'
data = h5py.File(filename, 'r')
print(type(data))

# untuk menampilkan data pada file
for key in data.keys():
    print(key)

# untuk menampilkan data setiap index
for key in data['meta'].keys():
    print(key)

# print(data['meta']['Description'].value)
print(data['meta']['Description'].value,data['meta']['Detector'].value)

