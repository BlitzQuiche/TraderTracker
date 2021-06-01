from .keys import APIKEY, SECRETKEY
from binance import Client

class binanceBot:
    
    def __init__(self):
        self.client = Client(APIKEY, SECRETKEY)

    def get_price(self, symbol):
        return self.client.get_avg_price(symbol = symbol)

    def get_trades(self, ticker):
        return self.client.get_my_trades(symbol = ticker)

    def get_asset_bal(self, asset):
        return self.client.get_asset_balance(asset = asset)