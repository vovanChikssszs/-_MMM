from sys import int_info
import random

class Student:

    def __init__(self, name):
        self.name = name
        self.gladness = 30
        self.progress = 30
        self.alive = True
        self.energy = 100


    def study(self):
        print("Я пашёл ачиться ")
        self.progress += 2
        self.energy -= 1
        self.gladness -= 1


    def sleep(self):
        print("я пашёл спать или ЖЕ ИГРАТЬ В БРАВЛ СТАРСТ ДО 5 УТРААААА")
        self.energy += 1
        self.gladness += 1



    def chill(self):
        print("Я какаю")
        self.gladness += 3
        self.energy += 5
        self.progress -= 2


    def info(self):
        print(f"Сегодня у {self.name} есть")
        print(f"Довольность :    {self.gladness}")
        print(f"Знания      :    {self.progress}")
        print(f"ЭНЕРГЕТИКИИ :    {self.energy}")




    def is_alive(self):
        if self.progress < 0:
            print("Я аутист")
            self.alive = False
        if self.gladness < 0:
            print("1000-7")
            self.alive = False
        if self.progress > 100:
            print("Я здох из-за того я слишком умный")
            self.alive = False
        if self.energy < 0:
            print("Я потерял связь с космосом")
            self.alive = False

    def live(self, day):
        print(f"День №{day} с жизни {self.name}")
        print("-" * 30)
        rnd = random.randint(1, 3)
        if rnd == 1:

            self.study()
        elif rnd == 2:

            self.chill()

        elif rnd == 3:
            self.sleep()

        self.info()
        self.is_alive()



st = Student("Sigma")
for d in range(1, 366):
    if not st.alive:
        break
    st.live(d)


#забудьте что писал я в прошлом разе