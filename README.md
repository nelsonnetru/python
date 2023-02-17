# Изучаем Python на GB
## Домашнее задание №1
* [Задача 1](https://github.com/nelsonnetru/python/tree/main/homework_01/001.py): Найдите сумму цифр трехзначного числа.
```
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
```
* [Задача 2](https://github.com/nelsonnetru/python/tree/main/homework_01/002.py): Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
```
6 -> 1 4 1
24 -> 4 16 4
60 -> 10 40 10
```
* [Задача 3](https://github.com/nelsonnetru/python/tree/main/homework_01/003.py): Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 
```
385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
385916 -> yes
123456 -> no
```
* [Задача 4](https://github.com/nelsonnetru/python/tree/main/homework_01/004.py): Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
```
3 2 4 -> yes
3 2 1 -> no
```
---
## Домашнее задание №2
* [Задача 1](https://github.com/nelsonnetru/python/tree/main/homework_02/001.py): Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
```
Input: 5 -> 5 1 6 5 9
Output: 1 9
```
* [Задача 2](https://github.com/nelsonnetru/python/tree/main/homework_02/002.py): На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.

* [Задача 3](https://github.com/nelsonnetru/python/tree/main/homework_02/003.py): Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
```
Система уравнений: 
| X + Y = S
| X * Y = P

S*Y - Y^2 = P - это квадратное уравнение
Y**2 - S*Y + P = 0
```
* [Задача 4](https://github.com/nelsonnetru/python/tree/main/homework_02/004.py): Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
```
Пример 10: 1, 2, 3
```
---
## Домашнее задание №3
* [Задача 16](https://github.com/nelsonnetru/python/tree/main/homework_03/016.py): Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
```
5
1 2 3 4 5
3
-> 1
```
* [Задача 18](https://github.com/nelsonnetru/python/tree/main/homework_03/018.py): Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
```
5
1 2 3 4 5
6
-> 5
```
* [Задача 20](https://github.com/nelsonnetru/python/tree/main/homework_03/020.py): В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
ценность.Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
---
## Домашнее задание №4
* [Задача 22](https://github.com/nelsonnetru/python/tree/main/homework_04/022.py): Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
```
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
-> 6 12
```
* [Задача 24](https://github.com/nelsonnetru/python/tree/main/homework_04/024.py): В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
```
4 -> 1 2 3 4
9
```
---
## Домашнее задание №5
* [Задача 26](https://github.com/nelsonnetru/python/tree/main/homework_05/026.py): Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
```
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
```
* [Задача 28](https://github.com/nelsonnetru/python/tree/main/homework_05/028.py): Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
```
2 2
4
```
---
## Домашнее задание №6
* [Задача 30](https://github.com/nelsonnetru/python/tree/main/homework_06/030.py): Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: a
n = a1 + (n-1) * d. Каждое число вводится с новой строки.
```
Ввод: 7 2 5
Вывод: 7 9 11 13 15
```
* [Задача 32](https://github.com/nelsonnetru/python/tree/main/homework_06/032.py): Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
```
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
```
---
## Домашнее задание №7
* [Задача 34](https://github.com/nelsonnetru/python/tree/main/homework_07/034.py): Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 

Стихотворение Винни-Пух вбивает в программу с клавиатуры. 
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке..
```
Ввод:
пара-ра-рам рам-пам-папам па-ра-па-дам

Вывод:
Парам пам-пам
```
* [Задача 36](https://github.com/nelsonnetru/python/tree/main/homework_07/036.py): Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
```
Ввод:
print_operation_table(lambda x, y: x * y) 

Вывод:

print_operation_table(lambda x, y: x * y)

1         2         3        4        5       6
2         4         6        8       10      12
3         6         9       12       15      18
4         8        12       16       20      24
5        10        15       20       25      30
6        12        18       24       30      36
```