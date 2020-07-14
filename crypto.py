import requests

params = {'apikey': '610D5CD6-06DA-4055-81A3-6F02D1747C59'}

# Coins
URL = "https://rest-sandbox.coinapi.io/v1/exchangerate/USD"
assets_URL = "https://rest-sandbox.coinapi.io/v1/assets"

response = requests.get(url=URL, params=params)
data = response.json()

coins = data['rates']

print("Coin Rate/USD\n")
for coin in coins:
    print(coin['asset_id_quote'], coin['rate'])

# Currency Definition
print("\nCurrency Definition\n")

assets_response = requests.get(url=assets_URL, params=params)
assets_data = assets_response.json()

coin_id = ""
coin_name = ""
for coin in assets_data:
    coin_id = coin['asset_id']
    try:
        coin_name = coin['name']
    except:
        coin_name = "N/A"
    print(coin_id, coin_name)
