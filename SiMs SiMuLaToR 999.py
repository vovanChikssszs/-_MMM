import random

class Human:
    def __init__(self, name, car=None, job=None):
        self.name = name
        self.house = House()
        self.car = car
        self.job = job
        self.money = 101

    def work(self):
        self.money += 20
        print("Работаю в шараге")

    def eat(self):
        self.house.food -= random.randint(1, 10)
        print("Я покушал")

    def shopping(self):
        self.money -= random.randint(1, 10)
        if self.car is None:
            print("Прогулялся до магаза")
        else:
            if self.car.drive(random.randint(1, 10) * 10):
                print("Проехался до магаза")
            else:
                print("Пробежался до магаза")

    def chill(self):
        self.money -= random.randint(10, 20)
        print("Хорошо отдохнул хы")

    def info(self):
        print(f"Деньги - ${self.money}")
        print(self.house)
        if self.car is not None:
            print(self.car)

    def live(self, day):
        print(f"День №{day}:")
        choice = random.randint(1, 4)
        if choice == 1:
            self.work()
        elif choice == 2:
            self.shopping()
        elif choice == 3:
            self.eat()
        else:
            self.chill()

    def is_alive(self):
        return self.money >= 0


class House:
    def __init__(self):
        self.food = 0
        self.pollution = 0

    def __str__(self):
        return f"Инфо о доме: еда = {self.food}, чистота = {self.pollution}"


class Car:
    def __init__(self, model):
        self.model = model
        self.fuel = 60
        self.state = 100

    def drive(self, length):
        delta_fuel = length * 0.1
        if self.fuel - delta_fuel < 0:
            print("Нету бензина")
            return False
        else:
            self.fuel -= delta_fuel
            self.state -= length * 0.01
            print(f"Мы проехали {length}. Осталось топлива: {self.fuel:.1f}")
            return True

    def add_fuel(self, fuel):
        if self.fuel + fuel <= 60:
            self.fuel += fuel
        else:
            self.fuel = 60

    def __str__(self):
        return f"Машина {self.model}\n Бензина - {self.fuel:.1f} л, состояние - {self.state:.1f}%"


class Job:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


car = Car("BMW X12")
print(car.drive(100))
print(car.drive(100000))
print(car)

job = Job("Programmer", 1000)
human = Human("Vovawe", car, job)

# Пример симуляции жизни персонажа
for day in range(1, 8):
    if human.is_alive():
        human.live(day)
        human.info()
    else:
        print(f"{human.name} не смог выжить...")
        break
