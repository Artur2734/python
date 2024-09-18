# Задача 7. Игра «Угадай число»

print("Загадай число от 1 до 100, а я попробую его угадать за 7 попыток.")
low = 1
high = 100
attempts = 0
while low <= high:
    mid = (low + high) // 2
    attempts += 1
    print(f"Твоё число равно, меньше или больше, чем {mid}?")
    print("1 — равно, 2 — больше, 3 — меньше")
    response = int(input("Твой ответ: "))
    if response == 1:
        print(f"Я угадал твоё число {mid} за {attempts} попыток!")
        break
    elif response == 2:
        low = mid + 1
    elif response ==3:
        high = mid -1
    else:
       print("Пожалуйста, введите 1, 2 или 3.")     

