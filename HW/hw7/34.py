# # Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
#  Поскольку разобраться в его кричалках не настолько просто, насколько легко 
# он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм 
# есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения
# одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры
# . В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке

# # *Пример:*

# # **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
# #     **Вывод:** Парам пам-пам  

data = input("Введите стих: ").split()
glasny_bukvi = [ "а","e","о","и"]

def slog(data):
    for x in data: 
        sum = 0 
        for y in x: 
            if y in glasny_bukvi: sum +=1
        if sum%2 > 0: return "Пам парам"    
    return "Парам пам-пам"    

print(slog(data))