# -*- coding:utf-8 -*-
import Constant
from utils.LogUtils import Log

def excel2xml(xmlDirPath, xlsPath):


    import os
    from utils.ParseUtils import XMLParse
    ext = os.path.splitext(xlsPath)[1].lower()
    header = []
    rows = []
    if ext == '.xls':
        import xlrd
        workbook = xlrd.open_workbook(xlsPath)
        sheet = workbook.sheet_by_index(0)
        header = sheet.row_values(0)
        for row_idx in range(1, sheet.nrows):
            rows.append(sheet.row_values(row_idx))
    elif ext == '.xlsx':
        try:
            import openpyxl
        except ImportError:
            raise ImportError('请先 pip install openpyxl')
        wb = openpyxl.load_workbook(xlsPath, read_only=True, data_only=True)
        ws = wb.active
        for i, row in enumerate(ws.iter_rows(values_only=True)):
            if i == 0:
                header = [str(cell) if cell is not None else '' for cell in row]
            else:
                rows.append([str(cell) if cell is not None else '' for cell in row])
    else:
        raise Exception('仅支持 .xls 或 .xlsx 文件')

    try:
        key_col_idx = header.index("Android Key")
    except ValueError:
        raise Exception("Excel中未找到‘Android Key’列")

    try:
        module_col_idx = header.index("所属模组")
    except ValueError:
        raise Exception("Excel中未找到‘所属模组’列")

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
    lang_col_map = {}
    for idx, col_name in enumerate(header):
        if col_name in lang_map:
            lang_col_map[col_name] = idx

    for row in rows:
        module_value = str(row[module_col_idx]).strip()
        key_value = str(row[key_col_idx]).strip()
        if not module_value or not key_value:
            continue
        xmlName = f"{module_value}.xml"
        for lang, dir_name in lang_map.items():
            if lang not in lang_col_map:
                continue
            value = row[lang_col_map[lang]]
            if value is None or value == "":
                continue
            filePath = f"{xmlDirPath}/{dir_name}/{xmlName}"
            XMLParse.update_xml_value(filePath, [key_value], [value])
            Log.debug(f"写入 {filePath}，key={key_value}，value={value}")

def main():
    Constant.Config.import_start_col = 2
    Constant.Config.import_base_xml = False
    Constant.Config.support_custom_ph_rule = True

    excel2xml("/Users/ninebot/Desktop/after_sale_app/development/android-mowerpdi/commonres/src/main/res",
               "/Users/ninebot/Desktop/after_sale_app/MultilingualTranslation/strings1.xls")

main()
