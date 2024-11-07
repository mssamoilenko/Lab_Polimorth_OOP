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
#task2
class Wheels:
    def __init__(self, number_of_wheels):
        self.number_of_wheels = number_of_wheels

    def show_wheels(self):
        return f"Кількість коліс: {self.number_of_wheels}"

class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def show_engine(self):
        return f"Тип двигуна: {self.engine_type}"

class Doors:
    def __init__(self, number_of_doors):
        self.number_of_doors = number_of_doors

    def show_doors(self):
        return f"Кількість дверей: {self.number_of_doors}"

class Car(Wheels, Engine, Doors):
    def __init__(self, number_of_wheels, engine_type, number_of_doors, car_model):
        Wheels.__init__(self, number_of_wheels)
        Engine.__init__(self, engine_type)
        Doors.__init__(self, number_of_doors)
        self.car_model = car_model

    def show_car(self):
        return (f"Модель автомобіля: {self.car_model}\n"
                f"{self.show_wheels()}\n"
                f"{self.show_engine()}\n"
                f"{self.show_doors()}")

car = Car(number_of_wheels=4, engine_type="Бензиновий", number_of_doors=4, car_model="Toyota Camry")
print(car.show_car())
#task4,5
class Employer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Print(self):
        return "This is Employer class"

    def __str__(self):
        return f"Employer: {self.name}, Age: {self.age}"

    def __int__(self):
        return self.age

class President(Employer):
    def Print(self):
        return f"{self.name} is the President of the company"

    def __str__(self):
        return f"President: {self.name}, Age: {self.age}"

class Manager(Employer):
    def Print(self):
        return f"{self.name} is a Manager in the company"

    def __str__(self):
        return f"Manager: {self.name}, Age: {self.age}"

class Worker(Employer):
    def Print(self):
        return f"{self.name} is a Worker in the company"

    def __str__(self):
        return f"Worker: {self.name}, Age: {self.age}"

president = President("Alla", 55)
manager = Manager("Don", 40)
worker = Worker("Kai", 30)

print(president.Print())
print(manager.Print())
print(worker.Print())

print(str(president))
print(int(manager))
print(str(worker))
