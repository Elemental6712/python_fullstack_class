
class PersonInfo:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Person:
    population = []

    def __init__(self, name, age):

        self.name = name
        self.age = age
        Person.population.append(self.name)

    def __str__(self):
        return f'Имя: {self.name}. Год рождения: {2024 - self.age}'

    @classmethod
    def from_birth_year(cls, person_info: PersonInfo):
        Person.population.append(person_info.name)
        return f'Имя клиента: {person_info.name}. Год рождения клиента: {2024 - int(person_info.age)}'
    
    @classmethod
    def current_population(cls):
        return f'Текущая популяция: {len(Person.population)}'

person_1 = Person('Владимир', 23)
person_2 = Person("Глеб", 27)
print(person_1)
print(person_2)

person_3 = PersonInfo("Евгений", 21)
print(Person.from_birth_year(person_3))

print(Person.current_population())
print(Person.population)


"""
Задание 2: Работа с атрибутами класса
Добавьте в класс Person атрибут класса population, который будет отслеживать количество созданных экземпляров.
Обновите методы __init__ и from_birth_year так, чтобы они увеличивали population на 1 при создании нового экземпляра.
Создайте метод класса, который выводит текущую популяцию.
"""