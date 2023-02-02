'''
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов
 списка, стоящих на нечётной позиции.

Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''

import random

rndList = [random.randint(1,9) for i in range(5)]
print (rndList)
print ('+'.join(str(x) for x in rndList[1::2]) + '=', end = '')
print(sum(rndList[1::2]))