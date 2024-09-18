#Задача 3. Слишком большие числа

number = int(input("Введите число: "))
digit_count = 0
if number == 0:
    digit_count = 1
else:
    number = abs(number)
    while number > 0:
        number //= 10
        digit_count += 1
print(f"Количество цифр в числе: {digit_count}")