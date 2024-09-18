#Задача 4. Поставьте оценку!

positive_count = 0
negative_count = 0
number = int(input('Введите число (0 для завершения): '))
while number != 0:
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    number = int(input('Введите число (0 для завершения): '))
print('Положительных чисел:' , (positive_count))
print('Отрицательных чисел:' , (negative_count))