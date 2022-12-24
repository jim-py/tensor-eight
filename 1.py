class Animals:
    def __init__(self, weight, height, legs, tail, name):
        self.weight = weight
        self.height = height
        self.legs = legs
        self.tail = tail
        self.name = name

class Mammals(Animals):
    def __init__(self, weight, height, legs, tail, name):
        super().__init__(weight, height, legs, tail, name)
        self.milk_feeding = True

class Human(Mammals):
    def __init__(self, weight, height, legs, tail, beard, name):
        super().__init__(weight, height, legs, tail, name)
        self.beard = beard

    def voice(self):
        print('Hello!')

class Cat(Mammals):
    def __init__(self, weight, height, legs, tail, breed, name):
        super().__init__(weight, height, legs, tail, name)
        self.breed = breed

    def voice(self):
        print('Meow!')


class Dog(Mammals):
    def __init__(self, weight, height, legs, tail, breed, name):
        super().__init__(weight, height, legs, tail, name)
        self.breed = breed

    def voice(self):
        print('Gav!')


Jimmy = Human(70, 182, 2, False, True, 'Jimmy')
Dasha = Human(55, 164, 2, False, False, 'Dasha')
Sam = Cat(5, 20, 4, True, 'European', 'Sam')
Husky = Dog(25, 55, 4, True, 'Siberian', 'Husky')
print(Jimmy.milk_feeding, Jimmy.name)
Jimmy.voice()
print(f'У {Jimmy.name} {Jimmy.legs} ноги, а у {Sam.name} {Sam.legs} лапы')
for mammals in (Jimmy, Dasha, Sam, Husky):
    if mammals.legs == 2:
        print(f'{mammals.name} - человек')
    else:
        print(f'{mammals.name} - не человек')
