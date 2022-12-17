# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
#     *Примеры:* 
#      5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
# number = int(input('Please, enter number:'))
# my_list = []
# for i in range(-number, number+1, 1):
#     my_list.append(i)
# print(*my_list, sep=', ')

# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    # *Примеры:*
    # - 6,78 -> 7
    # - 5 -> нет
    # - 0,34 -> 3
# number = 5
# if number==int(number):
#     print('нет')
# else:
#     print('дробное')
# num = number*10
# num = int(num)%10
# print(num)

# from decimal import Decimal
# number = Decimal(0.56)
# print(number)

# Напишите программу, которая принимает на вход число и проверяет,
# кратно ли оно 5 и 10 или 15, но не 30.

# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#     *Пример:*
#     - Для N = 5: 1, -3, 9, -27, 81
# number = int(input('Enter number:'))
# for i in range(0, number):
#     num = (-3)**i 
#     print(num)

my_list = []
number = int(input('Enter number:'))
for i in range(0, number):
    my_list.append((-3)**i)
print(*my_list, sep = ', ')