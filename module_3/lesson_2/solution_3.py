
class Temperature(object):

    @staticmethod
    def celsius_to_fahrenheit(cels):

        return f'Перевели градусы Цельсия в градусы Фаренгейта: {cels * 1.8 + 32}'
    
    @staticmethod
    def fahrenheit_to_celsius(fahr):

        return f'Перевели градусы Фаренгейта в градусы Цельсия: {(fahr - 32) * 5 // 9}'

print(Temperature.celsius_to_fahrenheit(73))
print(Temperature.fahrenheit_to_celsius(68))


"""
Задание 3: Конвертация единиц
Создайте класс Temperature с методами для конвертации температуры между градусами Цельсия и Фаренгейта.
Реализуйте статические методы celsius_to_fahrenheit и fahrenheit_to_celsius.
"""

