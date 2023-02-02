'''
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''
import random

rndList = [random.randint(1,99) + round(random.random(), 2) for i in range(5)]
rem = [round(i-int(i), 2) for i in rndList] # список дробных частей

print(rndList)
print(rem)
print(f'{max(rem)} - {min(rem)} = ' + str(round(max(rem) - min(rem), 2)))