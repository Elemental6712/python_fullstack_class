
class Animal:

    def __init__(self, name_animal, sould_animal):
        self.name_animal = name_animal
        self.sould_animal = sould_animal

    def make_sounds(self):
        return f'Созданое нами животное: {self.name_animal}, "говорит" {self.sould_animal}'
    

    def eat(self):
        return f'Созданое нами животное: {self.name_animal} есто только то, что дали мы)))'


animal_sould = Animal('Кошка', "Мур-мяу")
print(animal_sould.make_sounds())
print(animal_sould.eat())
