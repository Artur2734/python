N = int(input("Введите значение N: "))
if N > 0:
    count = 1
    while count <= N:
        cube = count ** 3 
        print(f"{count} в третьей степени равно {cube}")
        count += 1 
else:
    print("Значение N должно быть положительным числом.")
