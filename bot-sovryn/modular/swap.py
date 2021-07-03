import requests
from utils import utils
import math
import time

class swap :
    def __init__(self, api_key, starting_block) :
        self.api_key = api_key
        self.tokens = {
            '0xe700691da7b9851f2f35f8b8182c69c53ccad9db' : 'DoC',
            '0xb5999795BE0EbB5bAb23144AA5FD6A02D080299F' : 'XUSD',
            '0xEf213441a85DF4d7acBdAe0Cf78004E1e486BB96' : 'RUSDT',
            '0x6D9659bdF5b1A1dA217f7BbAf7dBAF8190E2e71B' : 'BNBs',
            '0x1D931Bf8656d795E50eF6D639562C5bD8Ac2B78f' : 'ETHs',
            '0xEfC78FC7D48B64958315949279bA181C2114abbD' : 'SOV',
            '0x542fDA317318eBF1d3DEAf76E0b632741A7e677d' : 'RBTC',
            '0x9aC7Fe28967b30e3a4E6E03286D715B42B453d10' : 'MoC',
            '0x440cd83c160de5c96ddb20246815ea44c7abbca8' : 'BPRO'
        }
        self.include_tokens = {
            '0xe700691da7b9851f2f35f8b8182c69c53ccad9db' : 'DoC',
            '0xb5999795BE0EbB5bAb23144AA5FD6A02D080299F' : 'XUSD',
            '0xEf213441a85DF4d7acBdAe0Cf78004E1e486BB96' : 'RUSDT',
            '0x6D9659bdF5b1A1dA217f7BbAf7dBAF8190E2e71B' : 'BNBs',
            '0x1D931Bf8656d795E50eF6D639562C5bD8Ac2B78f' : 'ETHs',
            '0x542fDA317318eBF1d3DEAf76E0b632741A7e677d' : 'RBTC',
        }
        self.stable_coin = {
            '0xe700691da7b9851f2f35f8b8182c69c53ccad9db' : 'DoC',
            '0xb5999795BE0EbB5bAb23144AA5FD6A02D080299F' : 'XUSD',
            '0xEf213441a85DF4d7acBdAe0Cf78004E1e486BB96' : 'RUSDT',
        }
        self.token_map_coingecko = {
            '0x6D9659bdF5b1A1dA217f7BbAf7dBAF8190E2e71B' : 'binancecoin',
            '0x1D931Bf8656d795E50eF6D639562C5bD8Ac2B78f' : 'ethereum',
            '0x542fDA317318eBF1d3DEAf76E0b632741A7e677d' : 'bitcoin'
        }
        self.base_url_covalent_api = 'https://api.covalenthq.com/v1/'
        self.base_url_coingecko_api = 'https://api.coingecko.com/api/v3/'
        self.starting_block = starting_block
        self.end_block = self.starting_block + 500

    def crawling_data(self) :
        url = self.base_url_covalent_api + "30/events/address/0x98aCE08D2b759a265ae326F010496bcD63C15afc/?starting-block=" + str(self.starting_block) + "&ending-block=" + str(self.end_block) + "&key=" + self.api_key + "&page-size=9999"
        _r = requests.get(url)
        if _r.status_code == 200 :
            return _r.json()
        else :
            return 0

    def process_data(self, data) :
        if data == 0 :
            return self.starting_block
        else :
            items = data['data']['items']
            _data_to_sent = {}
            for i in items :
                if i['decoded']['name'] == 'Conversion' :
                    if i['decoded']['params'][1]['value'] in self.include_tokens.keys() or i['decoded']['params'][2]['value'] in self.include_tokens.keys() :
                        _data_to_sent['date'] = i['block_signed_at']
                        _data_to_sent['tx_hash'] = i['tx_hash']
                        _data_to_sent['block'] = i['block_height']
                        _data_to_sent['from_token'] = self.tokens[i['decoded']['params'][1]['value']]
                        _data_to_sent['to_token'] = self.tokens[i['decoded']['params'][2]['value']]
                        _data_to_sent['trader'] = i['decoded']['params'][5]['value']
                        _data_to_sent['from_token_value'] = i['decoded']['params'][3]['value']
                        _data_to_sent['to_token_value'] = i['decoded']['params'][4]['value']
                        if i['decoded']['params'][1]['value'] in self.stable_coin.keys() :
                            _data_to_sent['total_swap_usd'] = int(i['decoded']['params'][1]['value'])/math.pow(10, 18)
                        elif i['decoded']['params'][2]['value'] in self.stable_coin.keys() :
                            _data_to_sent['total_swap_usd'] = int(i['decoded']['params'][2]['value'])/math.pow(10, 18)
                        else :
                            time.sleep(1)
                            
            # print(utils.utils.insert_swap_transaction(data))
            return self.starting_block + 500