import time
import requests
import time
from utils import utils


class lending :
    def __init__(self, api_key) :
        self.api_key = api_key
        self.base_url_covalent_api = 'https://api.covalenthq.com/v1/'
        self.base_url_coingecko_api = 'https://api.coingecko.com/api/v3/'
    
    def call_api_covalent_mint(self, starting_block) :
        url = self.base_url_covalent_api + "30/events/topics/" + "0xb4c03061fb5b7fed76389d5af8f2e0ddb09f8c70d1333abbb62582835e10accb" + "/?key=" + self.api_key + "&starting-block=" + str(starting_block) + "&ending-block=" + str(starting_block + 500)
        _r = requests.get(url)
        if _r.status_code != 200 :
            return 0
        return _r.json()
    
    def call_api_covalent_burn(self, starting_block) :
        url = self.base_url_covalent_api + "30/events/topics/" + "0x743033787f4738ff4d6a7225ce2bd0977ee5f86b91a902a58f5e4d0b297b4644" + "/?key=" + self.api_key + "&starting-block=" + str(starting_block) + "&ending-block=" + str(starting_block + 500)
        _r = requests.get(url)
        if _r.status_code != 200 :
            return 0
        return _r.json()

    def process_data(self, data_mint, data_burn, block_mint, block_burn, api_key) :
        if data_mint == 0 or data_burn == 0 :
            return block_mint, block_burn
        else :
            _utils = utils.utils()
            _process_mint = _utils.process_data_mint(data_mint, api_key)
            time.sleep(1)
            _process_burn = _utils.process_data_burn(data_burn, api_key)
            if _process_mint == 0  and _process_burn == 0 :
                return block_mint, block_burn
            return block_mint + 500, block_burn + 500