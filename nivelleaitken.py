'''Author - MD ELIOUS ALI MONDAL
   Created - 30/06/2017'''
#interpolating by the nivelle aitken method
x = float(input('Enter a number to find the value of function there : '))
from data import xi
from data import yi
def f(i,j):
    if j - i == 1:
        return ((x - xi[j])/(xi[i] - xi[j]))*yi[i] + ((x - xi[i])/(xi[j] - xi[i]))*yi[j]
    else:
        return ((x - xi[j])/(xi[i] - xi[j]))*f(i,j-1) + ((x - xi[i])/(xi[j] - xi[i]))*f(i+1,j)
print(f(0,len(xi)-1))    
