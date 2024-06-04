cost_of_orders = input('Вветите список: ')
modified_list_of_costs = [int(n) for n in cost_of_orders.split(', ')]

def calculate_discount(modified_list_of_costs, index = 0, past_price=None):
    discount_list = []

    if index < len(modified_list_of_costs):
        current_price = modified_list_of_costs[index]
        current_discount = past_price * 0.1 if past_price is not None else 0
        discounted_price = current_price - current_discount if past_price is not None else current_price
        discount_list.append(discounted_price)
        discount_list += calculate_discount(modified_list_of_costs, index + 1, current_price)
    
    return discount_list

end = calculate_discount(modified_list_of_costs)
end_int = [int(x) for x in end]

print(f'Выходные данные: {end_int}')