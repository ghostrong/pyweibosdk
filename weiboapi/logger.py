#coding=utf8

import logging
import logging.handlers

def get_logger(name):
    # the name should be an absolute path name
    handler = logging.handlers.RotatingFileHandler(name)
    # the format of log
    fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.addHandler(handler)

    # 输入的loglevel越小，忽略的信息越多，log记录的内容越少
    levels = [logging.CRITICAL, logging.ERROR, logging.WARNING, logging.INFO, logging.DEBUG]
    loglevel = levels[-1]  # log the most
    logger.setLevel(loglevel)
    return logger

if __name__ == '__main__':
    logger = get_logger('test')
    logger.critical('this is my first test log.')
