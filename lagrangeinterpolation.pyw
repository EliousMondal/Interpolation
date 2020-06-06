'''Author - MD ELIOUS ALI MONDAL
   Created - 30/06/2017'''
#doing interpolation by the lagrange method
x = float(input('Enter a number to find the value of bassil function there : '))
from data import xi
from data import yi

y = 0
i = 0
j = 0
for i in range (len(xi)):
    L = 1
    for j in range(len(xi)):
        if j != i:
            L = L * ((x - xi[j])/(xi[i] - xi[j]))   
    y = y + (yi[i] * L)
print(y)    
