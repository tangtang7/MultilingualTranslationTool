# MultilingualTranslationTool

多语翻译一键导入工具

---

## 功能简介

- 支持将表格（`.xls` / `.xlsx` / `.csv`）每行内容批量导入到多语言 Android xml 文件中。
- 自动追加或更新 xml 文件中的 string key。
- 每行使用表格中的“所属模组”列作为输出 xml 文件名（如 `所属模组=strings_device` → `strings_device.xml`）。
- 支持将 `xx-INDEX-1` / `xx-1` 等形式的 Android Key 写入为 `<string-array name="xx">`（按数字排序写入）。
- 仅依赖 Python 标准库、`xlrd`、`openpyxl`，无其它冗余依赖。

## 依赖环境

- Python 2.7+（当前工程代码兼容 Python 2.7 与 Python 3）
  - macOS 可能默认 `python` 指向 Python 2.7，可用 `python --version` 查看
  - 若你的环境使用 Python 3，请用 `python3` 执行脚本
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

1. 配置表格文件路径和目标 `res` 目录（在 `MowerPdiCovert.py` 的 `main()` 函数中）。
2. 可选：配置 `module_filter`，仅处理指定“所属模组”（支持：单个字符串或字符串数组）。
3. 运行主程序：
    ```bash
    python MowerPdiCovert.py
    ```

## 注意事项

- 支持 `.xls`、`.xlsx` 和 `.csv` 格式的表格文件。
- 表头需包含“所属模组”和“Android Key”两列。
- 语言列名需与代码中的 `lang_map` 保持一致。
- 若某行 `Android Key` 内容为 空或`仅适用于iOS`，该行会被跳过且不报错。
- 若 xml 文件不存在 key，则自动追加；已存在则更新。
- `英文（文案组）` 列会同时写入 `values-en` 和 `values` 两个目录。
- `module_filter` 说明：
  - `None` / 空字符串：处理所有模组（默认）
  - 字符串：仅处理该模组（例如：`"strings_device"`）
  - 字符串数组：仅处理这些模组（例如：`["strings_device", "strings_yaml"]`）
- value 写入时会自动进行占位符转换（如 `%s` → `%1$s`）和特殊字符转义（如 `&` → `&amp;`）。

## 常见问题

- 如果运行时报 `ImportError: No module named 'xlrd'` 或 `No module named 'openpyxl'`，请先安装依赖。
- 如遇其它问题请联系维护者。

---
