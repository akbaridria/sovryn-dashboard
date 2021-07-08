import requests
url = 'http://127.0.0.1:5000/hello/'
_r = requests.get(url)
print(_r.json())
