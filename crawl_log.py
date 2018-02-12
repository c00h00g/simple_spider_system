#-*- coding:utf-8 -*-

"""
the module provides the methods how to print log
"""

import logging

logger = logging.getLogger('mini_crawl.log')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("mini_crawl.log")
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def WARNING_LOG(msg, *args, **kwargs):
    """print a warning log
    """
    logger.warning(msg, *args, **kwargs)


def ERROR_LOG(msg, *args, **kwargs):
    """print a error log
    """
    logger.error(msg, *args, **kwargs)


def INFO_LOG(msg, *args, **kwargs):
    """print a info log
    """
    logger.info(msg, *args, **kwargs)

