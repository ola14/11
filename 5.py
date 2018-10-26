#Zapotochna Olha, lab 5
# використати for/while для чисел фібоначі


print('Задайте число')
m = float(input('m = '))
a=b=1
while a < m+1:
        c=a+b
        a=b
        b=c
        
print('Ось це перше число більше за твоє m: ', a)
  



