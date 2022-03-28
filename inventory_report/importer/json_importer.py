from typing import List, Dict
from abc import abstractclassmethod
from json import load
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @abstractclassmethod
    def import_data(cls, path_file: str) -> List[Dict]:
        if not (path_file.endswith('.json')):
            raise ValueError("Arquivo inválido")

        with open(path_file) as file:
            return load(file)
