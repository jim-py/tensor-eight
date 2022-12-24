class Human:
    def __init__(self, weight, height, name):
        self.weight = weight
        self.height = height
        self.name = name


class Student(Human):
    def __init__(self, weight, height, name, complete_dz):
        super().__init__(weight, height, name)
        self.complete_dz = complete_dz


Petya = Student(70, 182, 'Petya', 5)
Vasya = Student(70, 182, 'Vasya', 4)

for student in (Vasya, Petya):
    print(f'{student.name} сделал {student.complete_dz} домашних заданий')
