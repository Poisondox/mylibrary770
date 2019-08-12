'''
Created on 2019年7月20日

@author: 55057
'''

import urllib.request
import re

from core.loggers import logger


class ISBNSearchEngine:

    def  __init__(self):
        logger.info('search engine initialize.....') 
        
    # 获取页面解析
    def __getPage(self, ISBN):
        url = 'http://opac.nlc.cn/F?func=find-b&find_code=ISB&request={}'.format(ISBN)
        # 构建查询地址串
        res = urllib.request.urlopen(url)
        # 获取网页内容并解码
        content = res.read().decode()
        # 确认是否有查询结果
        result = re.search('数据库里没有这条请求记录.', content)
        # 根据结果返回
        if result is  None:
            return content 
        else:
            return None
    
    # 解析页面内容
    def get_information_with_ISBN(self, ISBN):
        # 执行页面获取
        content = self.__getPage(ISBN)
        if content is None:
            logger.info('查询结果为空。')
            return -1
        else:
        # 进行搜索
            isbn_field = re.search(r'ISBN:(.*) * ', content, re.M | re.I)  # ISBN号    
            title_field = re.search(r'TITLE:(.*) * ', content, re.M | re.I)  # 书名
            author_field = re.search(r'AUTHOR:(.*) * ', content, re.M | re.I)  # 作者
            imprint_field = re.search(r'IMPRINT:(.*) * ', content, re.M | re.I)  # 出版社
            callon_field = re.search(r'CALL-NO:(.*) * ', content, re.M | re.I)  # 中文图书号  
            # 计算价格
            isbprice = isbn_field.group(1).__str__();
            isbprice = re.search(r'[0-9]*[.][0-9]*', isbprice, re.M | re.I)
            if isbprice:
                isbprice = isbprice.group().__str__()
            else:
                isbprice = 0
               
            # 书本信息汇总[标题，作者，出版社，中图分类号，价格]
            book_information = [title_field.group(1).__str__(), author_field.group(1).__str__(), imprint_field.group(1).__str__() \
                   , callon_field.group(1).__str__(), isbprice, \
                   isbn_field.group(1).__str__()]
            logger.info(book_information)
            return book_information 
        
