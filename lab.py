#import tensorflow as tf
#from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
#import pandas as import pd
import math 
from statistics import mean
from scipy import stats

points = []

for i in range(26): # 26 for rest
    points.append([i+11, 0])
 

points[0][1] = 160
points[1][1] = 140
points[2][1] = 124
points[3][1] = 114
points[4][1] = 109
points[5][1] = 104
points[6][1] = 100
points[7][1] = 101
points[8][1] = 200
points[9][1] = 174
points[10][1] = 159
points[11][1] = 148
points[12][1] = 144
points[13][1] = 130
points[14][1] = 129
points[15][1] = 124
points[16][1] = 118
points[17][1] = 117
points[18][1] = 122
points[19][1] = 120
points[20][1] = 123
points[21][1] = 120
points[22][1] = 120
points[23][1] = 118
points[24][1] = 117
points[25][1] = 116
'''
points[0][1] = 496
points[1][1] = 738
points[2][1] = 578
points[3][1] = 787
points[4][1] = 1012
points[5][1] = 1000
points[6][1] = 1251
points[7][1] = 1520 # Ar
points[8][1] = 419
points[9][1] = 590
points[10][1] = 633
points[11][1] = 659
points[12][1] = 651
points[13][1] = 653
points[14][1] = 717
points[15][1] = 762
points[16][1] = 760
points[17][1] = 737
points[18][1] = 745
points[19][1] = 906
points[20][1] = 579
points[21][1] = 762
points[22][1] = 944
points[23][1] = 941
points[24][1] = 1140
points[25][1] = 1320 # Kr

points[0][1] = 0.9
points[1][1] = 1.3
points[2][1] = 1.6
points[3][1] = 1.9
points[4][1] = 2.2
points[5][1] = 2.6
points[6][1] = 3.2
points[8][1] = 0.8
points[9][1] = 1.0
points[10][1] = 1.4
points[11][1] = 1.5
points[12][1] = 1.6
points[13][1] = 1.7
points[14][1] = 1.6
points[15][1] = 1.8
points[16][1] = 1.9
points[17][1] = 1.9
points[18][1] = 1.9
points[19][1] = 1.6
points[20][1] = 1.8
points[21][1] = 2.0
points[22][1] = 2.2
points[23][1] = 2.6
points[24][1] = 3.0
'''

# DARCY PLS FIX THIS SOMETIME WTF
x, y = [], []
for i in range(len(points)):
    x.append(points[i][0])
    y.append(points[i][1])

x0 = 7
x1 = 24

a = [18, 19]
a1 = [17, 19]
b = [101, 200]
b1 = [3.2, 0.8]

'''
plt.style.use('seaborn-whitegrid')
plt.scatter(x[:x0], y[:x0], c = 'orange', marker = 'D')
plt.scatter(x[x0+1:], y[x0+1:], c = 'cornflowerblue', marker = 'D')
plt.plot(x[:x0], y[:x0], c = 'orange')
plt.plot(a1, b1, '--', c = 'gray')
plt.plot(x[x0+1:], y[x0+1:], c = 'cornflowerblue')
plt.title("Plot of atomic number vs electronegativity for periods 3 and 4 excluding Ar and Kr")
plt.xlabel("Atomic number, Z")
plt.ylabel("Electronegativity (Pauling)")
plt.show()
plt.plot()
'''
#print(stats.linregress(a, b))



plt.style.use('seaborn-whitegrid')
plt.scatter(x[:x0+1], y[:x0+1], c = 'orange', marker = 'D')
plt.scatter(x[x0+1:], y[x0+1:], c = 'cornflowerblue', marker = 'D')
plt.plot(x[:x0+1], y[:x0+1], c = 'orange')
plt.plot(a, b, '--', c = 'gray')
plt.plot(x[x0+1:], y[x0+1:], c = 'cornflowerblue')
plt.title("Plot of atomic number vs atomic radius for periods 3 and 4")
plt.xlabel("Atomic number, Z")
plt.ylabel("Atomic radius, r (pm)")
plt.show()
