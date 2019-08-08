'''
Created on 2019年8月7日

@author: 55057
'''
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from ORM_model.decBaseClass import initDatabase, destoryDatabase, Book
from contextlib import contextmanager
import time

#初始化数据库连接
sql_engine = create_engine('postgresql://sa:xyq566403@192.168.3.88:5432/librarydb',echo=True)
#初始化数据库实例session
sessionType = scoped_session(sessionmaker(bind=sql_engine))
#销毁数据库
destoryDatabase(sql_engine)
#初始化数据库
initDatabase(sql_engine)

#获取session实例操作数据库
def getSession():
    return sessionType()

#数据通过ORM手段写入数据库，方法实现于此文件
@contextmanager
def session_flow():
    
    session = getSession()
    
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise 
    finally:
        session.close()
        
        
#单本图书插入
def InsertBookData(isbn,ibook_name,ibook_author,ibook_publisher,ibook_number,ibook_price,ibook_notes,ibook_storoge_time):
    with session_flow() as temp_session:
        book = Book(ISBN=isbn,book_name=ibook_name,book_author=ibook_author,
                    book_publisher=ibook_publisher,book_number=ibook_number,
                    book_price=ibook_price,book_notes=ibook_notes,
                    book_storoge_time=ibook_storoge_time)
        #录入图书数据
        temp_session.add(book)

def InsertBook(ibook):
    with session_flow() as temp_session:
        temp_session.add(ibook)
        
    


#图书批量插入
def InsertBatchBooks(booklist):
    with session_flow() as temp_session:
        #全部写入session
        temp_session.add_all(booklist)
        
        
        
        

if __name__ == '__main__':
    InsertBookData('123', '韭菜的自我修养', '刘苗苗', '豌豆苗出版社', '瞎编的', 98.56, None, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))        
        


