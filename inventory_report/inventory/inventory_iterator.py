from collections.abc import Iterator


# https://refactoring.guru/pt-br/design-patterns/iterator/python/example
class InventoryIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection) -> None:
        self._collection = collection
        self._position = 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += 1
            return value
        except IndexError:
            raise StopIteration()
