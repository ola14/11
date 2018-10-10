#Програмування на мов пайтон, Лабораторна 3, Запоточна Ольга
print('Python, Lab 3 \nZapotochna Olga PMM-2')
print('enter variables:')
from math import *
y = float(input('y = '))
x = float(input('x = '))
if x>=0 and y >=0 :
    print(sqrt(pow(x,3)-pow(y,3))+log10(x+5))
else: print('choose values greater than 0')

