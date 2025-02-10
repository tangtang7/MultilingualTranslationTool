# -*- coding:utf-8 -*-
import Constant
from Excel2XmlUtil import Excel2XmlUtils


def excelToxml():
    excel2XmlUtils = Excel2XmlUtils()

    xlsDevicePath = "/Users/ninebot/Documents/after_sale_app/MultilingualTranslation/strings_device.xls"
    xlsYamlPath = "/Users/ninebot/Documents/after_sale_app/MultilingualTranslation/strings_yaml.xls"

    # dirPath = "/Users/ninebot/Documents/after_sale_app/MultilingualTranslation/res/values"

    dirDevicePath = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values/strings_device.xml"
    dirDevicePathaa = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-aa/strings_device.xml"
    dirDevicePathbg = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-bg/strings_device.xml"
    # dirDevicePathcs = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-cs/strings_device.xml"
    # dirDevicePathda = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-da/strings_device.xml"
    dirDevicePathde = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-de/strings_device.xml"
    dirDevicePathen = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-en/strings_device.xml"
    ### dirDevicePathen = "/Users/ninebot/Documents/after_sale_app/pdi-mower/commonres/src/main/res/values-en/strings_device.xml"
    dirDevicePathes = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-es/strings_device.xml"
    # dirDevicePathet = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-et/strings_device.xml"
    # dirDevicePathfi = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-fi/strings_device.xml"
    dirDevicePathfr = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-fr/strings_device.xml"
    # dirDevicePathhr = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-hr/strings_device.xml"
    dirDevicePathhu = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-hu/strings_device.xml"
    dirDevicePathit = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-it/strings_device.xml"
    dirDevicePathlt = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-lt/strings_device.xml"
    # dirDevicePathlv = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-lv/strings_device.xml"
    # dirDevicePathnl = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-nl/strings_device.xml"
    # dirDevicePathno = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-no/strings_device.xml"
    # dirDevicePathpl = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-pl/strings_device.xml"
    dirDevicePathpt = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-pt/strings_device.xml"
    # dirDevicePathro = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-ro/strings_device.xml"
    # dirDevicePathsk = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-sk/strings_device.xml"
    # dirDevicePathsl = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-sl/strings_device.xml"
    # dirDevicePathsv = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-sv/strings_device.xml"

    dirYamlPath = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values/strings_yaml.xml"
    dirYamlPathaa = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-aa/strings_yaml.xml"
    dirYamlPathbg = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-bg/strings_yaml.xml"
    # dirYamlPathcs = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-cs/strings_yaml.xml"
    # dirYamlPathda = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-da/strings_yaml.xml"
    dirYamlPathde = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-de/strings_yaml.xml"
    dirYamlPathen = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-en/strings_yaml.xml"
    dirYamlPathes = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-es/strings_yaml.xml"
    # dirYamlPathet = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-et/strings_yaml.xml"
    # dirYamlPathfi = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-fi/strings_yaml.xml"
    dirYamlPathfr = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-fr/strings_yaml.xml"
    # dirYamlPathhr = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-hr/strings_yaml.xml"
    dirYamlPathhu = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-hu/strings_yaml.xml"
    dirYamlPathit = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-it/strings_yaml.xml"
    dirYamlPathlt = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-lt/strings_yaml.xml"
    # dirYamlPathlv = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-lv/strings_yaml.xml"
    # dirYamlPathnl = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-nl/strings_yaml.xml"
    # dirYamlPathno = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-no/strings_yaml.xml"
    # dirYamlPathpl = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-pl/strings_yaml.xml"
    dirYamlPathpt = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-pt/strings_yaml.xml"
    # dirYamlPathro = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-ro/strings_yaml.xml"
    # dirYamlPathsk = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-sk/strings_yaml.xml"
    # dirYamlPathsl = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-sl/strings_yaml.xml"
    # dirYamlPathsv = "/Users/ninebot/Desktop/pdi-mower/commonres/src/main/res/values-sv/strings_yaml.xml"

    # excel2XmlUtils.xls2xml(xlsDevicePath, dirDevicePath, "en", None)
    excel2XmlUtils.xls2xml(xlsDevicePath, dirDevicePathaa, "aa", None)
    excel2XmlUtils.xls2xml(xlsDevicePath, dirDevicePathbg, "bg", None)
    excel2XmlUtils.xls2xml(xlsDevicePath, dirDevicePathde, "de", None)
    excel2XmlUtils.xls2xml(xlsDevicePath, dirDevicePathen, "en", None)
    excel2XmlUtils.xls2xml(xlsDevicePath, dirDevicePathes, "es", None)
    excel2XmlUtils.xls2xml(xlsDevicePath, dirDevicePathfr, "fr", None)
    excel2XmlUtils.xls2xml(xlsDevicePath, dirDevicePathhu, "hu", None)
    excel2XmlUtils.xls2xml(xlsDevicePath, dirDevicePathit, "it", None)
    excel2XmlUtils.xls2xml(xlsDevicePath, dirDevicePathlt, "lt", None)
    excel2XmlUtils.xls2xml(xlsDevicePath, dirDevicePathpt, "pt", None)

    # excel2XmlUtils.xls2xml(xlsYamlPath, dirYamlPath, "en", None)
    excel2XmlUtils.xls2xml(xlsYamlPath, dirYamlPathaa, "aa", None)
    excel2XmlUtils.xls2xml(xlsYamlPath, dirYamlPathbg, "bg", None)
    excel2XmlUtils.xls2xml(xlsYamlPath, dirYamlPathde, "de", None)
    excel2XmlUtils.xls2xml(xlsYamlPath, dirYamlPathen, "en", None)
    excel2XmlUtils.xls2xml(xlsYamlPath, dirYamlPathes, "es", None)
    excel2XmlUtils.xls2xml(xlsYamlPath, dirYamlPathfr, "fr", None)
    excel2XmlUtils.xls2xml(xlsYamlPath, dirYamlPathhu, "hu", None)
    excel2XmlUtils.xls2xml(xlsYamlPath, dirYamlPathit, "it", None)
    excel2XmlUtils.xls2xml(xlsYamlPath, dirYamlPathlt, "lt", None)
    excel2XmlUtils.xls2xml(xlsYamlPath, dirYamlPathpt, "pt", None)

def main():
    Constant.Config.import_start_col = 2
    Constant.Config.import_base_xml = False
    Constant.Config.support_custom_ph_rule = True

    excelToxml()


main()
