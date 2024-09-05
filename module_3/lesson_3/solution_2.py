
"""
Задание 2: Автоматизация управления теплицей (Инкапсуляция)

Создайте класс Greenhouse с приватными атрибутами для температуры, влажности и уровня света.

Добавьте публичные методы для установки и получения этих атрибутов, включая проверки на допустимые значения (например, температура должна быть между 15 и 30 градусами).

В программе создайте объект Greenhouse и продемонстрируйте установку и получение атрибутов с помощью методов.

"""

class Greenhouse:
    def __init__(self, temperature = 20, humidity = 50, light_level = 5):
        self.__temperature = temperature
        self.__humidity = humidity
        self.__light_level = light_level

    def change_temperature(self, temp):
        if not (15 <= temp <= 30):
            print('It is possible to set the temperature only in the range from 15 to 30')
        else:
            self.__temperature = temp
    
    def change_humidity(self, value):
        if not (40 <= value <= 80):
            print('Humidity should be at least 40 percent and no more than 80')
        else:
            self.__humidity = value
    
    def change_light_level(self, value):
        if not (3 <= value <= 8):
            print("The light level cannot be lower than 3 and higher than 8")
        else:
            self.__light_level = value
    
    @property
    def greenhouse_parameters(self):
        print(f"Temperature = {self.__temperature}, humidity = {self.__humidity}, light level = {self.__light_level}")

i = Greenhouse()

i.change_temperature(40)
i.change_humidity(73)
i.change_light_level(4)

i.greenhouse_parameters

