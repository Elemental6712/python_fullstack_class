from typing import Callable


def check_order(order): #Проверка заказа

    if len(order['items']) == 0:
        check_order = 'Требования не соблюдены'
    else:
        check_order = 'Требования соблюдены'
    return check_order

def package_order(check_order): #Упаковывает заказ
    if check_order == 'Требования не соблюдены':
        package_order = "Заказ не упакован"
    else:
        package_order = 'Заказ упакован'
    return package_order

def send_order(check: Callable[[str], str], package: Callable[[str], str], order): #Координирует процесс и инициирует отправку
    if len(order['items']) == 0:
        print(f'Заказ {order["id"]} не упакован, т.к он пустой.')
    else:
        print(f'Отправка: Упакован заказ {order["id"]}')

order1 = {'id': 1, 'items': ['book', 'pen']}

#order2 = {'id': 2, 'items': []}

send_order(check_order, package_order, order1)

#send_order(check_order, package_order, order2)
