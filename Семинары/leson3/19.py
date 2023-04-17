# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]

list = [1, 2, 3, 4, 5]
k = 1

# list2 = []
# for i in range(len(list)):
#     list2.append(list[i-k])

# print(list2)

for i in range(k):
    list.insert(0,list.pop())

print(list)

