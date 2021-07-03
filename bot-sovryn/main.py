from modular.swap import swap
import os
from modular import swap
from decouple import config
from time import sleep

API_KEY = config('API_KEY')
block = 2990000

count = 0
while True :
    _swap = swap.swap(API_KEY,block)
    _r = _swap.crawling_data()
    block = _swap.process_data(_r)
    print(block)
    sleep(3)
    if count > 0 :
        break
    count = count + 1