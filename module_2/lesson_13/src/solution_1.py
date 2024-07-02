def decorator(func):
    def wrapper():
        print(f'Цена на {data[0]} изменилась! {data[1]} > {data[2]}')
    return wrapper

@decorator
def change_price(data):
    pass


data = ('Кресло', 5000, 4500)
#data = ('Стол', 8000, 7600)


change_price()