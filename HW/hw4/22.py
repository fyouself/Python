# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются
# в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами 
# элементы множеств.

import random

n = int(input('Введите кол-во элементов первого множества - '))
m = int(input('Введите кол-во элементов первого множества - '))

list_n = []
list_m = []

for i in range(n):
    list_n.append(random.randint(0,20))
for i in range(m):
    list_m.append(random.randint(0,20))

print(list_n)
print(list_m)

list_n = set(list_n)
list_m = set(list_m)

mn = list_n.intersection(list_m)

print(mn)