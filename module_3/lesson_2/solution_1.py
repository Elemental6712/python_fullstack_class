
class PersonInfo:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age
    
    def __str__(self):
        return f'Имя: {self.name}. Год рождения: {2024 - self.age}'

    @classmethod
    def from_birth_year(cls, person_info: PersonInfo):
        return f'Имя: {person_info.name}. Год рождения: {2024 - int(person_info.age)}'


person_1 = Person('Владимир', 24)
print(person_1)


persona_2 = PersonInfo("София", 21)
print(Person.from_birth_year(persona_2))


"""
Задание 1: Альтернативные конструкторы
Создайте класс Person с атрибутами name и age.
Реализуйте метод __init__ для инициализации этих атрибутов.
Создайте класс метод from_birth_year для создания экземпляра Person на основе года рождения.
Выведите информацию о персоне, созданной через этот альтернативный конструктор.
"""