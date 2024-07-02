def my_decorator(func):
    
    def wraperr(*args):

        dict_date = func(*args)
        
        if len(dict_date) > 2 or len(dict_date) < 2:
            print('Несоблюдено кол-во аргументов')
        if type(dict_date[0]) != str and type(dict_date[1]) != int:
            print('Все типы не подходят.')
        elif type(dict_date[0]) != str:
            print('Ошибка: Первый аргумент не строка!')
        elif type(dict_date[1]) != int:
            print('Ошибка: Второй аргумент не число!')
        else:
            print('Estimated time calculated successfully.')
        return dict_date
    return wraperr


@my_decorator
def estimate_time(*name):
    return name


estimate_time('Веб-сайт', "пять")
estimate_time('Визитка', 10)
