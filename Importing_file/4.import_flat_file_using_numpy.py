import numpy as np

filename = 'mnist.txt'
data = np.loadtxt(filename, dtype = str, delimiter = ',')

print(data)