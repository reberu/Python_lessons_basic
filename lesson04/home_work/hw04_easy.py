# Все задачи текущего блока решите с помощью генераторов списков!
import random

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
list1 = []
list2 = []
for i in range(10):
    list1.append(random.randint(0, 100))
for i in list1:
    list2.append(i ** 2)
print(list1, '--> ', list2)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
fruits = ['pineapple', 'orange', 'mango', 'peach', 'apple', 'banana', 'kiwi', 'strawberry']
fruit1 = []
fruit2 = []
intersection = []
for i in range(len(fruits) - random.randint(0, len(fruits) - 1)):
    fruit1.append(fruits[random.randint(0, len(fruits) - 1)])
for i in range(len(fruits) - random.randint(0, len(fruits) - 1)):
    fruit2.append(fruits[random.randint(0, len(fruits) - 1)])
for i in fruit1:
    if i in fruit2:
        intersection.append(i)
print(intersection)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
list1.clear()
list2.clear()
for i in range(10):
    list1.append(random.randint(0, 100))
for i in list1:
    if (i % 3 == 0) and (i > 0) and (i % 4 != 0):
        list2.append(i)
print(list2)
