from typing import Literal

class Animal:
    def __init__(
            self,
            type_animal,
            animal_sounds,
            type_animal_food: Literal['всеядный', 'плотоядный', 'травоядный']
    ):
        self.type_animal = type_animal
        self.animal_sounds = animal_sounds
        self.type_animal_food = type_animal_food
    
    def __str__(self):
        return f'Это {self.type_animal} животное {self.type_animal_food},'
    
    def sounds(self):
        return f'{self.type_animal} "говорит" {self.animal_sounds}'
    
animal_1 = Animal('волк', "ауууу", "плотоядное")
animal_2 = Animal("корова", "мууу", "травоядное")
animal_3 = Animal("кошка", "мяу", "плотоядное")

print(animal_1, animal_1.sounds())
print(animal_2, animal_2.sounds())
print(animal_3, animal_3.sounds())
