# вводим вес багажа
first_weight = float(input("Введите вес первого багажа: "))
second_weight = float(input("Введите вес второго багажа: "))
third_weight = float(input("Введите вес третьего багажа: "))

# вычислям общий и средний вес
total = first_weight + second_weight + third_weight
avg = total / 3

# выводим результаты с точностью до 2 знаков после запятой
print(f"Общий вес: {total:.2f}")
print(f"Средний вес: {avg:.2f}")
