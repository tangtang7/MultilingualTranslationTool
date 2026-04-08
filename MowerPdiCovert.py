"""
将 Excel 每行内容写入对应 xml 文件，实现多语言批量导入。
"""

# 主入口，配置路径并执行 excel2xml
from utils.Excel2XmlUtils import excel2xml

def main():
    # xml 目录
    xml_path = "/Users/ninebot/Desktop/after_sale_app/development/android-mowerpdi/commonres/src/main/res"
    # Excel 文件路径
    excel_path = "/Users/ninebot/Desktop/after_sale_app/MultilingualTranslation/strings2.xlsx"
    # 执行批量导入
    excel2xml(xml_path, excel_path)

# 程序入口
if __name__ == "__main__":
    main()
