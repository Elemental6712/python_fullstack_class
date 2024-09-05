from abc import ABC, abstractmethod

class Fountain(ABC):
    @abstractmethod
    def spray_water(self):
        pass

class SimpleFountain(Fountain):
    def spray_water(self):
        print("Фонтан перешел в спокойный режим разбрызгивания воды")

class MusicalFountain(Fountain):
    def spray_water(self):
        print("Фонтан начал проигрывание музыки")
    
class LightedFountain(Fountain):
    def spray_water(self):
        print("Фонтан перешел в ночной режим и начал светиться")

types_fountains = [SimpleFountain(), MusicalFountain(), LightedFountain()]

for fountain in types_fountains:
    fountain.spray_water()




"""
Задание 1: Управление фонтанами (Полиморфизм)

Создайте абстрактный класс Fountain с методом spray_water.

Создайте подклассы SimpleFountain, MusicalFountain, и LightedFountain, которые переопределяют метод spray_water, выводя уникальное сообщение о том, как каждый фонтан брызгает воду.

В программе создайте список объектов типа Fountain и вызовите метод spray_water для каждого элемента списка.
"""