'''
Created on 2019年7月20日

@author: 55057
'''

import pymssql
import logging

'基础数据库功能'
class BaseDatabaseHelper:
    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
 
    def GetConnect(self):
        if not self.db:
            raise(NameError,'没有设置数据库信息')
            logging.error('没有设置数据库信息')
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset='utf8')
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,'连接数据库失败')
            logging.error('连接数据库失败')
        else:
            return cur
 
    def ExecQuery(self,sql):
        cur = self.GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()
 
        self.conn.close()
        return resList
 
    def ExecNonQuery(self,sql):
        cur = self.GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()
 
    def GetData(self,sql):
        count = 0
        for i in range(len(sql)):
            for j in range(len(sql[i])):
                count += 1
                if type(sql[i][j]) is str:
                    print(sql[i][j].encode('latin1').decode('gbk'),end=',')
                else:
                    print(sql[i][j],end=',')
                if count % len(sql[i]) == 0:
                    print('\n')
 

def test():
    ms = BaseDatabaseHelper(host='127.0.0.1', user='sa', pwd='xyq566403', db="BookDB")   #连接串
    sql = ms.ExecQuery('SELECT top 5 * from dbo.testTB')
    ms.GetData(sql)
 
 
if __name__ == '__main__':
    test()