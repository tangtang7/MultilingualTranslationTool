"""
Xml 相关操作工具，包括 xml 文件的 key-value 更新与追加。
"""
import os
import xml.dom.minidom
from utils.LogUtils import Log

#
def update_xml_value(xml_path, keys, values):
    """
    更新指定 xml 文件，xml 文件不存在则跳过。更新 key-value，如果没有该 key，则追加新节点。
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
