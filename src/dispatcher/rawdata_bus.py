'''
Created on 2019年7月21日

@author: 55057
'''



from database_helper.base_database_helper import BaseDatabaseHelper
import pymssql
import datetime

class RawDataBus:
    database_helper = 0
    conn = 0
    cursor = 0
    insert_sql_temple = """
        INSERT INTO dbo.book_information
        (ISBN,book_name,book_author,book_publisher,book_number,book_price,book_notes,book_storage_time)
        VALUES (%s, %s, %s, %s, %s, %s, %s ,%s)
        """
    
    def __init__(self):
        self.database_helper = BaseDatabaseHelper(host='127.0.0.1', user='sa', pwd='xyq566403', db="BookDB")
        self.conn = pymssql.connect(host=self.database_helper.host,user=self.database_helper.user,password=self.database_helper.pwd,database=self.database_helper.db,charset='utf8')
        self.cursor = self.conn.cursor()
        if not self.cursor:
            raise(NameError,'连接数据库失败')
    
    def __del__(self):
        self.conn.close()
    
    def writeBookInformationtoDatabase(self,book_information,isbn):
        
        self.cursor.executemany(self.insert_sql_temple,
                                [(isbn,book_information[0],book_information[1],book_information[2],
                                  book_information[3],book_information[4],'',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))])

        # 如果没有指定autocommit属性为True的话就需要调用commit()方法
        self.conn.commit()

    def closeConn(self):
        self.conn.close()

if __name__ == '__main__':
    rb = RawDataBus()
    rb.writeBookInformationtoDatabase('','')




        
    