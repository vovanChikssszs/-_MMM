class Student:
    print ("bye")
    def __init__(self, name="sigma", height=181, age=13):
        self.name = name
        self.height = height
        self.age = age

    def addYear(self):
        if self.age < 100:
          self.age += 1
    def study(self):
        print("ААААА УЧИТЬСЯЯЯ")
    def info(self):
        print(f"Name       - {self.name}")
        print(f"Age        - {self.age}")
        print(f"Height     - {self.height}")

student1 = Student(name="Sigma",height=181,age=13)
student1.info()

##признаюсь честно помучался с обучением студента спиханул удалил. я не хотел смотреть запись и списывать так как толку от такого не будет. ну спишу я ну и чему научусь (