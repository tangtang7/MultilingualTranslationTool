"""
Excel 读取与批量写入 xml 的工具。
"""
import os
import csv
from utils.XmlUtils import update_xml_value
from utils.LogUtils import Log

def read_excel(excel_path):
    """
    读取 .xls、.xlsx 或 .csv 文件，返回 header, rows（表头，数据行）
    :param excel_path: 表格文件路径
    :return: header, rows（表头，数据行）
    """
    # 获取文件扩展名
    ext = os.path.splitext(excel_path)[1].lower()
    # 初始化表头和数据行。取表格第一行为表头，其余为数据行
    header, rows = [], []
    # xlrd 处理 .xls 文件。
    if ext == '.xls':
        import xlrd
        wb = xlrd.open_workbook(excel_path)
        sheet = wb.sheet_by_index(0)
        header = [str(x) for x in sheet.row_values(0)]
        for i in range(1, sheet.nrows):
            rows.append([str(x) for x in sheet.row_values(i)])
    # openpyxl 处理 .xlsx 文件
    elif ext == '.xlsx':
        import openpyxl
        # 只读方式打开
        wb = openpyxl.load_workbook(excel_path, read_only=True, data_only=True)
        ws = wb.active
        for i, row in enumerate(ws.iter_rows(values_only=True)):
            if i == 0:
                header = [str(cell) if cell is not None else '' for cell in row]
            else:
                rows.append([str(cell) if cell is not None else '' for cell in row])
    # csv 处理 .csv 文件
    elif ext == '.csv':
        with open(excel_path, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i == 0:
                    header = [str(cell) if cell is not None else '' for cell in row]
                else:
                    rows.append([str(cell) if cell is not None else '' for cell in row])
    # 不支持的格式报错
    else:
        raise Exception('仅支持 .xls、.xlsx 或 .csv 文件')
    return header, rows

# 读取 Excel，每行以本行“所属模组”为 xml 文件名，按各语言写入对应 xml。
def excel2xml(xml_path, excel_path):
    # 读取 Excel 内容
    header, rows = read_excel(excel_path)
    try:
        # 获取“所属模组”列索引
        module_col_idx = header.index("所属模组")
    except ValueError:
        # 找不到列报错
        raise Exception("Excel中未找到 所属模组 列")
    try:
        # 获取“Android Key”列索引
        key_col_idx = header.index("Android Key")
    except ValueError:
        # 找不到列报错
        raise Exception("Excel中未找到 Android Key 列")

    # 语言列名与目录映射
    lang_map = {
        "英文（文案组）": "values-en",
        "Afar-aa(最长文案)": "values-aa",
        "bg-BG Bulgarian (保加利亚语)": "values-bg",
        "de-DE（德语）": "values-de",
        "es-ES（西班牙语）": "values-es",
        "fr-FR（法语）": "values-fr",
        "hu-HU Hungarian (匈牙利语)": "values-hu",
        "it-IT（意大利语）": "values-it",
        "lt-LT Lithuanian (立陶宛语)": "values-lt",
        "pt-PT（葡萄牙语）": "values-pt",
        "中文需求描述（CN）": "values-zh",
        "pl-PL（波兰语）": "values-pl",
        "nl-NL（荷兰语）": "values-nl",
        "no-NO（挪威语）": "values-no"
    }
    # 找到所有语言列的索引
    lang_col_map = {col: idx for idx, col in enumerate(header) if col in lang_map}

    # 遍历每一行数据
    for row in rows:
        # 获取所属模组
        module_value = row[module_col_idx].strip()
        # 获取 key
        key_value = row[key_col_idx].strip()
        # 跳过无效行
        if not module_value or not key_value:
            continue
        # 以所属模组命名 xml 文件
        xml_name = f"{module_value}.xml"
        # 遍历所有语言
        for lang, dir_name in lang_map.items():
            if lang not in lang_col_map:
                continue
            # 获取该行该语言的翻译内容
            value = row[lang_col_map[lang]]
            # 跳过无内容的语言
            if not value:
                continue
            # 占位符/格式化字符串自动转换（如 $$1s → %1$s）
            from utils.Str2XmlUtils import convert_str_to_xml
            value = convert_str_to_xml(value)
            # 组装 xml 文件路径
            file_path = os.path.join(xml_path, dir_name, xml_name)
            # 写入 key-value
            update_xml_value(file_path, [key_value], [value])
            # 日志记录
            Log.debug(f"写入 {file_path}，key={key_value}，value={value}")