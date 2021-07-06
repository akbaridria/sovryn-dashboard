import requests


class lending :
    def __init__(self, api_key) :
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
    
    def call_api_covalent_mint(self, starting_block) :
        url = self.base_url_covalent_api + "30/events/topics/" + "0x3aca338664f2c5eab1eb96b6722219dd3b08e1461a2fcac1a25415f70d2ffa46" + "/?key=" + self.api_key + "&starting-block=" + str(starting_block) + "&ending-block=" + str(starting_block + 500)
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

    def process_data(self, data_mint, data_burn, block_mint, block_burn) :
        if data_mint == 0 or data_burn == 0 :
            return block_mint, block_burn
        else :
            
            return 0, 1