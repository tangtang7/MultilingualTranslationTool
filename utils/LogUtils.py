# -*- coding:utf-8 -*-
"""
日志工具类，支持 debug/info/error。
"""
class Log:
    @staticmethod
    def debug(msg):
        print("[DEBUG]", msg)
    @staticmethod
    def error(msg):
        print("[ERROR]", msg)
    @staticmethod
    def info(msg):
        print("[INFO]", msg)

