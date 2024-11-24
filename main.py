import random 
count = 0
unique = []
spisok1 = [] 
numbers = int(input("Введите целое число: "))
for i in range(20): #Генерируем список
    spisok = [random.randint(-10, 10) for i in range(4)] 
    spisok1.append(spisok)
for i in spisok1:# Проверка уникальности и суммы
    if i not in unique:
        unique.append(i) 
    if sum(i) < numbers:  # Проверка суммы
        count += 1
print(f"Уникальные значения: {tuple(unique)}") # Выводим все
print(f"Количество пар, чья сумма меньше заданного пользователем значения: {count}")
