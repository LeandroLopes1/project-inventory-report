from inventory_report.inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, collection):
        # self._read_importer = read_importer
        self._collection = collection
        self._position = 0

    def __iter__(self) -> InventoryIterator:
        return InventoryIterator(self._collection)

    @classmethod
    def import_data(self, path_file, method):
        print(self._collection)
        # stock_data = self._read_importer.import_data(path_file)
        # self._collection = stock_data
        # print(stock_data)

        # method_map = {
        #     'simples': SimpleReport.generate,
        #     'completo': CompleteReport.generate
        # }

        # # print(self.stock_data)
        # return method_map[method](stock_data)
