'''
Created on 2019年8月11日

@author: 55057
'''

import configparser
from core.loggers import logger

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
    configpsr.read(file_path)
    connect_str = '%s://%s:%s@%s:%s/%s'%(configpsr['db_cfg']['db_type'],
                                  configpsr['db_cfg']['user'],
                                  configpsr['db_cfg']['password'],
                                  configpsr['db_cfg']['ipaddr'],
                                  configpsr['db_cfg']['port'],
                                  configpsr['db_cfg']['dbname'])
    
    #日志输出
    logger.info('connect str is: '+connect_str)
    #获取连接串
    return connect_str


if __name__ == '__main__':
    #initDatabaseCfgFile()
    logger.info(getConfigFromFile('db_cfg.ini'))
