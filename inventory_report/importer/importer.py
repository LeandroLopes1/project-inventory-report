from abc import ABC, abstractclassmethod
from typing import List, Dict


class Importer(ABC):
    @abstractclassmethod
    def import_data(cls, path: str) -> List[Dict]:
        raise NotImplementedError()
