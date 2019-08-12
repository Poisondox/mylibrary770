'''
Created on 2019�?8�?8�?

@author: 55057
'''

# 图书对象模型
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TEXT
from sqlalchemy.sql.sqltypes import Float
from sqlalchemy.dialects.mysql.types import TIMESTAMP

# 基础对象
Base = declarative_base()

#########################################################
# Book实例
class Book(Base):
    __tablename__ = u'bookslist'
    
    ID = Column(Integer, primary_key=True)  # 数据库主�?
    ISBN = Column(String)  # 图书ISBN�?
    book_name = Column(String, nullable=True)  # 图书名称
    book_author = Column(String, nullable=True)  # 图书作�??
    book_publisher = Column(String, nullable=True)  # 图书出版�?
    book_number = Column(String, nullable=True)  # 中图分类�?
    book_price = Column(Float, nullable=True)  # 图书价格
    book_notes = Column(TEXT, nullable=True)  # 图书笔记
    book_storoge_time = Column(TIMESTAMP, nullable=True)  # 图书入库时间
    
##########################################################
    

# 返回基础声明对象
def getBaseDeclarative():
    return Base


# 初始化数据库
def initDatabase(engine):
    Base.metadata.create_all(engine)


# �?毁数据库
def destoryDatabase(engine):
    Base.metadata.drop_all(engine)
