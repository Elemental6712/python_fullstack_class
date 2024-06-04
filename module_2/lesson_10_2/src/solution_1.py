def calculation_of_the_discount(price, visits):

    if visits < 10:
        print(f"Итоговая цена: {price}")

    elif visits >= 10 and visits < 20:
        discounted_price_10 = price - (price // 100 * 10)
        print(f"Итоговая цена: {discounted_price_10}")

    elif visits >= 20:
        discounted_price_20 = price - (price // 100 * 20)
        print(f"Итоговая цена: {discounted_price_20}")
