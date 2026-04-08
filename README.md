# MultilingualTranslationTool

多语翻译一键导入工具

---

## 功能简介

- 支持将 Excel（.xls/.xlsx）每行内容批量导入到多语言 Android xml 文件中。
- 自动追加或更新 xml 文件中的 string key。
- 支持占位符/格式化字符串自动转换（如 $$1s → %1$s）。
- 仅依赖 Python 标准库、xlrd、openpyxl，无其它冗余依赖。

## 依赖环境

- Python 3.x  
  安装方式：已内置于大多数操作系统，或访问 https://www.python.org/downloads/ 下载
- [xlrd](https://pypi.org/project/xlrd/)（用于读取 .xls 格式的 Excel 文件）  
  安装命令：`pip install xlrd`
- [openpyxl](https://pypi.org/project/openpyxl/)（用于读取 .xlsx 格式的 Excel 文件）  
  安装命令：`pip install openpyxl`

### 安装依赖

```bash
pip install xlrd openpyxl
```

## 目录结构说明

- `MowerPdiCovert.py`：主程序，仅包含主入口，调用 excel2xml 进行批量导入。
- `utils/Excel2XmlUtils.py`：Excel 读取与批量写入 xml 的工具。
- `utils/Str2XmlUtils.py`：表格字符串转换为 Android 格式字符串工具。
- `utils/XmlUtils.py`：Xml 相关操作工具，包括 xml 文件的 key-value 更新与追加。
- `utils/LogUtils.py`：日志工具。

## 使用方法

1. 配置 Excel 文件路径和目标 xml 目录（在 `MowerPdiCovert.py` 的 `main()` 函数中）。
2. 运行主程序：

```bash
python MowerPdiCovert.py
```

## 注意事项

- 仅支持 `.xls` 和 `.xlsx` 格式的 Excel 文件。
- Excel 表头需包含“所属模组”和“Android Key”两列。
- 语言列名需与代码中的 `lang_map` 保持一致。
- 若 xml 文件不存在 key，则自动追加。
- 所有 value 在写入 xml 前会自动进行占位符/格式化字符串转换（如 $$1s → %1$s）。

## 常见问题

- 如果运行时报 `ImportError: No module named 'xlrd'` 或 `No module named 'openpyxl'`，请先安装依赖。
- 如遇其它问题请联系维护者。

---
