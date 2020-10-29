import requests

# url = 'http://www.omdbapi.com/?i=tt3896198&apikey=345b3c35'
url = 'http://www.omdbapi.com/?apikey=7b0c61af&t=Hackers'
r = requests.get(url)
json_data = r.json()

for key, value in json_data.items():
    print(key + ":", value)