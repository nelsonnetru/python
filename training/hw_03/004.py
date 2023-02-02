'''
Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''

digit = 34
print(f'Проверка: {bin(digit)}')
binList = []

while digit > 1:
	binList.append(digit - digit // 2 * 2)
	digit //= 2

result = str(digit) + ''.join(str(x) for x in binList[::-1])
print(result)