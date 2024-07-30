changes = []



def optimization(*number_of_shelves, **shelf_length):

    number_of_shelves = int(input("Введите кол-во полок: "))
    shelf_length = list(map(int, input("Введите длину полок: ").split(',')))
    number_of_goods = list(map(int, input("Введите количество товаров: ").split(',')))
    for i in range(number_of_shelves):
        changes.append([shelf_length[i], 0])
    for i in range(len(changes)):
        changes[i][1] = number_of_goods[i]
    print(changes)


optimization()