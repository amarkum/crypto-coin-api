import investpy
import xlsxwriter

# init
params = {'apikey': '610D5CD6-06DA-4055-81A3-6F02D1747C59'}

workbook_to_write = xlsxwriter.Workbook("coins.xlsx")
sheet_one = workbook_to_write.add_worksheet("Sheet1")
sheet_two = workbook_to_write.add_worksheet("Sheet2")

top_100_coin_dict = {'BTC': 'Bitcoin', 'ETH': 'Ethereum', 'XRP': 'XRP', 'USDT': 'Tether', 'BCH': 'Bitcoin Cash',
                     'LTC': 'Litecoin',
                     'EOS': 'EOS', 'BNB': 'Binance Coin', 'BSV': 'Bitcoin SV', 'XLM': 'Stellar', 'TRX': 'TRON',
                     'XTZ': 'Tezos',
                     'ADA': 'Cardano', 'LEO': 'LEO', 'ATOM': 'Cosmos', 'XMR': 'Monero', 'HT': 'Huobi Token',
                     'LINK': 'Chainlink',
                     'NEO': 'Neo', 'ETC': 'Ethereum Classic', 'USDC': 'USD Coin', 'HEDG': 'HedgeTrade', 'MIOTA': 'IOTA',
                     'MKR': 'Maker', 'CRO': 'Crypto.com Coin', 'DASH': 'Dash', 'ONT': 'Ontology', 'VET': 'VeChain',
                     'XEM': 'NEM',
                     'BAT': 'Basic Attention Token', 'DOGE': 'Dogecoin', 'ZEC': 'Zcash', 'PAX': 'Paxos Standard',
                     'FTT': 'FTX Token',
                     'SNX': 'Synthetix Network Token', 'INB': 'Insight Chain', 'DCR': 'Decred', 'QTUM': 'Qtum',
                     'TUSD': 'TrueUSD',
                     'THR': 'ThoreCoin', 'THX': 'ThoreNextT', 'ZRX': '0x', 'RVN': 'Ravencoin', 'ALGO': 'Algorand',
                     'PZM': 'PRIZM',
                     'CNX': 'Cryptonex', 'BDX': 'Beldex', 'HOT': 'Holo', 'CENNZ': 'Centrality', 'OKB': 'OKB',
                     'REP': 'Augur',
                     'WAVES': 'Waves', 'SEELE': 'Seele', 'BTG': 'Bitcoin Gold', 'OMG': 'OmiseGO', 'LUNA': 'Terra',
                     'ZB': 'ZB Token',
                     'NANO': 'Nano', 'XIN': 'Mixin', 'ABBC': 'ABBC Coin', 'KCS': 'KuCoin Shares', 'THETA': 'THETA',
                     'KBC': 'Karatgold Coin', 'MOF': 'Molecular Future', 'LSK': 'Lisk', 'DGB': 'DigiByte',
                     'BTM': 'Bytom',
                     'SXP': 'Swipe', 'ENJ': 'Enjin Coin', 'BCD': 'Bitcoin Diamond', 'MCO': 'MCO', 'GAP': 'GAPS',
                     'KMD': 'Komodo',
                     'BTT': 'BitTorrent', 'ZEN': 'Horizen', 'IOST': 'IOST', 'ICX': 'ICON', 'VSYS': 'v.systems',
                     'XVG': 'Verge',
                     'SC': 'Siacoin', 'NOAH': 'Noah Coin', 'NEXO': 'Nexo', 'EKT': 'EDUCare', 'BCN': 'Bytecoin',
                     'MONA': 'MonaCoin',
                     'NRG': 'Energi', 'HC': 'HyperCash', 'STEEM': 'Steem', 'ZIL': 'Zilliqa', 'DX': 'DxChain Token',
                     'QC': 'Qcash',
                     'QNT': 'Quant', 'SLV': 'Silverway', 'BTS': 'BitShares', 'SAI': 'Single Collateral DAI',
                     'FXC': 'Flexacoin',
                     'ARDR': 'Ardor', 'AE': 'Aeternity', 'XET': 'ETERNAL TOKEN'}

data = investpy.get_crypto_historical_data(crypto='ABBC Coin', from_date='16/07/2019', to_date='16/07/2020',
                                           as_json=True)

# write all top 100 coin name
coin_column = 1
for key, val in top_100_coin_dict.items():
    print(key, val)

    sheet_two.write(0, 0, "Symbol")
    sheet_two.write(0, 1, "Name")

    sheet_two.write(coin_column, 0, key)
    sheet_two.write(coin_column, 1, val)

    coin_column += 1

workbook_to_write.close()

# CoinAPI Source Code

# coins - trade rate
# URL = "https://rest.coinapi.io/v1/exchangerate/USD"
#
# response = requests.get(url=URL, params=params)
# data = response.json()
#
# coins = data['rates']
#
# counter = 1
# sheet_one.write(0, 0, "Date")
#
# current_time = datetime.now().strftime("%m-%d-%Y")
# sheet_one.write(1, 0, current_time)
#
# for coin in coins:
#     sheet_one.write(0, counter, coin['asset_id_quote'])
#     sheet_one.write(1, counter, coin['rate'])
#     counter += 1

# print all assets definition
# assets_URL = "https://rest.coinapi.io/v1/assets"
#
# assets_response = requests.get(url=assets_URL, params=params)
# assets_data = assets_response.json()
#
# coin_id = ""
# coin_name = ""
#
# for coin in assets_data:
#
#     coin_id = coin['asset_id']
#     try:
#         coin_name = coin['name']
#     except:
#         coin_name = "N/A"
#     print(coin_id, coin_name)
