from inventory_report.inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __iter__(self) -> InventoryIterator:
        return InventoryIterator(self.data)

    def import_data(self, path_file, method):
        stock_data = self.importer.import_data(path_file)
        self.data = self.data + stock_data

        method_map = {
            'simples': SimpleReport.generate,
            'completo': CompleteReport.generate
        }

        # print(self.stock_data)
        return method_map[method](stock_data)
