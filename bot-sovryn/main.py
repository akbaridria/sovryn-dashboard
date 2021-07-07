from requests import api
from modular import swap
import os
from modular import swap
from decouple import config
from time import sleep
from utils import utils
from utils import database
from modular import borrow
from modular import lending

API_KEY = config('API_KEY')
block_swap = 2742574
block_borrow = 2742496
block_lend_mint = 2742512
block_lend_burn = 2744165

while True :
    # _swap = swap.swap(API_KEY,block_swap)
    # _r = _swap.crawling_data()
    # block_swap = _swap.process_data(_r)
    # print(block_swap)
    _borrow = borrow.borrow(API_KEY, block_borrow)
    _r_borrow = _borrow.call_api_covalent()
    block_borrow = _borrow.process_data(_r_borrow)
    # _lending = lending.lending(API_KEY)
    # _r_lending_mint = _lending.call_api_covalent_mint(block_lend_mint)
    # sleep(1)
    # _r_lending_burn = _lending.call_api_covalent_burn(block_lend_burn)
    # block_lend_mint, block_lend_burn = _lending.process_data(_r_lending_mint, _r_lending_burn, block_lend_mint, block_lend_burn, API_KEY)
    
    
    sleep(3)