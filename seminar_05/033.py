'''
Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
'''
import random

vasya_list = [random.randint(1,5) for i in range (6)]
print(f"Исходные отметки: {vasya_list}")

minDigit = min(vasya_list)
maxDigit = max(vasya_list)

for x in range(len(vasya_list)):
	if vasya_list[x] == maxDigit : vasya_list[x] = minDigit

print(f"Итоговые отметки: {vasya_list}")