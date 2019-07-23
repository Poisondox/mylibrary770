'''
Created on 2019年7月21日

@author: 55057
'''



from database_helper.base_database_helper import BaseDatabaseHelper
import pymssql
import datetime
import openpyxl
import logging
from book_querier.book_querier_engine import ISBNSearchEngine


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
            logging.error('连接数据库失败')
    
    def __del__(self):
        self.conn.close()
        
    
    def writeBookInformationtoDatabase(self,book_information,isbn):
        #执行写入操作
        self.cursor.executemany(self.insert_sql_temple,
                                [(isbn,book_information[0],book_information[1],book_information[2],
                                  book_information[3],book_information[4],'',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))])

        # 如果没有指定autocommit属性为True的话就需要调用commit()方法
        self.conn.commit()
        logging.debug("数据写入数据库完成"+isbn)
        #this is test function
        

    def closeConn(self):
        self.conn.close()

def execlDataToList(execl_filepath):
        #打开工作簿
    workbook = openpyxl.load_workbook(execl_filepath)
    sheet = workbook.active
    logging.info('workbook row is:'+str(sheet.max_row))
    #定义ISBN列表
    list_isbn = []
    for row_id in range(1,sheet.max_row+1):
       #增加ISBN
       list_isbn.append(sheet["A"+str(row_id)].value)
        #输出信息
    logging.info('ISBN length is'+str(len(list_isbn)))
    print('ISBN length is:'+str(len(list_isbn)))
    return list_isbn

def ISBNListToBookInformation(list_isbn):
    #图书详细内容
    isbn_list_length = len(list_isbn)
    bookdetaillist = []
    isbnEngine = ISBNSearchEngine()
    for index in range(0,isbn_list_length):
        #查找图书详情
        bookdetail = isbnEngine.get_information_with_ISBN(list_isbn[index])
        #构建图书详细信息
        bookdetaillist.append(bookdetail)
        
    logging.info('book detail list build succeed.')
    
    

#test function
if __name__ == '__main__':
    list = execlDataToList("D:/rawdata/mylibrary/all_isbn.xlsx")
    details = ISBNListToBookInformation(list)



        
    
