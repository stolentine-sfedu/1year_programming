# Вводим стоимость билета price и процент скидки discount (целое)
price = int(input("Введите цену: "))
discount_percent = int(input("Введите скидку (целое): "))

# вычисляем  сумму скидки и финальную цену
discount_sum = price * discount_percent / 100
final_price = price - discount_sum

discount_total = -1 * discount_sum
# выввод финальной цены и скидки 
print(f"Итоговая цена: {final_price:.2f}")
print(f"Сумма скидки: {discount_total:.2f}")
