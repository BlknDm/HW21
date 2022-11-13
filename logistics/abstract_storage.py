from abc import ABC, abstractmethod


class AbstractStorage(ABC):

    @abstractmethod
    def add(self, name, amount) -> None: # увеличивает запас items
        pass

    @abstractmethod
    def remove(self, name, amount): # уменьшает запас items
        pass

    @abstractmethod
    def get_free_space(self): # вернуть количество свободных мест
        pass

    @abstractmethod
    def get_items(self): # возвращает содержание склада в словаре {товар: количество}
        pass

    @abstractmethod
    def get_unique_items_count(self): # возвращает количество уникальных товаров.
        pass
