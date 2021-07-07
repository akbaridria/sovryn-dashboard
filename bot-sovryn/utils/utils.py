import requests
import math
import time
from . import database


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
    
    def process_data_mint( self, data_mint, api_key) :
        _data_to_sent_lending = {}
        for i in data_mint['data']['items'] :
            _data_to_sent_lending['tx_hash'] = i['tx_hash']
            _data_to_sent_lending['block'] = i['block_height']
            _data_to_sent_lending['date'] = i['block_signed_at']
            _data_to_sent_lending['ticker_symbol'] = i['sender_contract_ticker_symbol']
            _data_to_sent_lending['type'] = 'Mint'
            _data_to_sent_lending['trader']  = i['decoded']['params'][0]['value']
            _data_to_sent_lending['asset_amount'] = int(i['decoded']['params'][2]['value'])/math.pow(10,18)
            _data_transaction = self.get_a_transaction_global(_data_to_sent_lending['tx_hash'], api_key)
            if _data_transaction == 0 :
                return 0
            else :
                _data_to_sent_lending['total'] = _data_to_sent_lending['asset_amount']*_data_transaction['data']['items'][0]['gas_quote_rate'] if _data_to_sent_lending['ticker_symbol'] == 'iWRBTC' else _data_to_sent_lending['asset_amount']
                _data_to_sent_lending['total_gas'] = _data_transaction['data']['items'][0]['gas_quote']
            _d = database.database()
            _stat = _d.insert_lending_transaction(_data_to_sent_lending)
            if _stat == 0 :
                return 0
            print(_data_to_sent_lending)
        return 1

    def process_data_burn(self, data_burn, api_key) :
        _data_to_sent_lending = {}
        for i in data_burn['data']['items'] :
            _data_to_sent_lending['tx_hash'] = i['tx_hash']
            _data_to_sent_lending['block'] = i['block_height']
            _data_to_sent_lending['date'] = i['block_signed_at']
            _data_to_sent_lending['ticker_symbol'] = i['sender_contract_ticker_symbol']
            _data_to_sent_lending['type'] = 'Burn'
            _data_to_sent_lending['trader']  = i['decoded']['params'][0]['value']
            _data_to_sent_lending['asset_amount'] = int(i['decoded']['params'][2]['value'])/math.pow(10,18)
            _data_transaction = self.get_a_transaction_global(_data_to_sent_lending['tx_hash'], api_key)
            if _data_transaction == 0 :
                return 0
            else :
                _data_to_sent_lending['total'] = _data_to_sent_lending['asset_amount']*_data_transaction['data']['items'][0]['gas_quote_rate'] if _data_to_sent_lending['ticker_symbol'] == 'iWRBTC' else _data_to_sent_lending['asset_amount']
                _data_to_sent_lending['total_gas'] = _data_transaction['data']['items'][0]['gas_quote']
            _d = database.database()
            _stat = _d.insert_lending_transaction(_data_to_sent_lending)
            if _stat == 0 :
                return 0
            print(_data_to_sent_lending)
        return 1

    def get_a_transaction_global(self, tx_hash, api_key) :
        url = "https://api.covalenthq.com/v1/30/transaction_v2/" + tx_hash + "/?key=" + api_key
        print(url)
        _r = requests.get(url)
        time.sleep(0.5)
        if _r.status_code == 200 :
            return _r.json()
        else :
            return 0