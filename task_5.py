#Задача 5. Обычный день на работе

total_tasks = 0  
need_to_shop = False 
hour = 1  

print('Начался восьмичасовой рабочий день.')

while hour <= 8:
    print(hour ,'-й час')
    
    tasks = int(input('Сколько задач решит Максим? '))
    total_tasks += tasks  
    
   
    call_answer = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет): '))
    
    if call_answer == 1:
        need_to_shop = True
    
    hour += 1

print('Рабочий день закончился. Всего выполнено задач:' ,total_tasks)

if need_to_shop:
    print('Нужно зайти в магазин.')
