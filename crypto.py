import requests
import xlsxwriter
from datetime import datetime

# init
params = {'apikey': '610D5CD6-06DA-4055-81A3-6F02D1747C59'}

workbook_to_write = xlsxwriter.Workbook("coins.xlsx")
sheet_one = workbook_to_write.add_worksheet("Sheet1")
sheet_two = workbook_to_write.add_worksheet("Sheet2")

# coins - trade rate
URL = "https://rest.coinapi.io/v1/exchangerate/USD"

response = requests.get(url=URL, params=params)
data = response.json()

coins = data['rates']

counter = 1
sheet_one.write(0, 0, "Date")

current_time = datetime.now()
sheet_one.write(1, 0, "current_time")

for coin in coins:
    sheet_one.write(0, counter, coin['asset_id_quote'])
    sheet_one.write(1, counter, coin['rate'])
    counter += 1

# current definition
assets_URL = "https://rest.coinapi.io/v1/assets"

assets_response = requests.get(url=assets_URL, params=params)
assets_data = assets_response.json()

coin_id = ""
coin_name = ""
coin_column = 0
for coin in assets_data:
    # is_crypto = coin['type_is_crypto']
    # if is_crypto == 1:
    #     total_crypto_currency += 1

    coin_id = coin['asset_id']
    try:
        coin_name = coin['name']
    except:
        coin_name = "N/A"

    sheet_two.write(coin_column, 0, coin_id)
    sheet_two.write(coin_column, 1, coin_name)

    coin_column += 1

workbook_to_write.close()
