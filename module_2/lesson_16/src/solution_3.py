"""
changes = []
w = []
q = 1
def optimization(*number_of_shelves, **shelf_length):

    number_of_shelves = 2
    shelf_length = [3, 4]
    number_of_goods = [1, 4]
    for i in range(number_of_shelves):
        changes.append([shelf_length[i], 0])
    for i in range(len(changes)):
        changes[i][1] = number_of_goods[i]
    print(changes)


optimization()

for i in changes:
    i.pop(0)
    i *= i[0]
    i = [j * q for j in i]
    q += 1
    w.append(i)

print(w)
"""
changes = []
w = []



def optimization(*number_of_shelves, **shelf_length):

    q = 1
    number_of_shelves = 3
    shelf_length = [4, 5, 6]
    number_of_goods = [2, 3, 5]
    for i in range(number_of_shelves):
        changes.append([shelf_length[i], 0])
    for i in range(len(changes)):
        changes[i][1] = number_of_goods[i]
    for i in changes:
        i.pop(0)
        i = i * i[0]
        i = [j * q for j in i]
        q += 1
        w.append(i)

    print(w)


optimization()