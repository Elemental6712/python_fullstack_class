list_prices_1 = [100, 200, 300]

def sum_sales_with_for(list_prices):
    summa = 0
    for i in list_prices:
        summa += i
    print(*list_prices, sep=" + ", end=f' = {summa}')

sum_sales_with_for(list_prices_1)