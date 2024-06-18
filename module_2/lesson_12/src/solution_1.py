import statistics

def collect_data(data):
    return process_data(data)

def process_data(data):
    average = statistics.mean(data)
    return summarize_data(average)

def summarize_data(average):
    return f"Итог: Среднее значение {average}"


data_1= [1, 2, 3, 4, 5]
#data_2 = [10, 15, 5, 20]


print(collect_data(data_1))
