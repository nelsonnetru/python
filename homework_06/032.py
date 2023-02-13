'''
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)


Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
'''
import random 

list_x = [random.randint(-10, 10) for i in range(11)]
print(list_x)

minimum = int(input("Минимальное значение элемента: "))
maximum = int(input("Максимальное значение элемента: "))

list_index = []
for i in range(len(list_x)):
    if list_x[i] >= minimum and list_x[i] <= maximum:
        list_index.append(i)

list_index.sort()
print(f"Индексы элементов и данного диапазона: {list_index}")