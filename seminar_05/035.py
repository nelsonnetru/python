﻿'''
Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
'''

def isSimpleNumber (n: int):
	for i in range (2, n):
		if n%i == 0: return False

	return True

n = int(input("Введите число: "))

if isSimpleNumber(n): print ("Это простое число")
else: print ("Не является простым числом")