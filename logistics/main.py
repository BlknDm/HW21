from logistics.courier import Courier
from logistics.exception import BaseError
from logistics.request import Request
from logistics.shop import Shop
from logistics.store import Store


shop = Shop(
    items={
        'печенька': 3,
        'ноутбук': 2,
        'елка': 5,
        'гирлянда': 10,
    },
)

store = Store(
    items={
        'печенька': 10,
        'ноутбук': 20,
        'хлопушка': 5,
        'маска': 3,
        'скатерть': 6,
    },
)

storages = {
    'магазин': shop,
    'склад': store,
}


def main():
    while True:
        for storage_name in storages:
            print(f'В {storage_name} хранится: {storages[storage_name].get_items()}')

        user_input = input(
            'Введите строку в формате "Доставить 3 печенька из склад в магазин".\n'
            'Введите "stop" или "стоп", чтобы продолжить',
        )

        if user_input in ('stop', 'стоп'):
            break

        try:
            request = Request(request_str=user_input, storages=storages)

            courier = Courier(request=request, storages=storages)
            courier.move()

        except BaseError as error:
            print(error.message)


if __name__ == '__main__':
    main()
