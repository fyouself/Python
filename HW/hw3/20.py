# *Задача 20: * В настольной игре Скрабл (Scrabble)
# каждая буква имеет определенную ценность. В случае с английским 
# алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; 
# J, X – 8 очков; Q, Z – 10 очков. 
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# удем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.

# *Пример:*

# ноутбук
#     12

# list1 = ("A, E , I, O, U, L, N, S, T, R А, В, Е, И, Н, О, Р, С, Т")
# list2 = ("D, G , Д, К, Л, М, П, У " )
# list3 = ("B, C, M, P, Б, Г, Ё, Ь, Я ")
# list4 = ("F, H, V, W, Y, Й, Ы ")
# list5 = (" Ж, З, Х, Ц, Ч ")
# list8 = ("Ш, Э, Ю")
# list10 = ("Ф, Щ, Ъ")

# text = input("Введите слово - ")
# res= 0
# for i in text.upper():
#     if i in list1: res+=1
#     elif i in list2: res+=2
#     elif i in list3: res+=3
#     elif i in list4: res+=4
#     elif i in list5: res+=5
#     elif i in list8: res+=8
#     elif i in list10: res+=10

# print(res)


points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JZ', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
word = input().upper() # переводим все буквы в верхний регистр
count = 0
for i in word:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        for j in points_en:
            if i in points_en[j]:
                count = count + j
    else:
        for j in points_ru:
            if i in points_ru[j]:
                count = count + j
print(count)