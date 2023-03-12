from abstract_storage import AbstractStorage


class StorageClass(AbstractStorage):
    def __init__(self, items, capacity):
        self._items = items
        self._capacity = capacity
        self._location = None

    def __repr__(self):
        result = [f'{item[1]} {item[0]}' for item in self._items.items()]
        return '\n'.join(result)

    def add(self, name, quantity):
        if quantity > self.free_space:
            print(f'В {self._location} недостаточно места, попробуйте что-то еще')
            return False
        else:
            self._items[name] = self._items.get(name, 0) + quantity
            return True

    def remove(self, name, quantity):
        if name not in self._items:
            print(f'{name} не найден в {self._location}')
            return False
        elif quantity > self._items[name]:
            print(f'Не хватает {name} на {self._location}, попробуйте заказать меньше')
            return False
        else:
            self.items[name] -= quantity
            if self._items[name] == 0:
                del self._items[name]
            return True

    @property
    def free_space(self):
        return self._capacity - sum(self._items.values())

    @property
    def items(self):
        return self._items

    @property
    def unique_items_count(self):
        return len(self._items)


class Store(StorageClass):
    def __init__(self, items, capacity):
        super().__init__(items, capacity)
        self._location = 'склад'


class Shop(StorageClass):
    def __init__(self, items, capacity):
        super().__init__(items, capacity)
        self._location = 'магазин'

    def add(self, name, quantity):
        if name not in self._items and self.unique_items_count == 5:
            print('В магазин недостаточно места, попробуйте что-то другое')
            return False
        return super().add(name, quantity)


class Request():
    def __init__(self, args):
        self._sender = args[4]
        self._receiver = args[6]
        self._quantity = int(args[1])
        self._name = args[2]

    @property
    def sender(self):
        return self._sender

    @property
    def receiver(self):
        return self._receiver

    @property
    def quantity(self):
        return self._quantity

    @property
    def name(self):
        return self._name
