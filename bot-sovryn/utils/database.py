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
        _query = "INSERT IGNORE INTO `swap` (`tx_hash`, `date`, `trader`, `from_token`, `to_token`, `from_value`, `to_value`, `total_value_usd`, `spent_gas`, `block`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur = conn.cursor()
        try :
            cur.execute(_query,(data['tx_hash'], data['date'], data['trader'], data['from_token'], data['to_token'], data['from_token_value'], data['to_token_value'], data['total_swap_usd'], data['total_gas_spent'], data['block']))
            conn.commit()
        except Exception as e :
            print(e)
            conn.close()
            return 0
        else :
            conn.close()
            return 1
