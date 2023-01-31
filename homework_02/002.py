'''
Задача 2: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
'''
import random

n = int(input('Количество монет: '))
if n < 1: exit()

sideName = ['герб', 'решка'] # 0 - герб, 1 - решка

monets = [random.randint(0, 1) for i in range(n)]
print(monets)

print('\nВыпавшие монеты:')
for side in monets:
	print(f'{side} - ' + sideName[side])

minimalSide = 0 if monets.count(0) < monets.count(1) else 1
reverseMonets = monets.count(minimalSide)

print(f'\nМинимальное количество монет для переворота: {reverseMonets}')

if reverseMonets > 0:
	print(f'Нужно перевернуть монеты, которые лежат стороной: {sideName[minimalSide]}')