#interpolating by the nwton divided difference polynomial formation
x = float(input('Enter the number : '))
from data import xi
from data import yi
y = 0
#defining a recursive function to find th coefficients in the polynomial
def f(m,n):
    if m-n == 1:
        return (yi[m]-yi[n])/(xi[m]-xi[n])
    else:
        return (f(m,n+1)-f(m-1,n))/(xi[m]-xi[n])
    
#creating the polynomial
for i in range(1,len(xi)):
    N = f(i,0)
    for j in range(i):
        N = N*(x - xi[j])
    y = y + N
y = y +  yi[0]    

print(y)    
    
