
__author__ = 'Иванов Евгений Иванович'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.
import random
number = random.randint(1, 999999)
print(number)
maxNum = 0
while number:
    digit = number % 10
    if maxNum < digit:
        maxNum = digit
    number //= 10
print(maxNum)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.
a = (input("Введите значение переменной a: "))
b = (input("Введите значение переменной b: "))
a, b = b, a
print("Значение a:", a, "\nЗначение b:", b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4
import math
a = int(input("Введите значение коэффициента a: "))
b = int(input("Введите значение коэффициента b: "))
c = int(input("Введите значение коэффициента c: "))
print("Решим уравнение: ", a, "x² + ", b, "x + ", c, " = 0")
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("x1 = ", x1, "\nx2 = ", x2)
elif d == 0:
    x1 = x2 = -b / (2 * a)
    print("x1 = x2 = ", x1)
elif d < 0:
    print("Корень квадратного уравнения не извлекается")