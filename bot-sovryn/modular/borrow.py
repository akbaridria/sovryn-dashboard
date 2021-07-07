import requests
import math
from utils import database

class borrow :
    def __init__(self, api_key, starting_block) :
        self.api_key = api_key
        self.tokens = {
            '0xe700691da7b9851f2f35f8b8182c69c53ccad9db'.lower() : 'DoC',
            '0xb5999795BE0EbB5bAb23144AA5F D6A02D080299F'.lower() : 'XUSD',
            '0xEf213441a85DF4d7acBdAe0Cf78004E1e486BB96'.lower() : 'RUSDT',
            '0x6D9659bdF5b1A1dA217f7BbAf7dBAF8190E2e71B'.lower() : 'BNBs',
            '0x1D931Bf8656d795E50eF6D639562C5bD8Ac2B78f'.lower() : 'ETHs',
            '0xEfC78FC7D48B64958315949279bA181C2114abbD'.lower() : 'SOV',
            "0x542fDA317318eBF1d3DEAf76E0b632741A7e677d".lower() : 'RBTC',
            '0x9aC7Fe28967b30e3a4E6E03286D715B42B453d10'.lower() : 'MoC',
            '0x440cd83c160de5c96ddb20246815ea44c7abbca8'.lower() : 'BPRO'
        }
        self.token_borrow = {
            "0x542fDA317318eBF1d3DEAf76E0b632741A7e677d".lower() : 'RBTC',
            '0xe700691da7b9851f2f35f8b8182c69c53ccad9db'.lower() : 'DoC',
            '0xb5999795BE0EbB5bAb23144AA5F D6A02D080299F'.lower() : 'XUSD'
        }
        self.base_url_covalent_api = 'https://api.covalenthq.com/v1/'
        self.base_url_coingecko_api = 'https://api.coingecko.com/api/v3/'
        self.starting_block = starting_block
        self.end_block = self.starting_block + 500

    def call_api_covalent(self) :
        url = self.base_url_covalent_api + "30/events/topics/" + "0xb4eb3c9b62efcce7021cba5fd9cd0c44df91c2272806ccc5e57df7c912e8d716" + "/?key=" + self.api_key + "&starting-block=" + str(self.starting_block) + "&ending-block=" + str(self.starting_block + 500)
        _r = requests.get(url)
        if _r.status_code != 200 :
            return 0
        return _r.json()

    def process_data(self, data) :
        if data == 0 :
            print("oops")
            return self.starting_block
        else :
            items = data['data']['items']
            for i in items :
                _data_to_sent = {}
                if i['decoded']['params'][1]['value'].lower() in self.token_borrow.keys() and i['decoded']['params'][2]['value'].lower() in self.token_borrow.keys() :
                    _data_to_sent['tx_hash'] = i['tx_hash']
                    _data_to_sent['trader'] = i['decoded']['params'][3]['value']
                    _data_to_sent['block'] = i['block_height']
                    _data_to_sent['date'] = i['block_signed_at']
                    _data_to_sent['collateral_token'] = self.tokens[i['decoded']['params'][1]['value'].lower()]
                    _data_to_sent['collateral_amount'] = int(i['decoded']['params'][4]['value'])/math.pow(10,18)
                    _data_to_sent['borrow_token'] = self.tokens[i['decoded']['params'][2]['value'].lower()]
                    _data_to_sent['borrow_amount'] = int(i['decoded']['params'][5]['value'])/math.pow(10,18)
                    _data_to_sent['borrow_amount_in_usd'] = _data_to_sent['borrow_amount'] if _data_to_sent['borrow_token'] == 'DoC' or _data_to_sent['borrow_token'] == 'XUSD' else _data_to_sent['collateral_amount']
                    _d = database.database()
                    _stat = _d.insert_borrow_transaction(_data_to_sent)
                    if _stat == 0 :
                        return self.starting_block
                print(_data_to_sent)
            return self.starting_block + 500 