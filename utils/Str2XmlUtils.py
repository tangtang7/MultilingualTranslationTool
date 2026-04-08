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
    pattern = re.compile(r'\$\$\d[a-zA-Z]')
    replace_list = pattern.findall(base_str)
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
    pattern4 = re.compile(r'[^\\]\"')
    replace_list4 = pattern4.findall(temp_result3)
    temp_result4 = temp_result3
    for replace in replace_list4:
        temp_result4 = replace_quotation_to_xml(temp_result4, replace)

    # 匹配未转义的 &quot;
    pattern5 = re.compile(r'[^\\]&quot;')
    replace_list5 = pattern5.findall(temp_result4)
    temp_result5 = temp_result4
    for replace in replace_list5:
        temp_result5 = replace_quotation_to_xml(temp_result5, replace)

    # 删除字符串结尾的换行和空白符号
    pattern6 = re.compile(r'(\n$)|(\s$)')
    temp_result6 = re.sub(pattern6, "", temp_result5)

    # 将换行符替换为 \\n 和 n
    pattern7 = re.compile(r'\n')
    enter1 = "\\\n"
    enter2 = "n"
    temp_result7 = re.subn(pattern7, enter1, temp_result6)[0]
    temp_result8 = re.subn(pattern7, enter2, temp_result7)[0]

    # 将非换行空格替换为普通空格
    pattern8 = re.compile(r'\xa0')
    temp_result9 = re.sub(pattern8, " ", temp_result8)
    return temp_result9

# 下面注释掉的是历史处理逻辑，保留以便后续扩展
# # 将 "（未转义的"） 替换为 \"
# pattern6 = re.compile(r'[^\\](“)')
# replace_list6 = pattern6.findall(temp_result5)
# temp_result6 = temp_result5
# for replace in replace_list6:
#     temp_result6 = replace_quotation_to_xml(temp_result6, replace)
#
# # 将 "（未转义的"） 替换为 \"
# pattern7 = re.compile(r'[^\\](”)')
# replace_list7 = pattern7.findall(temp_result6)
# temp_result7 = temp_result6
# for replace in replace_list7:
#     temp_result7 = replace_quotation_to_xml(temp_result7, replace)
#
# # 将 "（未转义的"） 替换为 \"
# pattern8 = re.compile(r'[^\\](‘)')
# replace_list8 = pattern8.findall(temp_result7)
# temp_result8 = temp_result7
# for replace in replace_list8:
#     temp_result8 = replace_quotation_to_xml(temp_result8, replace)
#
# # 将 "（未转义的"） 替换为 \"
# pattern9 = re.compile(r'[^\\](’)')
# replace_list9 = pattern9.findall(temp_result8)
# temp_result9 = temp_result8
# for replace in replace_list9:
#     temp_result9 = replace_quotation_to_xml(temp_result9, replace)
#
# # 删除字符串结尾的换行和空白符号
# pattern10 = re.compile(r'(\n$)|(\s$)')
# # 字符串开头的空白符号暂时保留
# # pattern6 = re.compile(r'(^\s)|(\n$)|(\s$)')
# temp_result10 = re.sub(pattern10, "", temp_result9)
#
# # 将 换行符 替换为 \n
# pattern11 = re.compile(r'\n')
# enter1 = "\\\n"
# enter2 = "n"
# temp_result11 = re.subn(pattern11, enter1, temp_result10)[0]
# temp_result12 = re.subn(pattern11, enter2, temp_result11)[0]
#
# # 将 非换行空格 替换为 普通空格
# pattern12 = re.compile(r' ')
# temp_result13 = re.sub(pattern12, " ", temp_result12)
# return temp_result13