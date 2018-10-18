#Програмування на мовi пайтон, Лабораторна 4.1, Запоточна Ольга

import math
n=5
y=0
x=0.25
while x>=0.0001:
    x=float((pow(2,n)*math.factorial(n))/pow(n,n))
    y+=x
    n+=1

print ('my result', y)
