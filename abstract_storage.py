from abc import ABC, abstractmethod


class AbstractStorage(ABC):
    @abstractmethod
    def add(self, name, quantity):
        pass

    @abstractmethod
    def remove(self, name, quantity):
        pass

    @property
    @abstractmethod
    def free_space(self):
        pass

    @property
    @abstractmethod
    def items(self):
        pass

    @property
    @abstractmethod
    def unique_items_count(self):
        pass
