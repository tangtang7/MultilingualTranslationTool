#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import re
from loguru import logger

from Constant import Config


class Log:
    """Log util"""

    current = ""
    # Log info green
    @staticmethod
    def debug(msg):
        # if Log.current != "info":
        #     print('\033[32m')
        #     Log.current = "info"
        #
        # print(f'DEBUG: {msg}')
        logger.debug(msg)

    # Log error red
    @staticmethod
    def error(msg):
        # if Log.current != "error":
        #     print('\033[31m')
        #     Log.current = "error"
        # print(f'ERROR: {msg}')
        logger.error(msg)

    @staticmethod
    def warn(msg):
        # if Log.current != "warn":
        #     print('\033[34m')
        #     Log.current = "warn"
        # print(f'WARN: {msg}')
        logger.warning(msg)

    # Log info white
    @staticmethod
    def info(msg):
        if Config.isShowInfo:
            logger.info(msg)
        #     if Log.current != "debug":
        #         print('\033[37m')
        #         Log.current = "debug"
        #     print(f'INFO: {msg}')

def test_replace_quotation_to_xml(base_str, change_word):
    new_str = ''
    while change_word in base_str:
        start = base_str.find(change_word)
        new_str += base_str[:start + 1] + "\\" + base_str[start + 1:start + 2]
        base_str = base_str[start + 2:]
    new_str += base_str
    return new_str

if __name__ == '__main__':
    Log.info("你好")
    Log.debug("debug")
    Log.warn("warn")
    Log.error("error")
