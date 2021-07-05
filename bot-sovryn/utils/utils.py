import requests
import math
import time

class utils :
    
    def __init(self) :
        pass

    def insert_swap_transaction(data) :
        return data
    
    def get_gecko_price(base, id, date) :
        url_gecko = base + "coins/" + id + "/history?date=" + date
        print(url_gecko)
        _r = requests.get(url_gecko)
        if _r.status_code == 200 :
           _data = _r.json()

           return 1, _data['market_data']['current_price']['usd']
        else :
           return 0, 0
    
    def get_a_transaction_covalent(url, date) :
        url_gecko_bitcoin = "https://api.coingecko.com/api/v3/coins/bitcoin/history?date=" + date
        _r = requests.get(url)
        time.sleep(1)
        _r_gecko = requests.get(url_gecko_bitcoin)
        if _r.status_code == 200 and _r_gecko.status_code == 200:
            _data = _r.json()
            _data_gecko = _r_gecko.json()
            _address = _data['data']['items'][0]['from_address']
            _total_gas_spent = float(_data_gecko['market_data']['current_price']['usd']) * ((int(_data['data']['items'][0]['gas_price'])/math.pow(10,18))*int(_data['data']['items'][0]['gas_spent']))
            return 1, _address, _total_gas_spent
        else :
            return 0, 0, 0