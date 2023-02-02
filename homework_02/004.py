﻿'''
Задача 4: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
Пример 10: 1, 2, 3

0 - целое число
для N = 1: 2^0 == N
'''

N = int(input('Введите число N: '))

powTwo = 0
while 2**powTwo <= N:
	powTwo += 1

print('Целые степени двойки 2^k <= N: ')
print(*range(powTwo))