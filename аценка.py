баллы = int(input("Введите количество баллов (0-100): "))

if 0 <= баллы <= 49:
    оценка = "Миша всё очень плохо давай по новой (>:( цензура )"
elif 50 <= баллы <= 69:
    оценка = "Такое се"
elif 70 <= баллы <= 89:
    оценка = "Норм"
elif 90 <= баллы <= 99:
    оценка = "Красава"
elif 99 <= баллы <= 100:
    оценка = "ФУУУ ЗАДРОТ"

print(f"Оценка: {оценка}")