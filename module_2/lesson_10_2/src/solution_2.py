def background_theme(time):

    if time >= 6 and time <= 18:
        print("Тема фона: Светлая")


    elif time < 6 or time < 24:
        print("Тема фона: Темная")


    else:
        print("Укажите текущее время в формате от 0 до 23")
    
background_theme(10)