# -*- coding:utf-8 -*-
"""
将 Excel 每行内容写入对应 xml 文件，实现多语言批量导入。
"""
from utils.Excel2XmlUtils import excel2xml, get_all_xml_files_from_excel
from utils.XmlUtils import sort_xml_strings_and_arrays

def main():
    # xml 目录
    xml_path = "/Users/ninebot/Desktop/after_sale_app/development/android-mowerpdi/commonres/src/main/res"
    # 表格文件路径
    # excel_path = "/Users/ninebot/Desktop/after_sale_app/MultilingualTranslation/s1.xls"
    # excel_path = "/Users/ninebot/Desktop/after_sale_app/MultilingualTranslation/s2.xlsx"
    excel_path = "/Users/ninebot/Desktop/after_sale_app/MultilingualTranslation/s3.csv"
    # 执行批量导入
    excel2xml(xml_path, excel_path)
    # 执行批量排序
    sort_xml_files_batch(xml_path, excel_path)

def sort_xml_files_batch(xml_path, excel_path):
    """
    批量对 excel 文件所有涉及的 xml 文件进行排序。
    :param xml_path: xml 文件根目录
    :param excel_path: 表格文件路径
    """
    xml_file_list = get_all_xml_files_from_excel(xml_path, excel_path)
    for file_path in xml_file_list:
        sort_xml_strings_and_arrays(file_path)

# 程序入口
if __name__ == "__main__":
    main()
