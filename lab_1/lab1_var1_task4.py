# Вводим целые числа для вычисления выражения.
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))
e = -1

while True:
    e = int(input("Введите e (не равно 0): "))

    if e != 0:
        break

    print("Вы ввели 0. Число e не должно быть равно 0. Введите ДРУГОЕ число!")


# Считаем и выводим

# разность
sub_ab = a - b
print(f"a - b = {sub_ab}")

# степернь
d_pow = d ** 2
print(f"d ** 2 = {d_pow}")

# целочисленное деление
division_result = d_pow // e
print(f"d ** 2 // e = {division_result}")

# расчет и вывод нескольких операций
result = sub_ab * c + division_result
print(f"(a - b) * c + d ** 2 // e. = {result}")
