'''
Задача No49. Решение в группах

Планеты вращаются вокруг звезд по эллиптическим орбитам. 
Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. 
Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит 
планет найдет ту, по которой вращается самая далекая планета. Круговые орбиты не 
учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные 
спутники были запущены на круговые орбиты. Результатом функции должен быть кортеж, 
содержащий длины полуосей эллипса орбиты самой далекой планеты. 

Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. 
Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. 

При решении задачи используйте списочные выражения. Подсказка: проще всего будет 
найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем 
найти и сам эллипс, имеющий такую  площадь. Гарантируется, что самая далекая планета 
ровно одна. 

Ввод:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

print(*find_farthest_orbit(orbits))
Вывод:2.5 10
'''
from math import pi
'''
def find_farthest_orbit(list_of_orbits):
	return_index = 0
	S_max = pi*list_of_orbits[return_index][0]*list_of_orbits[return_index][1]

	for i in range(len(list_of_orbits)):
		if list_of_orbits[i][0] !=  list_of_orbits[i][1]:
			S_item = pi* list_of_orbits[i][0]* list_of_orbits[i][1]
			if S_item > S_max: 
				S_max = S_item
				return_index = i

	return list_of_orbits[return_index]
'''
def find_farthest_orbit(list_of_orbits):
	list_ellipse_orbits = [(i[0], i[1]) for i in list_of_orbits if i[0] != i[1]]
	list_S_orbits = [pi * x[0] * x[1] for x in list_ellipse_orbits]
	return list_ellipse_orbits[list_S_orbits.index(max(list_S_orbits))]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

print(*find_farthest_orbit(orbits))