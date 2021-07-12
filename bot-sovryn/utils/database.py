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
    
    def insert_lending_transaction(self, data) :
        conn = self.mysqlconnect()
        _query = "INSERT IGNORE INTO `lending` (`tx_hash`, `date`, `block`, `ticker_symbol`, `type`, `trader`, `asset_amount`, `total`, `total_gas`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur = conn.cursor()
        try :
            cur.execute(_query,(data['tx_hash'], data['date'], data['block'], data['ticker_symbol'], data['type'], data['trader'], data['asset_amount'], data['total'], data['total_gas']))
            conn.commit()
        except Exception as e :
            print(e)
            conn.close()
            return 0
        else :
            conn.close()
            return 1
        
    def insert_borrow_transaction(self, data) :
        conn = self.mysqlconnect()
        _query = "INSERT IGNORE INTO `borrowing` (`tx_hash`, `trader`, `block`, `date`, `collateral_token`, `collateral_amount`, `borrow_token`, `borrow_amount`, `borrow_amount_in_usd`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur = conn.cursor()
        try :
            cur.execute(_query,(data['tx_hash'], data['trader'], data['block'], data['date'], data['collateral_token'], data['collateral_amount'], data['borrow_token'], data['borrow_amount'], data['borrow_amount_in_usd']))
            conn.commit()
        except Exception as e :
            print(e)
            conn.close()
            return 0
        else :
            conn.close()
            return 1
    
    def getBlock(self, database_name) :
        conn = self.mysqlconnect()
        cur = conn.cursor()
        query_sql = "SELECT block FROM " + database_name + " ORDER BY date DESC LIMIT 1"
        cur.execute(query_sql)
        _r = cur.fetchone()
        return _r
    
    def getBlockLend(self, database_name, typed) :
        conn = self.mysqlconnect()
        cur = conn.cursor()
        query_sql = "SELECT block FROM " + database_name + " WHERE type='" + typed + "' ORDER BY date DESC LIMIT 1"
        cur.execute(query_sql)
        _r = cur.fetchone()
        return _r
    
    def getDate(self, database_name) :
        conn = self.mysqlconnect()
        cur = conn.cursor()
        query_sql = "SELECT date FROM " + database_name + " ORDER BY date DESC LIMIT 1"
        cur.execute(query_sql)
        _r = cur.fetchone()
        return _r
    
    def getDateLend(self, database_name, typed) :
        conn = self.mysqlconnect()
        cur = conn.cursor()
        query_sql = "SELECT date FROM " + database_name + " WHERE type='" + typed + "' ORDER BY date DESC LIMIT 1"
        cur.execute(query_sql)
        _r = cur.fetchone()
        return _r

    
