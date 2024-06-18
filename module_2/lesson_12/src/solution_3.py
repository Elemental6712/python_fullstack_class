def filter_data(data, filter_func):
    return list(filter(filter_func, data))

    

data_sets = [

    ([10, 23, 35, 47], lambda x: x % 2 != 0),  #фильтрация нечётных значений)
    ([5, 7, 8, 10], lambda x: x > 7),  #значения больше 7
    ([1, 2, 3, 5, 6], lambda x: x < 5),  #значения меньше 5,
    ([10, 20, 30, 40, 50], lambda x: x % 5 == 0 and x % 8 == 0),  #только значения, кратные 5 и 8
    
]


for data, filter_func in data_sets:
    filtered_data = filter_data(data, filter_func)
    print(f"Отфильтрованные данные: {filtered_data}")