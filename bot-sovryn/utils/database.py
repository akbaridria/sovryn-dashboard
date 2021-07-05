import pymysql
from decouple import Config, config

class database :

    def __init__(self) :
        self.user = config('USER_DB')
        self.password = config('PASSWORD_DB')
        self.host = config('HOST_DB') 
        self.db_name = config('NAME_DB')

    def mysqlconnect(self):
        conn = pymysql.connect(
            host=self.host,
            user=self.user, 
            password=self.password,
            db='akbaridr_sov',
            port=3306,
            cursorclass=pymysql.cursors.DictCursor
            )
        return conn
    
    def insert_swap_transaction(self, data) :
        conn = self.mysqlconnect()
        query = "INSERT INTO `swap` ("