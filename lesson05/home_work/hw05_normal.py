# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"
import os

while True:
    print('1. Перейти в папку')
    print('2. Просмотреть содержимое папки')
    print('3. Удалить папку')
    print('4. Создать папку')
    print('5. Завершить программу')
    choice = input('Выберите нужную операцию: ')
    path = os.getcwd()
    if choice == '5':
        print('Всего хорошего!')
        break

    elif choice == '1':
        dirname = input('Введите название папки: ')
        fullpath = str(path) + r"\\" + dirname
        if os.path.exists(fullpath):
            os.chdir(fullpath)
            print('Успешно перешли в папку. Текущая директория: ' + os.getcwd())
            break
        else:
            print('Невозможно перейти в папку')
            break

    elif choice == '2':
        print('Содержимое папки:')
        for i in os.listdir(os.getcwd()):
            print(i)
        break

    elif choice == '3':
        dirname = input('Введите название папки: ')
        fullpath = str(path) + r"\\" + dirname
        if os.path.exists(fullpath):
            os.rmdir(fullpath)
            print('Успешно удалена папка ' + dirname)
            break
        else:
            print('Невозможно удалить папку')
            break

    elif choice == '4':
        dirname = input('Введите название папки: ')
        fullpath = str(path) + r"\\" + dirname
        if not os.path.exists(fullpath):
            os.mkdir(fullpath)
            print('Успешно создана папка ' + dirname)
            break
        else:
            print('Невозможно создать папку')
            break

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
