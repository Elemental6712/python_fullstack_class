price_list = input("Список цен: ")
price_list_two = [int(x) for x in price_list.split(', ')]
def find_max_price(price_list_two):
    if len(price_list_two) == 1:
        return price_list_two[0]
    else:
        max_price = find_max_price(price_list_two[1:])
        return price_list_two[0] if price_list_two[0] > max_price else max_price
result = find_max_price(price_list_two)
print(result)