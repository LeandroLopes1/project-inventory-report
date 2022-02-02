from pathlib import Path
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


# https://stackoverflow.com/questions/60805355/convert-xml-to-list-of-dictionaries-in-python
def read_cvs_file(path):
    import csv
    with open(path) as f:
        result = [{k: v for k, v in row.items()}
                  for row in csv.DictReader(f, skipinitialspace=True)]
    return result


# https://stackoverflow.com/questions/39332792/python-3-how-to-read-file-json-into-list-of-dictionary
def read_json_file(path):
    import json
    with open(path) as file:
        result = json.load(file)
    return result


# https://stackoverflow.com/questions/60805355/convert-xml-to-list-of-dictionaries-in-python
def read_xml_file(path):
    import xml.etree.ElementTree as ET

    tree = ET.parse(path)
    root = tree.getroot()

    stock_list = []

    for item in root.findall('./record'):
        stock = {}
        for child in item:
            stock[child.tag] = child.text
        stock_list.append(stock)

    return stock_list


def read_file(path):
    extention_file = Path(path).suffix.replace('.', '')

    extension_func_map = {
        "csv": read_cvs_file,
        "json": read_json_file,
        "xml": read_xml_file
    }

    return extension_func_map[extention_file](path)


class Inventory:
    def __init__(self):
        self.stock_data = None

    @classmethod
    def import_data(self, path_file, method):
        # accepted_methods = ['simples', 'completo']
        self.stock_data = read_file(path_file)

        method_map = {
            'simples': SimpleReport.generate,
            'completo': CompleteReport.generate
        }

        # print(self.stock_data)
        return method_map[method](self.stock_data)
