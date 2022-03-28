from typing import List, Dict
from abc import abstractclassmethod
from csv import DictReader
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @abstractclassmethod
    def import_data(cls, path_file: str) -> List[Dict]:
        if not (path_file.endswith('.csv')):
            raise ValueError("Arquivo inválido")

        with open(path_file) as file:
            csv_reader = DictReader(file)
            return list(csv_reader)
