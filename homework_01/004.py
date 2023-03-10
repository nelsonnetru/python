'''
Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
3 2 4 -> yes
3 2 1 -> no

Решение: 
1. должно быть обязательно k < m*n
2. k должно делиться без остатка на дольки одной из сторон k%m == 0 or k%n == 0 

'''

m = int(input('Количество долек m = '))
n = int(input('Количество долек n = '))
k = int(input('Количество долек k = '))

if (m * n > k) and (k%m == 0 or k%n == 0):
	print('yes')
else:
	print('no')