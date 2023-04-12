# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

n = int(input("Write number - "))

res = 1
temp = 0
count = 2
while res <= n:
    if res == n:
        print(f"Число {n} является {count} по счету")
        break
    res += temp
    temp = res - temp
    count +=1
    
if res > n:
    print("-1")  
    
    
