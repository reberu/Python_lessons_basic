import math
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
def fibonacci(n, m):
    fib1 = 1
    fib2 = 1
    i = 2
    result = []
    while i < m:
        fib_sum = fib2 + fib1
        fib1 = fib2
        fib2 = fib_sum
        i += 1
        if i >= n:
            result.append(fib_sum)
    print(result)

fibonacci(4, 7)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for i in range(len(origin_list)):
        for j in range(len(origin_list) - 1, i, -1):
            if origin_list[j] < origin_list[j - 1]:
                origin_list[j], origin_list[j - 1] = origin_list[j - 1], origin_list[j]
    print(origin_list)

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
A1 = [0, 0]
A2 = [1, 3]
A3 = [4, 3]
A4 = [3, 0]

a = math.sqrt(pow(A2[0] - A1[0], 2) + pow(A2[1] - A1[1], 2))
b = math.sqrt(pow(A3[0] - A2[0], 2) + pow(A3[1] - A2[1], 2))
c = math.sqrt(pow(A4[0] - A3[0], 2) + pow(A4[1] - A3[1], 2))
d = math.sqrt(pow(A1[0] - A4[0], 2) + pow(A1[1] - A4[1], 2))

if a == c and b == d:
    print("Похоже на параллелограм")
else:
    print('Это не параллелограм')

# Здесь будет описание явных признаков параллелограма
