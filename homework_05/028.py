'''
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.

2 2
4
'''
def recSumm(numberA: int, numberB: int):
	if numberB == -1:
		return 0
	numberB -= 1
	return (numberA + recSumm(1, numberB))

A = int(input("Введите число А: "))
B = int(input("Введите число B: "))

print(f"A + B = {recSumm(A, B)}")