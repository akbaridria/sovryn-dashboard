from modular.swap import swap
import os
from modular import swap
from decouple import config
from time import sleep
from utils import utils
from utils import database

API_KEY = config('API_KEY')
block = 3003000


while True :
    _swap = swap.swap(API_KEY,block)
    _r = _swap.crawling_data()
    block = _swap.process_data(_r)
    print(block)
    sleep(3)