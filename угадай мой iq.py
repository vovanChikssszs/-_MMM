import random
число = random.randint(1, 300)
while True:
    пытка = int(input("Угадайте моё iq от 1 до 300: "))

    if пытка < число:
        print("больше")
    elif пытка > число:
        print("меньше")
    else:
        print("Угадал. но это не моё iq если число было больше 5")
        break
##дя будет до 300 из-за мемов