#import tensorflow as tf
#from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
#import pandas as import pd
import math 
from statistics import mean


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


points = [
    [2.0, (1.67*(10**-5))],
    [4.0, (4.17*(10**-6))],
    [6.0, (1.85*(10**-6))],
    [8.0, (1.04*(10**-6))],
    [10.0, (6.67*(10**-7))]
]

points2 = [
    [2.0, 1/(1.67*(10**-5))],
    [4.0, 1/(4.17*(10**-6))],
    [6.0, 1/(1.85*(10**-6))],
    [8.0, 1/(1.04*(10**-6))],
    [10.0, 1/(6.67*(10**-7))]
]

points3 =[
    [2.0**2, 1/(1.67*(10**-5))],
    [4.0**2, 1/(4.17*(10**-6))],
    [6.0**2, 1/(1.85*(10**-6))],
    [8.0**2, 1/(1.04*(10**-6))],
    [10.0**2, 1/(6.67*(10**-7))]
]



x, y = [], []
for i in range(len(points)):
    x.append(points2[i][0])
    y.append(points2[i][1])

a, b = [], []
for i in range(len(points)):
    a.append(points3[i][0])
    b.append(points3[i][1])

xs = np.array(a, dtype=np.float64)
ys = np.array(b, dtype=np.float64)

def lobf(x,y):
    m = (((mean(x)*mean(y))-mean(x*y))/((mean(x)*mean(x))-mean(x*x)))
    b = mean(y)-(m*mean(x))
    return m, b

plt.style.use('seaborn-whitegrid')
plt.scatter(x, y, c = 'red')
plt.scatter(a, b, c = 'green')
#plt.plot(a, b, regression)*****
plt.title("test plot now xd")
plt.xlabel("distance in m")
plt.ylabel("fg except its not rlly a force xd")
plt.show()