"""
Xml 相关操作工具，包括 xml 文件的 key-value 更新与追加。
"""
import os
import xml.dom.minidom
from utils.LogUtils import Log

def update_xml_value(xml_path, keys, values):
    """
    更新或追加 <string> 节点。若 xml 文件不存在则跳过。若 key 已存在则替换，否则追加。
    :param xml_path:  xml 文件路径
    :param keys: Android key
    :param values: 多语言翻译值
    """
    Log.debug(f"--- updating xml: {xml_path}")
    # 检查 xml 文件是否存在
    if not os.path.exists(xml_path):
        Log.error(f"xml 文件不存在: {xml_path}")
        return

    # 解析 xml 文件
    xml_doc = xml.dom.minidom.parse(xml_path)
    # 获取所有 <string> 节点
    nodes = xml_doc.getElementsByTagName('string')
    # 遍历 keys，逐个处理
    for idx, key in enumerate(keys):
        found = False
        for node in nodes:
            # 获取 string name 属性
            xml_key = node.getAttribute("name")
            # 找到匹配的 key 且节点有内容
            if key == xml_key and node.firstChild is not None:
                # 替换内容为 values 中对应的值
                node.firstChild.data = str(values[idx])
                found = True
                break
        # 如果 xml 中没有该 key，则追加新节点
        if not found:
            new_node = xml_doc.createElement('string')
            new_node.setAttribute('name', key)
            new_text = xml_doc.createTextNode(str(values[idx]))
            new_node.appendChild(new_text)
            xml_doc.documentElement.appendChild(new_node)
            Log.info(f"追加新 key: {key} -> {values[idx]}")
    # 以二进制写入
    with open(xml_path, 'wb') as f:
        # 保存修改后的 xml 内容
        f.write(xml_doc.toxml('utf-8'))

def update_xml_string_array(xml_path, array_name, items):
    """
    更新或追加 <string-array> 节点。若 xml 文件不存在则跳过。若 key 已存在则替换，否则追加。
    <string-array name="xx">
        <!--数字-->
        <item>value</item>
    </string-array>
    :param xml_path: xml 文件路径
    :param array_name: 数组名
    :param items: [(index, value), ...]，按 index 排序。若缺少中间的某个 index 则展示为 <item />
    """
    Log.debug(f"--- updating string-array: {xml_path} name={array_name}")
    if not os.path.exists(xml_path):
        Log.error(f"xml 文件不存在: {xml_path}")
        return
    xml_doc = xml.dom.minidom.parse(xml_path)
    root = xml_doc.documentElement
    # 查找已存在的 string-array
    arrays = [n for n in root.getElementsByTagName('string-array') if n.getAttribute('name') == array_name]
    if arrays:
        arr_node = arrays[0]
        # 清空所有子节点（item、注释、文本等）
        while arr_node.firstChild:
            arr_node.removeChild(arr_node.firstChild)
    else:
        arr_node = xml_doc.createElement('string-array')
        arr_node.setAttribute('name', array_name)
        root.appendChild(arr_node)
    # 按 index 排序
    items_sorted = sorted(items, key=lambda x: x[0])
    indices = [idx for idx, _ in items_sorted]
    if not indices:
        return
    min_idx = min(indices)
    max_idx = max(indices)
    idx_map = {idx: value for idx, value in items_sorted}
    for idx in range(min_idx, max_idx + 1):
        # 添加换行和间隔（首项前也加）
        arr_node.appendChild(xml_doc.createTextNode('\n        '))
        # 添加注释 <!--数字-->
        comment = xml_doc.createComment(str(idx))
        arr_node.appendChild(comment)
        # 注释和 item 之间换行和间隔
        arr_node.appendChild(xml_doc.createTextNode('\n        '))
        item_node = xml_doc.createElement('item')
        if idx in idx_map:
            item_node.appendChild(xml_doc.createTextNode(str(idx_map[idx])))
        arr_node.appendChild(item_node)
    # 末尾换行和间隔
    arr_node.appendChild(xml_doc.createTextNode('\n    '))
    with open(xml_path, 'wb') as f:
        f.write(xml_doc.toxml('utf-8'))