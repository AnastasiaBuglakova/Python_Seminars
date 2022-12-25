# Наше решение на семинаре
# my_str = 'A*x**2 + B*x -C = 0'
# def conv(my_str):
#     new_str = my_str.split('x')
#     print(new_str)
#     new_str2=[]
#     for i in range(len(new_str)):
#         new_str2.append(new_str[i].replace('**2','').replace('*','').replace(' ','').replace('+','').replace('=','').replace('0',''))
#     return new_str2

# stringa = '-3*x**2 + 78*x - 9=0'
# str_new = conv(stringa)
# for i in range(3):
#     str_new[i] = int(str_new[i])
#     print(type (str_new[i]))
# print(str_new)
# def parabola (list):
#     x1 = (-str_new[0] - (str_new[1]**2 - 4*str_new[0]*str_new[2]))/(2*str_new[0])
#     x2 = (-str_new[0] + (str_new[1]**2 - 4*str_new[0]*str_new[2]))/(2*str_new[0])
#     print(x1, x2)
# print(parabola (str_new))
import math
equation = '32*x**2 + 7*x -1 = 0'
def create_koef(equation: str) -> tuple:
    new_koef = []
    nq = equation.replace(' ','').replace('=0','').replace('+',' ').replace('-',' -').split(' ')
    print(nq)
    for item in nq:
        if item.startswith('x'):
            new_koef.append('1')
        elif item.startswith('-x'):
            new_koef.append(-1)
        else:
            new_koef.append(int(item.split('*x')[0]))
    print(new_koef)
    return new_koef

def solution(koef: list):
    a, b, c = koef
    a = 32
    b = 7
    c = -1
    disc = b**2 - 4*a*c
    if disc > 0:
        x1= (-b+math.sqrt(disc))/(2*a)
        x2= (-b-math.sqrt(disc))/(2*a)
        return x1, x2
    elif disc==0:
        x= -b/(2*a)
        return x
    else:
        return None

print(solution(create_koef(equation)))
