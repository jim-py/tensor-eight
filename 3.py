class Human:
    def __init__(self, weight, height, name):
        self.weight = weight
        self.height = height
        self.name = name


class Student(Human):
    def __init__(self, weight, height, name, complete_dz):
        super().__init__(weight, height, name)
        self.complete_dz = complete_dz

    def __gt__(self, student): 
        return self.complete_dz > student.complete_dz

    def __lt__(self, student): 
        return self.complete_dz < student.complete_dz

    def __eq__(self, student): 
        return self.complete_dz == student.complete_dz

    def __ne__(self, student): 
        return self.complete_dz != student.complete_dz

    def __ge__(self, student): 
        return self.complete_dz >= student.complete_dz

    def __le__(self, student): 
        return self.complete_dz <= student.complete_dz


Petya = Student(70, 182, 'Petya', 5)
Vasya = Student(70, 182, 'Vasya', 4)

print(Petya > Vasya)
print(Petya < Vasya)
print(Petya == Vasya)
print(Petya != Vasya)
print(Petya >= Vasya)
print(Petya <= Vasya)
