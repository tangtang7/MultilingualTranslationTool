# -*- coding:utf-8 -*-
import Constant
from Excel2XmlUtil import Excel2XmlUtils


def excelToxml(xmlDirPath, xlsPath):
    excel2XmlUtils = Excel2XmlUtils()

    deviceXmlName = "strings_device.xml"
    yamlXmlName = "strings_yaml.xml"
    mowerXmlName = "strings_i2_LiDAR.xml"

    xmlName = deviceXmlName
    filePath = xmlDirPath + "/values/" + xmlName
    filePathaa = xmlDirPath + "/values-aa/" + xmlName
    filePathbg = xmlDirPath + "/values-bg/" + xmlName
    filePathde = xmlDirPath + "/values-de/" + xmlName
    filePathen = xmlDirPath + "/values-en/" + xmlName
    filePathes = xmlDirPath + "/values-es/" + xmlName
    filePathfr = xmlDirPath + "/values-fr/" + xmlName
    filePathhu = xmlDirPath + "/values-hu/" + xmlName
    filePathit = xmlDirPath + "/values-it/" + xmlName
    filePathlt = xmlDirPath + "/values-lt/" + xmlName
    filePathpt = xmlDirPath + "/values-pt/" + xmlName
    filePathzh = xmlDirPath + "/values-zh/" + xmlName
    filePathpl = xmlDirPath + "/values-pl/" + xmlName
    filePathnl = xmlDirPath + "/values-nl/" + xmlName

    excel2XmlUtils.xls2xml(xlsPath, filePath, "英文（文案组）", None)
    excel2XmlUtils.xls2xml(xlsPath, filePathaa, "Afar-aa(最长文案)", None)
    excel2XmlUtils.xls2xml(xlsPath, filePathbg, "bg-BG Bulgarian (保加利亚语)", None)
    excel2XmlUtils.xls2xml(xlsPath, filePathde, "de-DE（德语）", None)
    excel2XmlUtils.xls2xml(xlsPath, filePathen, "英文（文案组）", None)
    excel2XmlUtils.xls2xml(xlsPath, filePathes, "es-ES（西班牙语）", None)
    excel2XmlUtils.xls2xml(xlsPath, filePathfr, "fr-FR（法语）", None)
    excel2XmlUtils.xls2xml(xlsPath, filePathhu, "hu-HU Hungarian (匈牙利语)", None)
    excel2XmlUtils.xls2xml(xlsPath, filePathit, "it-IT（意大利语）", None)
    excel2XmlUtils.xls2xml(xlsPath, filePathlt, "lt-LT Lithuanian (立陶宛语)", None)
    excel2XmlUtils.xls2xml(xlsPath, filePathpt, "pt-PT（葡萄牙语）", None)
    excel2XmlUtils.xls2xml(xlsPath, filePathzh, "中文需求描述（CN）", None)
    excel2XmlUtils.xls2xml(xlsPath, filePathpl, "pl-PL（波兰语）", None)
    excel2XmlUtils.xls2xml(xlsPath, filePathnl, "nl-NL（荷兰语）", None)

    # dirPath = xmlDirPath + "/values/"
    # dirPathaa = xmlDirPath + "/values-aa/"
    # dirPathbg = xmlDirPath + "/values-bg/"
    # dirPathde = xmlDirPath + "/values-de/"
    # dirPathen = xmlDirPath + "/values-en/"
    # dirPathes = xmlDirPath + "/values-es/"
    # dirPathfr = xmlDirPath + "/values-fr/"
    # dirPathhu = xmlDirPath + "/values-hu/"
    # dirPathit = xmlDirPath + "/values-it/"
    # dirPathlt = xmlDirPath + "/values-lt/"
    # dirPathpt = xmlDirPath + "/values-pt/"
    # dirPathzh = xmlDirPath + "/values-zh/"
    # dirPathpl = xmlDirPath + "/values-pl/"
    # dirPathnl = xmlDirPath + "/values-nl/"
    #
    # # 共 13 个文件
    # excel2XmlUtils.xls2xml(xlsPath, None, "英文（文案组）", dirPath)
    # excel2XmlUtils.xls2xml(xlsPath, None, "Afar-aa(最长文案)", dirPathaa)
    # excel2XmlUtils.xls2xml(xlsPath, None, "bg-BG Bulgarian (保加利亚语)", dirPathbg)
    # excel2XmlUtils.xls2xml(xlsPath, None, "de-DE（德语）", dirPathde)
    # excel2XmlUtils.xls2xml(xlsPath, None, "英文（文案组）", dirPathen)
    # excel2XmlUtils.xls2xml(xlsPath, None, "es-ES（西班牙语）", dirPathes)
    # excel2XmlUtils.xls2xml(xlsPath, None, "fr-FR（法语）", dirPathfr)
    # excel2XmlUtils.xls2xml(xlsPath, None, "hu-HU Hungarian (匈牙利语)", dirPathhu)
    # excel2XmlUtils.xls2xml(xlsPath, None, "it-IT（意大利语）", dirPathit)
    # excel2XmlUtils.xls2xml(xlsPath, None, "lt-LT Lithuanian (立陶宛语)", dirPathlt)
    # excel2XmlUtils.xls2xml(xlsPath, None, "pt-PT（葡萄牙语）", dirPathpt)
    # excel2XmlUtils.xls2xml(xlsPath, None, "中文需求描述（CN）", dirPathzh)
    # excel2XmlUtils.xls2xml(xlsPath, None, "pl-PL（波兰语）", dirPathpl)
    # excel2XmlUtils.xls2xml(xlsPath, None, "nl-NL（荷兰语）", dirPathnl)

def main():
    Constant.Config.import_start_col = 2
    Constant.Config.import_base_xml = False
    Constant.Config.support_custom_ph_rule = True

    excelToxml("/Users/ninebot/Desktop/after_sale_app/development/android-mowerpdi/commonres/src/main/res",
               "/Users/ninebot/Desktop/after_sale_app/MultilingualTranslation/strings.xls")

main()
