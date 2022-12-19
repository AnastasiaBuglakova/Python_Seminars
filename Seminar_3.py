# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# my_list = ['4dfg', '086jhgf', '999dfgh', 'fghj4']
# search = input('enter a number: ')
# for item in my_list:
#     if search in item:
#         print('yyeee')
#         break
# else:
#     print('net')


# trigger = True
# my_list = ['4dfg', '086jhgf', '999dfgh', 'fghj4']
# search = input('enter a number: ')
# for item in my_list:
#     if search in item:
#         trigger = False
#         print('yyeee')
        
# if trigger:
#     print('net')


#     3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

my_list = []
search = input('Please, enter string of symbols: ')
position=0
print(my_list)
count = 0
for item in my_list:
    if search==item:
        count +=1
    if count == 2:
        break
    position+=1
if count >=2:
    print(position)
else:
    print('-1')
