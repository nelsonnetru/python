﻿'''
Задача №31. Решение в группах
Последовательностью Фибоначчи называется
последовательность чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

0, 1, 1, 2, 3, 5, 8, 13, 21, 34

Требуется найти N-е число Фибоначчи

Input: 7
Output: 21
'''

def fibo(n):
	if n in (0, 1): return 1
	else: return (fibo(n-1) + fibo(n-2) )

n = int(input("Число: "))
print (fibo(n-2))