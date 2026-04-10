# -*- coding:utf-8 -*-
"""
日志工具类，支持 debug/info/error。
"""
import sys


def _safe_text(msg):
    """将日志内容转换为可输出的文本；在 Python2 下尽量避免 UnicodeEncodeError。"""
    try:
        # Python2
        if sys.version_info[0] == 2:
            if isinstance(msg, unicode):  # noqa: F821
                return msg.encode('utf-8')
        return msg
    except Exception:
        try:
            return str(msg)
        except Exception:
            return ''


class Log:
    @staticmethod
    def debug(msg):
        print("[DEBUG] %s" % _safe_text(msg))
    @staticmethod
    def error(msg):
        print("[ERROR] %s" % _safe_text(msg))
    @staticmethod
    def info(msg):
        print("[INFO] %s" % _safe_text(msg))

