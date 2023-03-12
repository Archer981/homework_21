from classes import Store, Shop, Request


items_store = {
    'ложка': 30,
    'вилка': 10,
    'тарелка': 5,
    'стол': 1,
    'стул': 1,
    'ящик': 1,
}
items_shop = {
    'ложка': 2,
    'вилка': 3,
    'тарелка': 1,
}

store = Store(items_store, 100)
shop = Shop(items_shop, 20)

places = {
    'склад': store,
    'магазин': shop,
}


def main():
    while True:
        print('На склад хранится:')
        print(store)
        print('В магазин хранится:')
        print(shop)
        query = input('Введите Ваш запрос вида "Доставить Х _____ из _____ в _____": ')
        if query.lower() in ['stop', 'стоп']:
            break
        query = query.lower().split(' ')

        if len(query) != 7 or not query[1].isdigit():
            print('Проверьте правильность формулировки запроса')
            continue
        request = Request(query)
        if request.sender not in places or request.receiver not in places or request.sender == request.receiver:
            print('Проверьте место отправления и назначения')
            continue
        if not places[request.sender].remove(request.name, request.quantity):
            continue
        print(f'Нужное количество есть на {request.sender}')
        print(f'Курьер забрал {request.quantity} {request.name} из {request.sender} и везет в {request.receiver}')
        if not places[request.receiver].add(request.name, request.quantity):
            print(f'Курьер возвращает {request.quantity} {request.name} из {request.receiver} в {request.sender}')
            places[request.sender].add(request.name, request.quantity)
            continue
        print(f'Курьер доставил {request.quantity} {request.name} из {request.sender} в {request.receiver}')


if __name__ == '__main__':
    main()
