book = int(input("Количество книг: "))
stationery = int(input("Количество концтоваров: "))
toys = int(input("Количество игрушек: "))
volum_book = book * 2
volum_stationery = stationery * 1.5
volum_toys = toys * 3
total_volume = volum_book + volum_stationery + volum_toys
print(f"Общий объем: {total_volume} м^3")