def prices(price_list):
    rounded_prices = filter(lambda price: price % 100 != 0, price_list)
    modified_price_list = [round(i, -2) for i in rounded_prices]
    print(modified_price_list)

list_prices = [99, 150, 200, 349, 501]

prices(list_prices) 