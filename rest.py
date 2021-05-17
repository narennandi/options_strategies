import robin_stocks
import robin_stocks.robinhood as r
import pandas as pd
import numpy as np
import configs

class Rest(object):
    def __init__(self):
        login = r.login(configs.username, configs.pwd)

    def get_option_data(self, ticker, expirationDate, optionType):
        OptionData = r.find_options_by_expiration(
            ticker, 
            expirationDate=expirationDate,
            optionType=optionType
        )
        return OptionData
    
    def get_latest_price(self, ticker):
        res = r.stocks.get_latest_price(ticker, priceType=None, includeExtendedHours=True)
        return float(res[0])

    def find_nearest(self, array, value):
        array = np.asarray(array)
        idx = (np.abs(array - value)).argmin()
        return array[idx], idx 
    
