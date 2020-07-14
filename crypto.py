import requests

URL = "https://rest-sandbox.coinapi.io/v1/exchangerate/USD"
params = {'apikey': '610D5CD6-06DA-4055-81A3-6F02D1747C59'}

response = requests.get(url=URL, params=params)
data = response.json()

coins = data['rates']

print("Currencies")
for coin in coins:
    print(coin['asset_id_quote'])

