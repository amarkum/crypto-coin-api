import requests

params = {'apikey': '610D5CD6-06DA-4055-81A3-6F02D1747C59'}

# Coins
URL = "https://rest.coinapi.io/v1/exchangerate/USD"

response = requests.get(url=URL, params=params)
data = response.json()

coins = data['rates']

counter = 1
print("Coin Rate/USD\n")
for coin in coins:
    print(counter, coin['asset_id_quote'], coin['rate'])
    counter = counter + 1

# Currency Definition
print("\nCurrency Definition\n")

assets_URL = "https://rest.coinapi.io/v1/assets"

assets_response = requests.get(url=assets_URL, params=params)
assets_data = assets_response.json()

coin_id = ""
coin_name = ""
total_crypto_currency = 0
for coin in assets_data:
    is_crypto = coin['type_is_crypto']
    if is_crypto == 1:
        total_crypto_currency += 1

    coin_id = coin['asset_id']
    try:
        coin_name = coin['name']
    except:
        coin_name = "N/A"
    print(coin_id, coin_name)

print("Total Crypto Currency", total_crypto_currency)
