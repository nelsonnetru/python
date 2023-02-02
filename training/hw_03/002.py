'''
Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''

import random
rndList = [random.randint(1,9) for x in range(5)]
print(rndList)

end = len(rndList) // 2 + (len(rndList) % 2 > 0)
resList = list()

for i in range(end):
	resList.append(rndList[i] * rndList[len(rndList)-1-i])
	print(f'{rndList[i]} * {rndList[len(rndList)-1-i]} = ' + str(resList[-1]))

print()
print(resList)