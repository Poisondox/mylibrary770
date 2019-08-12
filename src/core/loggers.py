'''
Created on 2019年8月11日

@author: 55057
'''

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 日志输出
logger = logging.getLogger(__name__)




#日志测试
if __name__ == '__main__':
    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail.")
    logger.info("Finish")

