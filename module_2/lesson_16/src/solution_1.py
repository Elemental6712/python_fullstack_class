changes = []


def optimization(*number_of_shelves, **shelf_length):

    number_of_shelves = int(input())
    shelf_length = list(map(int, input().split(',')))
    for i in range(number_of_shelves):
        changes.append([shelf_length[i], 0])

    print(changes)


optimization()