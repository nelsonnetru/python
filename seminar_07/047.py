'''
У  вас  есть  код,  который  вы  не  можете  менять  (так  часто  бывает,  когда  
код  в  глубинепрограммы используется множество раз и вы не хотите ничего сломать):

transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный  способ  вашего  взаимодействия  с  этим  кодом  -  посредством  
заданияфункции transformation.Однако вы поняли, что для вашей текущей задачи 
вам не нужно никак преобразовыватьсписок значений, а нужно получить его как есть.

Напишите  такое  лямбда-выражение  transformation,  чтобы  transformed_values  
получилсякопией values
'''

transformation = lambda x: x

values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transormed_values = list(map(transformation, values))

print(values)
print('-'*20)
print(transormed_values)

if values == transormed_values:
	print('ok')
else:
	print('fail')