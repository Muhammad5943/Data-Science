from urllib.request import urlretrieve

url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'

a = print(urlretrieve(url, 'winequality-white-contoh.csv'))
print(a)