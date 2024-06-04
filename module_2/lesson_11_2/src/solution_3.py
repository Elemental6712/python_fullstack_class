quantity_goods_1 = {'apples': 50, 'bananas': 10, 'cherries': 3}
minimal_amount_1 = 15

def track_low_stock_with_for(list_of_products, minimal_amount):
    
    for product, quantity in list(quantity_goods_1.items()):
        if int(quantity) > minimal_amount_1:
            del quantity_goods_1[product]
        else:
            continue
    print(f'Низкий запас: {quantity_goods_1}')
    

track_low_stock_with_for(quantity_goods_1, minimal_amount_1)