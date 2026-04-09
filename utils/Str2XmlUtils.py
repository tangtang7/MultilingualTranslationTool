"""
表格字符串转换为 Android 格式字符串工具。
"""
# 导入正则表达式模块
import re

def change_str_to_xml(base_str):
    """
    将表格占位符转换为 Android 占位符
    :param base_str: 输入字符串，格式: $$1s or $$s
    :return: 转换后的字符串，格式: %1$s or %s
    """
    new_str = '%'
    new_str += base_str[2]
    if len(base_str) == 4:
        new_str += '$' + base_str[3]
    return new_str

def replace_placeholder_to_xml(base_str, change_word):
    """
    将 base_str 中需要替代的字符（change_word）替换成需要的格式
    :param base_str: 源字符串
    :param change_word: 需要替换的字符
    :return: 转换后的字符串
    """
    new_str = ''
    if len(change_word) == 4:
        while change_word in base_str:
            start = base_str.find(change_word)
            new_str += base_str[:start] + change_str_to_xml(base_str[start:start + 4])
            base_str = base_str[start + 4:]
    elif len(change_word) == 3:
        while change_word in base_str:
            start = base_str.find(change_word)
            new_str += base_str[:start] + change_str_to_xml(base_str[start:start + 3])
            base_str = base_str[start + 3:]
    new_str += base_str
    return new_str

def replace_quotation_to_xml(base_str, change_word):
    """
    将 base_str 中需要替代的内容（change_word）替换成加转义符的引号
    :param base_str: 源字符串
    :param change_word: 需要替换的不含转义符的引号
    :return: 替换后的字符串
    """
    new_str = ''
    while change_word in base_str:
        start = base_str.find(change_word)
        new_str += base_str[:start + 1] + "\\" + base_str[start + 1:start + 2]
        base_str = base_str[start + 2:]
    new_str += base_str
    return new_str

def convert_str_to_xml(base_str) -> str:
    """
    将字符串中的占位符、引号、换行等进行批量转换
    :param base_str: 输入字符串
    :return: 转换后的字符串
    """
    # 匹配 $$1s 形式的占位符
    pattern1 = re.compile(r'\$\$\d[a-zA-Z]')
    replace_list = pattern1.findall(base_str)
    temp_result1 = base_str
    for replace in replace_list:
        temp_result1 = replace_placeholder_to_xml(temp_result1, replace)

    # 匹配 $$s 形式的占位符
    pattern2 = re.compile(r'\$\$[a-zA-Z]')
    replace_list2 = pattern2.findall(temp_result1)
    temp_result2 = temp_result1
    for replace in replace_list2:
        temp_result2 = replace_placeholder_to_xml(temp_result2, replace)

    # 匹配未转义的单引号
    pattern3 = re.compile(r'[^\\]\'')
    replace_list3 = pattern3.findall(temp_result2)
    temp_result3 = temp_result2
    for replace in replace_list3:
        temp_result3 = replace_quotation_to_xml(temp_result3, replace)

    # 匹配未转义的双引号
    pattern4 = re.compile(r'[^\\]"')
    replace_list4 = pattern4.findall(temp_result3)
    temp_result4 = temp_result3
    for replace in replace_list4:
        temp_result4 = replace_quotation_to_xml(temp_result4, replace)

    # 匹配未转义的 &quot;
    pattern5 = re.compile(r'[^\\]&quot;')
    replace_list5 = pattern5.findall(temp_result4)
    temp_result6 = temp_result4
    for replace in replace_list5:
        temp_result6 = replace_quotation_to_xml(temp_result6, replace)

    # 将未转义的“”‘’ 替换为 \“\”\‘\’
    # pattern6 = re.compile(r'[^\\]([“”‘’])')
    # replace_list6 = pattern6.findall(temp_result5)
    # temp_result6 = temp_result5
    # for replace in replace_list6:
    #     temp_result6 = replace_quotation_to_xml(temp_result6, replace)

    # 将非换行空格替换为普通空格
    pattern7 = re.compile(r'[\xa0\u00a0]')
    temp_result7 = re.sub(pattern7, " ", temp_result6)

    # 删除字符串结尾的空白符号（包括空格、制表符、回车、换行）
    pattern8 = re.compile(r'[ \t\r\n]+$')
    temp_result9 = re.sub(pattern8, "", temp_result7)

    # 删除字符串开头的换行和空白符号
    # pattern9 = re.compile(r'(^\s)|(\n$)|(\s$)')
    # temp_result9 = re.sub(pattern9, "", temp_result8)

    # 将换行符替换为 \\n 和 n
    pattern10 = re.compile(r'\n')
    enter1 = "\\\n"
    enter2 = "n"
    temp_result10 = re.subn(pattern10, enter1, temp_result9)[0]
    temp_result11 = re.subn(pattern10, enter2, temp_result10)[0]
    return temp_result11