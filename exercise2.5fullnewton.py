#interpolation by newtons divided difference polynomial
#and finding the roots of the polynomial by newton raphson method

ans = float(input('Enter the guess of the root : '))
from data import xi
from data import yi

#defining a recursive function that would calculate the coefficients of polynomial
def f(m,n):
    if m-n == 1:
        return (yi[m]-yi[n])/(xi[m]-xi[n])
    else:
        return (f(m,n+1)-f(m-1,n))/(xi[m]-xi[n])
    
#creating the divided difference polynomial    
def fn(x):    
    y = 0
    for i in range(1,len(xi)):
        N = f(i,0)
        for j in range(i):
            N = N*(x - xi[j])
        y = y + N
    return y +  yi[0]

#defining the derivative of a function
def dif(f,x):
    return (f(x + 0.000001) - f(x))/0.000001
epsilon = 0.000000000000001

#doing the newton rhapson method for finding the roots of the polynomial
while abs(fn(ans)) >= epsilon:
        ans = ans - (fn(ans)/dif(fn,ans))
print('The approximate root of the polynomial with given data points is ',ans)    
