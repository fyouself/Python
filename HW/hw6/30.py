# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15
a1 = int(input("Введите первое число - "))
d = int(input("Введите разность - "))
n = int(input("Введите количество элементов - "))

for i in range(n):
    print(a1 + i*d, end=' ')