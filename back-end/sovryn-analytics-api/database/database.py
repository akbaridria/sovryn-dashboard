from posixpath import split
import pymysql
from decouple import Config, config
from pymysql.constants import CLIENT

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
            cursorclass=pymysql.cursors.DictCursor,
            client_flag=CLIENT.MULTI_STATEMENTS
            )
        return conn
    
    def get_the_largest_swap(self, from_date=0, to_date=0, wallet=0) :
        conn = self.mysqlconnect()
        cur = conn.cursor()
        if from_date == 0 and wallet == 0 :
            query_sql = "SELECT MAX(total_value_usd +0) AS largest_swap, SUM(total_value_usd +0.0) AS total_volume, COUNT(DISTINCT(trader)) AS total_unique, COUNT(tx_hash) AS total_transaction FROM `swap`"
        elif from_date != 0 and wallet == 0 :
            query_sql = "SELECT MAX(total_value_usd +0) AS largest_swap, SUM(total_value_usd +0.0) AS total_volume, COUNT(DISTINCT(trader)) AS total_unique, COUNT(tx_hash) AS total_transaction FROM `swap` WHERE `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "'"
        elif from_date != 0 and wallet != 0 :
            query_sql = "SELECT MAX(total_value_usd +0) AS largest_swap, SUM(total_value_usd +0.0) AS total_volume, COUNT(DISTINCT(trader)) AS total_unique, COUNT(tx_hash) AS total_transaction FROM `swap` WHERE `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "' AND `trader` = '" + str(wallet) + "'"
        print(query_sql)
        
        cur.execute(query_sql)
        _d = cur.fetchone()
        return _d
    
    def get_rbtc_doc(self, from_date = 0, to_date = 0, wallet = 0) :
        conn = self.mysqlconnect()
        cur = conn.cursor()
        if from_date == 0 and wallet == 0 :
            query_sql = "SELECT COUNT(tx_hash) AS rbtc_doc FROM `swap` WHERE from_token IN ('RBTC','DoC') AND to_token IN ('RBTC','DoC')"
        elif from_date != 0 and wallet == 0 :
            query_sql = "SELECT COUNT(tx_hash) AS rbtc_doc FROM `swap` WHERE from_token IN ('RBTC','DoC') AND to_token IN ('RBTC','DoC') AND `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "'"
        elif from_date != 0 and wallet != 0 :
            query_sql = "SELECT COUNT(tx_hash) AS rbtc_doc FROM `swap` WHERE from_token IN ('RBTC','DoC') AND to_token IN ('RBTC','DoC') AND `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "' AND `trader` = '" + str(wallet) + "'"
        cur.execute(query_sql)
        _r = cur.fetchone()
        return _r
    
    def get_rbtc_rusdt(self, from_date = 0, to_date = 0, wallet = 0) :
        conn = self.mysqlconnect()
        cur = conn.cursor()
        if from_date == 0 and wallet == 0 :
            query_sql = "SELECT COUNT(tx_hash) AS rbtc_rusdt FROM `swap` WHERE from_token IN ('RBTC','RUSDT') AND to_token IN ('RBTC','RUSDT')"
        elif from_date != 0 and wallet == 0 :
            query_sql = "SELECT COUNT(tx_hash) AS rbtc_rusdt FROM `swap` WHERE from_token IN ('RBTC','RUSDT') AND to_token IN ('RBTC','RUSDT') AND `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "'"
        elif from_date != 0 and wallet != 0 :
            query_sql = "SELECT COUNT(tx_hash) AS rbtc_rusdt FROM `swap` WHERE from_token IN ('RBTC','RUSDT') AND to_token IN ('RBTC','RUSDT') AND `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "' AND `trader` = '" + str(wallet) + "'"
        cur.execute(query_sql)
        _r = cur.fetchone()
        return _r
    
    def get_rbtc_bpro(self, from_date = 0, to_date = 0, wallet = 0) :
        conn = self.mysqlconnect()
        cur = conn.cursor()
        if from_date == 0 and wallet == 0 :
            query_sql = "SELECT COUNT(tx_hash) AS rbtc_bpro FROM `swap` WHERE from_token IN ('RBTC','BPRO') AND to_token IN ('RBTC','BPRO')"
        elif from_date != 0 and wallet == 0 :
            query_sql = "SELECT COUNT(tx_hash) AS rbtc_bpro FROM `swap` WHERE from_token IN ('RBTC','BPRO') AND to_token IN ('RBTC','BPRO') AND `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "'"
        elif from_date != 0 and wallet != 0 :
            query_sql = "SELECT COUNT(tx_hash) AS rbtc_bpro FROM `swap` WHERE from_token IN ('RBTC','BPRO') AND to_token IN ('RBTC','BPRO') AND `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "' AND `trader` = '" + str(wallet) + "'"
        cur.execute(query_sql)
        _r = cur.fetchone()
        return _r
    
    def get_rbtc_sov(self, from_date = 0, to_date = 0, wallet = 0) :
        conn = self.mysqlconnect()
        cur = conn.cursor()
        if from_date == 0 and wallet == 0 :
            query_sql = "SELECT COUNT(tx_hash) AS rbtc_sov FROM `swap` WHERE from_token IN ('RBTC','SOV') AND to_token IN ('RBTC','SOV')"
        elif from_date != 0 and wallet == 0 :
            query_sql = "SELECT COUNT(tx_hash) AS rbtc_sov FROM `swap` WHERE from_token IN ('RBTC','SOV') AND to_token IN ('RBTC','SOV') AND `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "'"
        elif from_date != 0 and wallet != 0 :
            query_sql = "SELECT COUNT(tx_hash) AS rbtc_sov FROM `swap` WHERE from_token IN ('RBTC','SOV') AND to_token IN ('RBTC','SOV') AND `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "' AND `trader` = '" + str(wallet) + "'"
        cur.execute(query_sql)
        _r = cur.fetchone()
        return _r
    
    def get_total_swap(self, from_date = 0, to_date = 0, wallet = 0) :
        conn = self.mysqlconnect()
        cur = conn.cursor()
        if from_date == 0 and wallet == 0 :
            query_sql = "select date, SUM(total_value_usd) from swap GROUP BY date"
        elif from_date != 0  and wallet == 0 :
            query_sql = "select date, SUM(total_value_usd) from swap WHERE `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "'" + " GROUP BY date"
        elif from_date != 0 and wallet != 0 :
            query_sql = "select date, SUM(total_value_usd) from swap WHERE `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "' AND `trader` = '" + str(wallet) + "' GROUP BY date"
        cur.execute(query_sql)
        _r = cur.fetchall()
        return _r
    
    def get_swap_month(self, from_date = 0, to_date = 0, wallet = 0) :
        conn = self.mysqlconnect()
        cur = conn.cursor()
        if from_date == 0 and wallet == 0 :
            query_sql = "select MONTH(date) AS month, SUM(total_value_usd) AS volume from swap GROUP BY YEAR(date), MONTH(date)"
        elif from_date != 0  and wallet == 0 :
            query_sql = "select MONTH(date) AS month, SUM(total_value_usd) AS volume from swap WHERE `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "'" + " GROUP BY YEAR(date), MONTH(date)"
        elif from_date != 0 and wallet != 0 :
            query_sql = "select MONTH(date) AS month, SUM(total_value_usd) AS volume from swap WHERE `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "' AND `trader` = '" + str(wallet) + "' GROUP BY YEAR(date), MONTH(date)"
        cur.execute(query_sql)
        _r = cur.fetchall()
        return _r
    
    def get_swap_user(self, from_date = 0, to_date = 0, wallet = 0) :
        conn = self.mysqlconnect()
        cur = conn.cursor()
        if from_date == 0 and wallet == 0 :
            query_sql = "SELECT date, COUNT(DISTINCT(trader)) AS unique_swapper FROM `swap` GROUP BY date"
        elif from_date != 0  and wallet == 0 :
            query_sql = "SELECT date, COUNT(DISTINCT(trader)) AS unique_swapper FROM `swap` WHERE `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "'" + " GROUP BY date"
        elif from_date != 0 and wallet != 0 :
            query_sql = "SELECT date, COUNT(DISTINCT(trader)) AS unique_swapper FROM `swap` WHERE `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "' AND `trader` = '" + str(wallet) + "' GROUP BY date"
        cur.execute(query_sql)
        _r = cur.fetchall()
        return _r
    
    def get_swap_user_month(self, from_date = 0, to_date = 0, wallet = 0) :
        conn = self.mysqlconnect()
        cur = conn.cursor()
        if from_date == 0 and wallet == 0 :
            query_sql = "SELECT date, COUNT(DISTINCT(trader)) AS unique_swapper FROM `swap` GROUP BY YEAR(date), MONTH(date)"
        elif from_date != 0  and wallet == 0 :
            query_sql = "SELECT date, COUNT(DISTINCT(trader)) AS unique_swapper FROM `swap` WHERE `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "'" + " GROUP BY YEAR(date), MONTH(date)"
        elif from_date != 0 and wallet != 0 :
            query_sql = "SELECT date, COUNT(DISTINCT(trader)) AS unique_swapper FROM `swap` WHERE `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "' AND `trader` = '" + str(wallet) + "' GROUP BY YEAR(date), MONTH(date)"
        cur.execute(query_sql)
        _r = cur.fetchall()
        return _r
    
    def get_spent_gas_date(self, from_date = 0, to_date = 0, wallet = 0) :
        conn = self.mysqlconnect()
        cur = conn.cursor()
        if from_date == 0 and wallet == 0 :
            query_sql = "select date, SUM(spent_gas) AS volume from swap group by date"
        elif from_date != 0  and wallet == 0 :
            query_sql = "select date, SUM(spent_gas) AS volume from swap WHERE `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "'" + " group by date"
        elif from_date != 0 and wallet != 0 :
            query_sql = "select date, SUM(spent_gas) AS volume from swap WHERE `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "' AND `trader` = '" + str(wallet) + "' group by date"
        cur.execute(query_sql)
        _r = cur.fetchall()
        return _r
    
    def get_spent_gas_month(self, from_date = 0, to_date = 0, wallet = 0) :
        conn = self.mysqlconnect()
        cur = conn.cursor()
        if from_date == 0 and wallet == 0 :
            query_sql = "select MONTH(date) AS month, SUM(spent_gas) AS volume from swap GROUP BY YEAR(date), MONTH(date)"
        elif from_date != 0  and wallet == 0 :
            query_sql = "select MONTH(date) AS month, SUM(spent_gas) AS volume from swap WHERE `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "'" + " GROUP BY YEAR(date), MONTH(date)"
        elif from_date != 0 and wallet != 0 :
            query_sql = "select MONTH(date) AS month, SUM(spent_gas) AS volume from swap WHERE `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "' AND `trader` = '" + str(wallet) + "' GROUP BY YEAR(date), MONTH(date)"
        cur.execute(query_sql)
        _r = cur.fetchall()
        return _r
    
    def top_trader(self, from_date = 0, to_date = 0, wallet = 0) :
        conn = self.mysqlconnect()
        cur = conn.cursor()
        if from_date == 0 and wallet == 0 :
            query_sql = "select trader, SUM(total_value_usd) AS volume from swap GROUP BY trader ORDER BY volume DESC LIMIT 10"
        elif from_date != 0  and wallet == 0 :
            query_sql = "select trader, SUM(total_value_usd) AS volume from swap WHERE `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "'" + " GROUP BY trader ORDER BY volume DESC LIMIT 10"
        elif from_date != 0 and wallet != 0 :
            query_sql = "select trader, SUM(total_value_usd) AS volume from swap WHERE `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "' AND `trader` = '" + str(wallet) + "' GROUP BY trader ORDER BY volume DESC LIMIT 10"
        cur.execute(query_sql)
        _r = cur.fetchall()
        return _r

    def get_kpi_lending(self, from_date=0, to_date=0, wallet=0) :
        conn = self.mysqlconnect()
        cur = conn.cursor()
        if from_date == 0 and wallet == 0 :
            query_sql = "SELECT SUM(total) AS total, type, COUNT(DISTINCT(trader)) AS user from lending WHERE ticker_symbol != 'iBPro' GROUP BY type"
        elif from_date != 0 and wallet == 0 :
            query_sql = "SELECT SUM(total) AS total, type, COUNT(DISTINCT(trader)) AS user from lending  WHERE ticker_symbol != 'iBPro' AND `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "' GROUP BY type"
        elif from_date != 0 and wallet != 0 :
            query_sql = "SELECT SUM(total) AS total, type, COUNT(DISTINCT(trader)) AS user from lending  WHERE ticker_symbol != 'iBPro' AND `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "' AND `trader` = '" + str(wallet) + "' GROUP BY type"
        print(query_sql)
        cur.execute(query_sql)
        _d = cur.fetchall()
        return _d
    
    def get_total_mint_burn(self, from_date=0, to_date=0, wallet=0) :
        conn = self.mysqlconnect()
        cur = conn.cursor()
        if from_date == 0 and wallet == 0 :
            query_sql = "SELECT date, sum( if( type = 'Mint', total, 0 ) ) AS Mint, sum( if( type = 'Burn', total, 0 ) ) AS Burn FROM lending as T1 GROUP BY T1.date"
        elif from_date != 0 and wallet == 0 :
            query_sql = "SELECT date, sum( if( type = 'Mint', total, 0 ) ) AS Mint, sum( if( type = 'Burn', total, 0 ) ) AS Burn FROM lending as T1 WHERE ticker_symbol != 'iBPro' AND `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "' GROUP BY T1.date"
        elif from_date !=0 and wallet != 0 :
            query_sql = "SELECT date, sum( if( type = 'Mint', total, 0 ) ) AS Mint, sum( if( type = 'Burn', total, 0 ) ) AS Burn FROM lending as T1 WHERE ticker_symbol != 'iBPro' AND `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "' AND `trader` = '" + str(wallet) + "' GROUP BY T1.date"
        cur.execute(query_sql)
        _r = cur.fetchall()
        return _r
    
    def get_user_mint_burn(self, from_date=0, to_date=0, wallet=0) :
        conn = self.mysqlconnect()
        cur = conn.cursor()
        if from_date == 0 and wallet == 0 :
            query_sql = "SELECT date, (SELECT COUNT(DISTINCT(trader)) FROM lending WHERE type='Mint' AND date=T1.date) AS Mint, (SELECT COUNT(DISTINCT(trader)) FROM lending WHERE ticker_symbol != 'iBPro' AND type='Burn' AND date=T1.date) AS Burn FROM lending as T1 GROUP BY T1.date"
        elif from_date != 0 and wallet == 0 :
            query_sql = "SELECT date, (SELECT COUNT(DISTINCT(trader)) FROM lending WHERE type='Mint' AND date=T1.date) AS Mint, (SELECT COUNT(DISTINCT(trader)) FROM lending WHERE ticker_symbol != 'iBPro' AND type='Burn' AND date=T1.date) AS Burn FROM lending as T1 WHERE `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "' GROUP BY T1.date"
        elif from_date !=0 and wallet != 0 :
            query_sql = "SELECT date, (SELECT COUNT(DISTINCT(trader)) FROM lending WHERE type='Mint' AND date=T1.date) AS Mint, (SELECT COUNT(DISTINCT(trader)) FROM lending WHERE ticker_symbol != 'iBPro' AND type='Burn' AND date=T1.date) AS Burn FROM lending as T1 WHERE `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "' AND `trader` = '" + str(wallet) + "' GROUP BY T1.date"
        cur.execute(query_sql)
        _r = cur.fetchall()
        return _r

    def get_kpi_borrowing(self, from_date=0, to_date=0, wallet=0) :
        conn = self.mysqlconnect()
        cur = conn.cursor()
        if from_date == 0 and wallet == 0 :
            query_sql = "SELECT sum(borrow_amount_in_usd) AS borrow, COUNT(DISTINCT(trader)) AS user, COUNT(tx_hash) AS transactions FROM `borrowing`"
        elif from_date != 0 and wallet == 0 :
            query_sql = "SELECT sum(borrow_amount_in_usd) AS borrow, COUNT(DISTINCT(trader)) AS user, COUNT(tx_hash) AS transactions FROM `borrowing` WHERE `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "'"
        elif from_date !=0 and wallet != 0 :
            query_sql = "SELECT sum(borrow_amount_in_usd) AS borrow, COUNT(DISTINCT(trader)) AS user, COUNT(tx_hash) AS transactions FROM `borrowing` WHERE `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "' AND `trader` = '" + str(wallet) + "'"
        cur.execute(query_sql)
        _r = cur.fetchone()
        return _r
    
    def get_total_borrow_date(self, from_date=0, to_date=0, wallet=0) :
        conn = self.mysqlconnect()
        cur = conn.cursor()
        if from_date == 0 and wallet == 0 :
            query_sql = "SELECT date, SUM(borrow_amount_in_usd) AS total FROM borrowing GROUP BY date"
        elif from_date != 0 and wallet == 0 :
            query_sql = "SELECT date, SUM(borrow_amount_in_usd) AS total FROM borrowing WHERE `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "' GROUP BY date"
        elif from_date !=0 and wallet != 0 :
            query_sql = "SELECT date, SUM(borrow_amount_in_usd) AS total FROM borrowing WHERE `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "' AND `trader` = '" + str(wallet) + "' GROUP BY date"
        cur.execute(query_sql)
        _r = cur.fetchall()
        return _r

    def get_total_user_borrow(self, from_date=0, to_date=0, wallet=0) :
        conn = self.mysqlconnect()
        cur = conn.cursor()
        if from_date == 0 and wallet == 0 :
            query_sql = "SELECT date, COUNT(DISTINCT(trader)) AS total FROM borrowing GROUP BY date"
        elif from_date != 0 and wallet == 0 :
            query_sql = "SELECT date, COUNT(DISTINCT(trader)) AS total FROM borrowing WHERE `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "' GROUP BY date"
        elif from_date !=0 and wallet != 0 :
            query_sql = "SELECT date, COUNT(DISTINCT(trader)) AS total FROM borrowing WHERE `date` >= '" + str(from_date) + "' AND `date` <= '" + str(to_date) + "' AND `trader` = '" + str(wallet) + "' GROUP BY date"
        cur.execute(query_sql)
        _r = cur.fetchall()
        return _r

    def getBlock(self, database_name) :
        conn = self.mysqlconnect()
        cur = conn.cursor()
        query_sql = "SELECT block FROM " + database_name + " ORDER BY date DESC LIMIT 1"
        cur.execute(query_sql)
        _r = cur.fetchone()
        return _r
