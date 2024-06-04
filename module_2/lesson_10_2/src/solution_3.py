name_and_number_of_tasks = {'Анна': 5, 'Боб': 3, "Сюзан": 7}

def most_effective(name_and_number_of_tasks):
    name_employee = list(name_and_number_of_tasks.keys())
    number_of_tasks = list(name_and_number_of_tasks.values())

    best_value = max(number_of_tasks)
    best_employees = [n for n, completed in name_and_number_of_tasks.items() if completed == best_value]
    return best_employees

result = most_effective(name_and_number_of_tasks)

normal = ', '.join(map(str, result))

print(f'Лучший сотрудник: {normal}')