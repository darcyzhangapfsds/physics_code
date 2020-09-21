#import tensorflow as tf
#from tensorflow import keras
#import numpy as np
import matplotlib.pyplot as plt
#import pandas as import pd
import math 


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

#x, y = [], []
#for i in range(len(points)):
#    x.append(points[i][0])
#    y.append(points[i][1])



x, y = [], []
for i in range(len(points)):
    x.append(points[i][0])
    y.append(points[i][1])

plt.scatter(x, y)
plt.show()