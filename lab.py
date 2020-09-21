#import tensorflow as tf
#from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
#import pandas as import pd
import math 
from statistics import mean
from scipy import stats

'''
def calc_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg
def calc_minmax(num):
    maxmin = (max(num) - min(num)) / 2.00000000
    return maxmin
def calc_square(num):
    for i in num:
        print(i**2.00)
def calc_minmaxsqr(num):
    return ((max(num))**2-(min(num))**2) / 2.0000
'''

# UP-TO-DATE DATA STARTS BELOW--DARCY PLS FIX THIS SHIT
points = [
    [2.0, (1.67*(10**-5))],
    [4.0, (4.17*(10**-6))],
    [6.0, (1.85*(10**-6))],
    [8.0, (1.04*(10**-6))],
    [10.0, (6.67*(10**-7))]
]

points2 = [
    [1/2.0, 1/(1.67*(10**-5))],
    [1/4.0, 1/(4.17*(10**-6))],
    [1/6.0, 1/(1.85*(10**-6))],
    [1/8.0, 1/(1.04*(10**-6))],
    [1/10.0, 1/(6.67*(10**-7))]
]

deltapoints =[
    [(1/2.0)**2, (1.67*(10**-5))],
    [(1/4.0)**2, (4.17*(10**-6))],
    [(1/6.0)**2, (1.85*(10**-6))],
    [(1/8.0)**2, (1.04*(10**-6))],
    [(1/10.0)**2, (6.67*(10**-7))]
]


# DARCY PLS FIX THIS SOMETIME WTF
x, y = [], []
for i in range(len(points)):
    x.append(deltapoints[i][0])
    y.append(deltapoints[i][1])

a, b = [], []
for i in range(len(points)):
    a.append(points2[i][0])
    b.append(points2[i][1])




'''

xs = np.array(a, dtype=np.float64)
ys = np.array(b, dtype=np.float64)

def lobf(x,y):
    m = (((mean(x)*mean(y))-mean(x*y))/((mean(x)*mean(x))-mean(x*x)))
    b = mean(y)-(m*mean(x))
    return m, b
m, b =lobf(xs, ys)
reg_line = []
'''

# REGRESSION FIXED - DO NOT CHANGE
#coef = np.polyfit(a, b, 1)
#poly1d_fn = np.poly1d(coef) 
#plt.plot(x,y, 'yo', x, poly1d_fn(x), '--k')
#plt.xlim(XXXX, XXXX)
#plt.ylim(XXXX, XXXX)

# LINREGRESS 2.0
'''
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print("slope: %f    intercept: %f" % (slope, intercept))
print("R-squared: %f" % r_value**2)
plt.plot(x, intercept + slope*x, 'r', label='fitted line')
'''

plt.style.use('seaborn-whitegrid')
plt.scatter(x, y, c = 'red')
plt.plot(x, y)
plt.title("test plot now xd")
plt.xlabel("distance (m^2)")
plt.ylabel("1/Fg")
plt.show()
#print(stats.linregress(a, b))
#print(stats.linregress(x, y))