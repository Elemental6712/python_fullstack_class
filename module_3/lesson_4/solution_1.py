from abc import ABC, abstractmethod

class Instrument(ABC):
    @abstractmethod
    def play(self):
        return 'Музыка'

class Guitar(Instrument):
    def play(self):
        return 'Звуки музыки при игре на гитаре'

class Piano(Instrument):
    def play(self):
        return 'Звуки музыки при игре на пианино'

class Flute(Instrument):
    def play(self):
        return 'Звуки музыки при игре на флейте'


my_guitara = Guitar()
my_piano = Piano()
my_flute = Flute()

print(my_guitara.play())
print(my_piano.play())
print(my_flute.play())

"""Задание 1: Школа музыки (Наследование от абстрактного класса)
Создайте абстрактный класс Instrument с абстрактным методом play().
Создайте подклассы Guitar, Piano, и Flute, каждый из которых переопределяет метод play.
В каждом подклассе должен быть своя реализация метода для воспроизведения звука инструмента.
В главной программе создайте список объектов типа Instrument и вызовите для каждого метод play."""

