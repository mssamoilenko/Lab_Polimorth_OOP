#task1
class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Square():
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length

class CircleSquare(Circle, Square):

    def __init__(self, side_length):
        Square.__init__(self, side_length)
        Circle.__init__(self, side_length / 2)

    def description(self):
        return (f"Коло вписане в квадрат:\n"
                f"Сторона квадрата: {self.side_length}\n"
                f"Радіус кола: {self.radius}\n"
                f"Площа квадрата: {self.area()}\n"
                f"Периметр квадрата: {self.perimeter()}\n"
                f"Площа кола: {Circle.area(self)}\n"
                f"Периметр кола: {self.perimeter()}")

figure = CircleSquare(10)
print(figure.description())

#task3
class Pet:
    def __init__(self, name, type_pet):
        self.name = name
        self.type_pet = type_pet
    def sound(self):
        pass
    def type(self):
        return f"Тип підвиду: {self.type_pet}."
    def show(self):
        return self.name
    def __str__(self):
        return f"Моя тварина - {self.show()}. {self.type()} Звук, який вона видає: {self.sound()}."
class Cat(Pet):
    def __init__(self, name, type_pet):
        super().__init__(name, type_pet)
    def sound(self):
        return "мяу"

class Dog(Pet):
    def __init__(self, name, type_pet):
        super().__init__(name, type_pet)
    def sound(self):
        return "гав"

class Hamster(Pet):
    def __init__(self, name, type_pet):
        super().__init__(name, type_pet)
    def sound(self):
        return "хрум-хрум"
class Parrot(Pet):
    def __init__(self, name, type_pet):
        super().__init__(name, type_pet)
    def sound(self):
        return "Красунчик хоррроший"

cat1 = Cat("Кову", "Лисий кіт")
dog1 = Dog("Бобік", "Пес водолаз")
ham=Hamster("Космонавт","Пухнастий хом'як")
par=Parrot("Красунчик","Хвилястий папуга")
print(ham)
print(par)
print(cat1)
print(dog1)
