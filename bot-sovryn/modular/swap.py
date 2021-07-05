import requests
from utils import utils
import math
import time

class swap :
    def __init__(self, api_key, starting_block) :
        self.api_key = api_key
        self.tokens = {
            '0xe700691da7b9851f2f35f8b8182c69c53ccad9db'.lower() : 'DoC',
            '0xb5999795BE0EbB5bAb23144AA5FD6A02D080299F'.lower() : 'XUSD',
            '0xEf213441a85DF4d7acBdAe0Cf78004E1e486BB96'.lower() : 'RUSDT',
            '0x6D9659bdF5b1A1dA217f7BbAf7dBAF8190E2e71B'.lower() : 'BNBs',
            '0x1D931Bf8656d795E50eF6D639562C5bD8Ac2B78f'.lower() : 'ETHs',
            '0xEfC78FC7D48B64958315949279bA181C2114abbD'.lower() : 'SOV',
            "0x542fDA317318eBF1d3DEAf76E0b632741A7e677d".lower() : 'RBTC',
            '0x9aC7Fe28967b30e3a4E6E03286D715B42B453d10'.lower() : 'MoC',
            '0x440cd83c160de5c96ddb20246815ea44c7abbca8'.lower() : 'BPRO'
        }
        self.include_tokens = {
            '0xe700691da7b9851f2f35f8b8182c69c53ccad9db'.lower() : 'DoC',
            '0xb5999795BE0EbB5bAb23144AA5FD6A02D080299F'.lower() : 'XUSD',
            '0xEf213441a85DF4d7acBdAe0Cf78004E1e486BB96'.lower() : 'RUSDT',
            '0x6D9659bdF5b1A1dA217f7BbAf7dBAF8190E2e71B'.lower() : 'BNBs',
            '0x1D931Bf8656d795E50eF6D639562C5bD8Ac2B78f'.lower() : 'ETHs',
            '0x542fDA317318eBF1d3DEAf76E0b632741A7e677d'.lower() : 'RBTC',
        }
        self.stable_coin = {
            '0xe700691da7b9851f2f35f8b8182c69c53ccad9db'.lower() : 'DoC',
            '0xb5999795BE0EbB5bAb23144AA5FD6A02D080299F'.lower() : 'XUSD',
            '0xEf213441a85DF4d7acBdAe0Cf78004E1e486BB96'.lower() : 'RUSDT',
        }
        self.token_map_coingecko = {
            '0x6D9659bdF5b1A1dA217f7BbAf7dBAF8190E2e71B'.lower() : 'binancecoin',
            '0x1D931Bf8656d795E50eF6D639562C5bD8Ac2B78f'.lower() : 'ethereum',
            '0x542fDA317318eBF1d3DEAf76E0b632741A7e677d'.lower() : 'bitcoin'
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
                    if i['decoded']['params'][1]['value'].lower() in self.include_tokens.keys() or i['decoded']['params'][2]['value'].lower() in self.include_tokens.keys() :
                        _data_to_sent['date'] = i['block_signed_at']
                        _data_to_sent['tx_hash'] = i['tx_hash']
                        _data_to_sent['block'] = i['block_height']
                        _data_to_sent['from_token'] = self.tokens[str(i['decoded']['params'][1]['value']).lower()]
                        _data_to_sent['to_token'] = self.tokens[str(i['decoded']['params'][2]['value']).lower()]
                        _data_to_sent['from_token_value'] = int(i['decoded']['params'][3]['value'])/math.pow(10, 18)
                        _data_to_sent['to_token_value'] = int(i['decoded']['params'][4]['value'])/math.pow(10, 18)
                        tanggal = _data_to_sent['date'][:10]
                        _tanggal = tanggal[8:10] + "-" + tanggal[5:7] + "-" + tanggal[:4]
                        if i['decoded']['params'][1]['value'].lower() in self.stable_coin.keys() :
                            _data_to_sent['total_swap_usd'] = int(i['decoded']['params'][3]['value'])/math.pow(10, 18)
                        elif i['decoded']['params'][2]['value'].lower() in self.stable_coin.keys() :
                            _data_to_sent['total_swap_usd'] = int(i['decoded']['params'][4]['value'])/math.pow(10, 18)
                        else :
                            time.sleep(1)
                            if i['decoded']['params'][1]['value'].lower() in self.include_tokens.keys() :
                                _status, _price = utils.utils.get_gecko_price(self.base_url_coingecko_api, self.token_map_coingecko[i['decoded']['params'][1]['value']], _tanggal)
                                if _status == 0 :
                                    return self.starting_block
                                else :
                                    _data_to_sent['total_swap_usd'] = float(_price) * float(_data_to_sent['from_token_value'])
                            else :
                                _status, _price = utils.utils.get_gecko_price(self.base_url_coingecko_api, self.token_map_coingecko[i['decoded']['params'][2]['value']], _tanggal)
                                if _status == 0 :
                                    return self.starting_block
                                else :
                                    _data_to_sent['total_swap_usd'] = float(_price) * float(_data_to_sent['to_token_value'])
                        url_transaction_covalent = self.base_url_covalent_api + "30/transaction_v2/" + _data_to_sent['tx_hash'] + "/?key=" + self.api_key
                        _status_transaction, _trader, _total_gas_spent = utils.utils.get_a_transaction_covalent(url_transaction_covalent,_tanggal)
                        if _status_transaction == 1 :
                            _data_to_sent['trader'] = _trader
                            _data_to_sent['total_gas_spent'] = _total_gas_spent
                        else :
                            return self.starting_block
                        print(_data_to_sent)
            # print(utils.utils.insert_swap_transaction(data))
            return self.starting_block + 500