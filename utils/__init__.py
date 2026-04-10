# -*- coding:utf-8 -*-
"""utils 工具包初始化文件。

该文件存在可确保 `utils` 目录被 Python 识别为包，从而支持：

    from utils.Excel2XmlUtils import ...

同时，这里提供少量 Python2/3 兼容定义，供项目内部统一使用。
"""

# 用于区分 Python 2/3
import sys

# 是否 Python2
PY2 = sys.version_info[0] == 2

# 统一字符串类型：
# - Python2: basestring / unicode
# - Python3: str
if PY2:
    text_type = unicode  # noqa: F821
    string_types = (basestring,)  # noqa: F821
else:
    text_type = str
    string_types = (str,)


def to_text(value, encoding='utf-8', errors='ignore'):
    """将任意对象转换为文本字符串（Py2 返回 unicode，Py3 返回 str）。"""
    if value is None:
        return text_type('')
    if isinstance(value, text_type):
        return value
    # Python2 下可能出现 str(bytes)
    try:
        if PY2 and isinstance(value, str):
            return value.decode(encoding, errors)
    except Exception:
        pass
    try:
        return text_type(value)
    except Exception:
        try:
            return text_type(repr(value))
        except Exception:
            return text_type('')

