class Human:
    def __init__(self, name):
        self.name = name

class Car:
    def __init__(self, model):
        self.model = model
        self.peaple = []

    def add_peaple(self, human):
        self.peaple.append(human)

    def info(self):
        print(f"Auto:    {self.model}")
        if self.peaple:
            print("ёёё сейчас тут")
            for p in self.peaple:
                print(p.name)
        else:
            print("тишинаааа. никого нету")





human1 = Human("Abobus")
human2 = Human("Not sigma")


car = Car("Poco x3 pro")
car.add_peaple(human1)
car.add_peaple(human2)
car.add_peaple(human2)
car.add_peaple(human2)
car.add_peaple(human2)
car.add_peaple(human2)
car.add_peaple(human2)
car.add_peaple(human2)
car.add_peaple(human2)
car.info()