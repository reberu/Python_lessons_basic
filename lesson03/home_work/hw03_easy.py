# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    integer, fractional = map(int, str(number).split(".", 1))
    lst = list(str(fractional))
    lst = list(map(int, lst))
    if len(lst) > ndigits: round()
        count = len(lst) - 1
        while count > 0:
            if lst[count] >= 5:
                lst[count - 1] = lst[count - 1] + 1
                lst[count] = 0
            else:
                lst[count - 1] = lst[count - 1] - 1
            count -= 1
    fractional = ''.join(str(e) for e in lst)
    fractional = fractional[0:ndigits+1]
    result = str(integer) + "." + fractional
    return result

print(my_round(2.1234567, 3))
print(my_round(2.1999967, 3))
print(my_round(2.9999967, 3))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    pass


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
