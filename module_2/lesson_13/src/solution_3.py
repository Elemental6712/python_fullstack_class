cahce = {}

small_business = ("Логотип", "Малый бизнес")

def my_decorator(func):
    def wraperr(*args):
        if small_business[1] in cahce:
                print(cahce[small_business[1]])
        else:
            cahce[small_business[1]] = 'Загрузили из кеша: 3000'
            print(func(*args))
    return wraperr

@my_decorator
def calculate_project_cost(small_business):
    return 'Посчитали цену: 3000'


calculate_project_cost(small_business)
calculate_project_cost(small_business)