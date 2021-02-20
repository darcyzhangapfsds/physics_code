import matplotlib.pyplot as plt
from statistics import mean
import math 
from scipy import stats
import numpy as np

points = [
    [2.00, 2],
    [3.00, 3],
    [4.00, 4],
    [5.00, 5],
    [6.00, 6]
]



maxx = [
    (points[len(points)-1][0])+0.1,
    (points[0][0])-0.1
]
maxy = [
    points[len(points)-1][1]+0.1,
    points[0][1]-0.1
]
minx = [
    points[len(points)-1][0]-0.1, 
    points[0][0]+0.1
]
miny = [
    points[len(points)-1][1]-0.1,
    points[0][1]+0.1
]

x, y = [], []
for i in range(len(points)):
    x.append(points[i][0])
    y.append(points[i][1])

xa = np.arange(-5,10,0.025)

def f(x, m, b):
    return m*x+b

m, b, xd, xd2, xd3  = stats.linregress(x, y)
mmax, bmax, xdmax, xd2max, xd3max = stats.linregress(maxx, maxy)
mmin, bmin, xdmin, xd2min, xd3min = stats.linregress(minx, miny)

plt.style.use('seaborn-whitegrid')
#plt.plot(xa, f(xa, m, b), c='black', label='y = ' + str(m) + 'x + ' + str(b))
#plt.plot(xa, f(xa, 1.05, -0.2), c ='cornflowerblue', label='max slope, y = ' + str(mmin+0.05) + 'x' + str(bmin-0.2))
#plt.plot(xa, f(xa, 0.95, 0.2), c = 'orange', label='min slope, y = ' + str(mmax-0.05) + 'x+' + str(bmax+0.2))
#plt.plot(xa, f(xa, m, b), c = 'green', label='slope, y = ' + str(m) + 'x')
plt.errorbar(x, y, xerr=0.1, yerr=0.1, ecolor='red', elinewidth=1, capsize=3, fmt='none')
plt.scatter(x, y, s=100, facecolors='none', edgecolors='cornflowerblue', linewidths=1.75)
plt.xlabel('Voltage, ΔV (V ± 0.1V)')
plt.xlim(1.5,6.5)
plt.ylim(1.5,6.5)
plt.ylabel('Current, I (A•10' + r'$^-3$' + ' ± 0.1A•10' + r'$^-3$' + ')')
plt.legend(loc='upper left', fontsize='large', frameon=True)
plt.title('Figure 5, plot of different voltages and the corresponding current measurements with data from table 5')
plt.show()          
