# 2- Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности. 
# Посмотрели, что такое множество? Вот здесь его не используйте.

import random

spisok = [random.randint(1,9) for i in range(0,10)]

print(spisok)

new_spisok = [i for i in spisok if spisok.count(i) < 2]

print(new_spisok)