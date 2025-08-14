import requests
# pip install requests

r = requests.get("http://ctf.neimark-it.ru:20204/ecb_oracle/encrypt/12/")

print(r.text)

