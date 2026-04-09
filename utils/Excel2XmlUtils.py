"""
Excel 读取与批量写入 xml 的工具。
"""
import os
import csv
import re
from utils.XmlUtils import update_xml_value
from utils.LogUtils import Log
from collections import defaultdict
from utils.Str2XmlUtils import convert_str_to_xml
from utils.XmlUtils import update_xml_string_array

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
    """
    读取 Excel，每行以本行“所属模组”列为 xml 文件名，按各语言以Android Key 为 name 写入对应 xml。
    若缺少 “所属模组” 或 “Android Key” 列，报错提示且跳过。
    :param xml_path: xml 文件路径
    :param excel_path: 表格文件路径
    """
    # 读取 Excel 内容
    header, rows = read_excel(excel_path)
    try:
        # 获取“所属模组”列索引
        module_col_idx = header.index("所属模组")
    except ValueError:
        # 找不到列报错
        raise Exception("Excel 中未找到 所属模组 列")
    try:
        # 获取“Android Key”列索引
        key_col_idx = header.index("Android Key")
    except ValueError:
        # 找不到列报错
        raise Exception("Excel 中未找到 Android Key 列")

    # 语言列名与目录映射
    lang_map = {
        "英文（文案组）": ["values-en", "values"],  # Write to both values-en and values
        "Afar-aa(最长文案)": ["values-aa"],
        "bg-BG Bulgarian (保加利亚语)": ["values-bg"],
        "de-DE（德语）": ["values-de"],
        "es-ES（西班牙语）": ["values-es"],
        "fr-FR（法语）": ["values-fr"],
        "hu-HU Hungarian (匈牙利语)": ["values-hu"],
        "it-IT（意大利语）": ["values-it"],
        "lt-LT Lithuanian (立陶宛语)": ["values-lt"],
        "pt-PT（葡萄牙语）": ["values-pt"],
        "中文需求描述（CN）": ["values-zh"],
        "pl-PL（波兰语）": ["values-pl"],
        "nl-NL（荷兰语）": ["values-nl"],
        "no-NO（挪威语）": ["values-no"]
    }
    # 找到所有语言列的索引
    lang_col_map = {col: idx for idx, col in enumerate(header) if col in lang_map}
    # 普通 key 收集: {(file_path, lang): ([key], [value])}
    normal_kv = defaultdict(lambda: ([], []))
    # 数组项收集: {(file_path, lang, array_name): [(index, value)]}
    array_kv = defaultdict(list)

    # 遍历每一行数据
    for row in rows:
        # 获取所属模组
        module_value = row[module_col_idx].strip()
        # 获取 key
        key_value = row[key_col_idx].strip()
        # 跳过无效行
        if not module_value or not key_value or key_value == '仅适用于iOS':
            continue
        # 以所属模组命名 xml 文件
        xml_name = f"{module_value}.xml"
        # 遍历所有语言
        for lang, dir_names in lang_map.items():
            if lang not in lang_col_map:
                continue
            # 获取该行该语言的翻译内容
            value = row[lang_col_map[lang]]
            # 跳过无内容的语言
            if not value:
                continue
            value = convert_str_to_xml(value)
            for dir_name in dir_names:
                file_path = os.path.join(xml_path, dir_name, xml_name)
                # 支持 xx-INDEX-数字 形式，string-array name 取 xx
                array_key_match = re.match(r'^(.*?)(?:-INDEX)?-(\d+)$', key_value)
                if array_key_match:
                    base_key = array_key_match.group(1)
                    index = int(array_key_match.group(2))
                    array_kv[(file_path, base_key)].append((index, value))
                else:
                    normal_kv[file_path][0].append(key_value)
                    normal_kv[file_path][1].append(value)

    # 先写普通 key
    for file_path, (keys, values) in normal_kv.items():
        if keys:
            update_xml_value(file_path, keys, values)
            for k, v in zip(keys, values):
                Log.debug(f"写入 {file_path}，key={k}，value={v}")

    # 再写数组 key
    for (file_path, array_name), items in array_kv.items():
        if items:
            update_xml_string_array(file_path, array_name, items)
            Log.debug(f"写入 {file_path}，string-array name={array_name}，items={items}")

def get_all_xml_files_from_excel(xml_path, excel_path):
    """
    获取表格中所有涉及的 xml 文件路径。
    :param xml_path: xml 文件根目录
    :param excel_path: 表格文件路径
    :return: set of xml file paths
    """
    header, rows = read_excel(excel_path)
    try:
        module_col_idx = header.index("所属模组")
    except ValueError:
        raise Exception("Excel 中未找到 所属模组 列")
    lang_map = {
        "英文（文案组）": ["values-en", "values"],
        "Afar-aa(最长文案)": ["values-aa"],
        "bg-BG Bulgarian (保加利亚语)": ["values-bg"],
        "de-DE（德语）": ["values-de"],
        "es-ES（西班牙语）": ["values-es"],
        "fr-FR（法语）": ["values-fr"],
        "hu-HU Hungarian (匈牙利语)": ["values-hu"],
        "it-IT（意大利语）": ["values-it"],
        "lt-LT Lithuanian (立陶宛语)": ["values-lt"],
        "pt-PT（葡萄牙语）": ["values-pt"],
        "中文需求描述（CN）": ["values-zh"],
        "pl-PL（波兰语）": ["values-pl"],
        "nl-NL（荷兰语）": ["values-nl"],
        "no-NO（挪威语）": ["values-no"]
    }
    lang_col_map = {col: idx for idx, col in enumerate(header) if col in lang_map}
    xml_files = set()
    for row in rows:
        module_value = row[module_col_idx].strip()
        if not module_value:
            continue
        xml_name = f"{module_value}.xml"
        for lang, dir_names in lang_map.items():
            if lang not in lang_col_map:
                continue
            for dir_name in dir_names:
                file_path = os.path.join(xml_path, dir_name, xml_name)
                xml_files.add(file_path)
    return xml_files
