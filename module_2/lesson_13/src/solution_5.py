
def my_decorator(func):
    def wraperr(*args, **kwargs):
        result = func(*args, **kwargs)
        if result ==('Роман', "correctpassword"):
            print('Доступ получен. Данные...')
        else:
            print("В доступе отказано!")
        return result
    return wraperr

@my_decorator
def access_client_data(name, password):
    return name, password

access_client_data('Роман', "correctpassword") #Доступ получен
access_client_data('Олег', 'wrongpassword') # В доступе отказано