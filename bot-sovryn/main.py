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
from datetime import date, datetime

API_KEY = config('API_KEY')

while True :
    _d = database.database()
    today = date.today()
    block_swap = _d.getBlock('swap')
    block_borrow = _d.getBlock('borrowing')
    block_lend_mint = _d.getBlockLend('lending', 'Mint')
    block_lend_burn = _d.getBlockLend('lending', 'Burn')
    date_swap = _d.getDate('swap')
    date_borrow = _d.getDate('borrowing')
    date_lend_mint = _d.getDateLend('lending', 'Mint')
    date_lend_burn = _d.getDateLend('lending', 'Burn')
    if date_swap["date"] < today :
        _swap = swap.swap(API_KEY,int(block_swap["block"]))
        _r = _swap.crawling_data()
        block_swap = _swap.process_data(_r)
        print(block_swap)
    if date_borrow["date"] < today :
        _borrow = borrow.borrow(API_KEY, int(block_borrow["block"]))
        _r_borrow = _borrow.call_api_covalent()
        block_borrow = _borrow.process_data(_r_borrow)
    if date_lend_burn["date"] < today and date_lend_mint["date"] < today :
        _lending = lending.lending(API_KEY)
        _r_lending_mint = _lending.call_api_covalent_mint(int(block_lend_mint["block"]))
        sleep(1)
        _r_lending_burn = _lending.call_api_covalent_burn(int(block_lend_burn["block"]))
        block_lend_mint, block_lend_burn = _lending.process_data(_r_lending_mint, _r_lending_burn, int(block_lend_mint["block"]), int(block_lend_burn["block"]), API_KEY)
        
    
    sleep(3)