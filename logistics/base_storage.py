from logistics.abstract_storage import AbstractStorage
from logistics.exception import NotEnoughSpaceError, UnknownProductError, NotEnoughProductError


class BaseStorage(AbstractStorage):

    def __init__(self, items, capacity):
        self._items = items
        self._capacity = capacity

    def add(self, name, amount):

        if self.get_free_space() < amount:
            raise NotEnoughSpaceError

        self._items[name] = self._items.get(name, 0) + amount

    def remove(self, name, amount):
        if name not in self._items:
            raise UnknownProductError

        if self._items[name] < amount:
            raise NotEnoughProductError

        self._items[name] -= amount
        if self._items[name] == 0:
            self._items.pop(name)

    def get_free_space(self):
        return self._capacity - sum(self._items.values())

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self._items)
