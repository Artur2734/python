name_debtor = input("Введите имя должника: ")
debt = int(input("{name_debtor}, вваша задолженность составляет сколько рублей? "))
while debt > 0:
    payment = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? '))
    if payment >= debt:
        print('Отлично', name_debtor, 'Вы погасили долг. Спасибо!')
        break
    else:
        print('Маловато', name_debtor, 'Давайте ещё раз.')

