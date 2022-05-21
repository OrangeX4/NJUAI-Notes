class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"please sit down {self.name}")


class Battery:
    def __init__(self, size):
        self.size = size

    def describe(self):
        print(f"The size is{self.size}")


class ElectriCar(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.Body = Battery(75)


my = ElectriCar("kk", 16)