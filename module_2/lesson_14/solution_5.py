from collections import Counter

def type_of_goods(list_product):
    modified_list = Counter(map(lambda types: types[1], list_product))
    return dict(modified_list)
    

list_1 = [('Рубашка', 'Одежда'), ('Кружка', 'Посуда')]
list_2 = [('Рубашка', 'Одежда'), ('Штаны', 'Одежда'), ('Кружка', 'Посуда')]                                       
list_3 = [('Ручка', 'Канцелярия'), ('Тетрадь','Канцелярия'), ('Кружка', 'Посуда'), ('Стул', 'Мебель')]

print(type_of_goods(list_1))
print(type_of_goods(list_2))
print(type_of_goods(list_3))