import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(url)

print(response.status_code)
print(response.text)