'''
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:
- для k = 8 список будет выглядеть так: 
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
'''

k = 8

fiboList = [0, 1]

for i in range (2, k+1):
	fiboList.append(fiboList[i-1] + fiboList[i-2])

negaFibo = fiboList.copy()

for i in range(2, k+1, 2):
	negaFibo[i] = -negaFibo[i]

negaFibo.pop(0)
resultList = negaFibo[::-1] + fiboList
print(resultList)