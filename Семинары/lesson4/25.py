# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

text = "a a a b c a a d c d d".split()
# list = list()
# for i in range(len(text)):
#    list.append(f"{text[i]}_{text[:i].count(text[i])+1}")

# print(list)
str1 = ""
dict = {}

for i in text:
    if i not in dict:
        str1 +=i + " "
    else:
        str1 += i + "_" + str(dict[i]) + " "
    dict[i] = dict.get(i, 0)
    dict[i] += 1

print(str1)
print(dict)
