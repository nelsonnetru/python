'''
Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.

A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8

'''

def goPow (numberA: int, numberB: int):
	if numberB == 1: 
		return numberA
	numberB -= 1
	return numberA*goPow(numberA, numberB)

A = int(input("Введите число А: "))
B = int(input("Введите число B: "))

print(f"A^B = {goPow(A, B)}")