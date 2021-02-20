import matplotlib.pyplot as plt
import numpy as np
import math
from statistics import mean
import scipy
from scipy import misc
from scipy import stats


def p(mass, velocity):
    mass = float(mass)
    velocity = float(velocity)
    return mass*velocity

def p2(Force, time):
    Force = float(Force)
    time = float(time)
    return Force*time

def a(mass, Force):
    mass = float(mass)
    Force = float(Force)
    return Force/mass




# --------------------
x0 = 5

def f(x):
    return x**2

def f1(x):
    return m*x + x0

def derive(function, value):
    h = 0.00000000001
    top = function(value + h) - function(value)
    bottom = h
    slope = top / bottom
    return float("%.3f" % slope)

m = derive(f, x0)

x = np.arange(-10.0, 10.0, 0.5)

y = f(x)
y1 = f1(x)

plt.plot(x, y,'blue')
plt.plot(x, y1,'red')
plt.grid(True)

plt.text(-5, 100.0,
     r"$f(x)=x^2$", 
     horizontalalignment='center',
     fontsize=12,color='red')
plt.text(-5, 50.0,
     r"$f'(x)=$" + str(m) + 'x' + ' + ' + str(x0), 
     horizontalalignment='center',
     fontsize=12,color='blue')
plt.text(0, 150.0,
     'actual slope value' + str(stats.linregress(x, y1)), 
     horizontalalignment='center',
     fontsize=10,color='black') 
plt.text(0, 200.0,
     'derivative of f(x) @ x0 = ' + str(m), 
     horizontalalignment='center',
     fontsize=10,color='black') 
plt.style.use('seaborn-whitegrid')
plt.grid(color='black', linestyle='-', linewidth=0.5)
plt.title('derivative calculator xd')
plt.plot(x, y, scalex=True, scaley=True)
plt.show() 


