#list_of_products_1 = ['fruit', 'toy', 'fruit', 'toy']
#necessary_product_1 = 'toy'

#То, что чуть выше, для проверки)))

list_of_products_1 = ['clothes', 'clothes', 'clothes']
necessary_product_1 = 'clothes'

def count_specific_items_with_while(list_of_products, necessary_product):
    
    count = 0
    
    while len(list_of_products) > 0:
        
        if list_of_products.pop() == necessary_product:        
            count += 1
        
        else:
            continue
    print(f'Количество "{necessary_product_1}": {count}')

count_specific_items_with_while(list_of_products_1, necessary_product_1)