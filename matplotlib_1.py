from numpy import*
from math import*
import matplotlib.pylab as plt
x = linspace(1,7,10)
y = 5*sin(10*x)*sin(3*x)/pow(x,2)

plt.plot(x,y,'g--', label = '')
plt.axis([1,7,-1,1])
plt.xlabel('x')
ply.ylabel('y')
plt.savefig('y.png', dpi = 200)


plt.title('TASK 1, example 8')
plt.legend()


plt.show()
