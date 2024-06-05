number_of_days = int(input())
list_of_days = []
def sales_schedule_with_range(number_of_days):
    for i in range(3, number_of_days + 1, 3):
        list_of_days.append(i)
    print(f'Дни распродажи: {list_of_days}')

sales_schedule_with_range(number_of_days)
