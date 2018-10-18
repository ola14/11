#Lab_4.3 Zapotochna Olya
import math
print ('Python, Lab 4.3')
print('Zapotochna O')

print('Задайте число')
a = float(input('a = '))
print('Задайте значення для х')
x = float(input('x = '))

n = 0

while abs((x ** 2) - a) > 0.0001:
	x = (1/2)*(x + a / x) 
	n += 1
print(float(x))
