'''
Created on 2019年8月11日

@author: 55057
'''

import configparser

#初始化配置解析类
configpsr = configparser.ConfigParser()

#初始化配置文件
def initDatabaseCfgFile():
    configpsr.read_dict(   {
                'db_cfg': {'db_type': 'postgresql',
                                    'user': 'sa',
                                    'password': 'sa',
                                    'ipaddr': '0.0.0.0',
                                    'port': '5432',
                                    'dbname': 'db'}})
with open('db_cfg.ini', 'w') as configfile:
    configpsr.write(configfile)
    


#从文件中获取连接字符串
def getConfigFromFile(file_path):
    return
    