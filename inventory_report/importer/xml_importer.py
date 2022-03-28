from typing import List, Dict
from abc import abstractclassmethod
import xml.etree.ElementTree as XMLTree
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @abstractclassmethod
    def import_data(cls, path_file: str) -> List[Dict]:
        if not (path_file.endswith('.xml')):
            raise ValueError("Arquivo inválido")

        tree = XMLTree.parse(path_file)
        root = tree.getroot()
        items = []
        for item in root:
            stock = {}
            for child in item:
                stock[child.tag] = child.text
            items.append(stock)
        return items
