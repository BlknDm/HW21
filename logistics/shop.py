from logistics.base_storage import BaseStorage
from logistics.exception import ToomachVariableProductError


class Shop(BaseStorage):
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def add(self, name, amount):
        if self.get_unique_items_count() >= 5:
            raise ToomachVariableProductError
        super().add(name, amount)
