import matplotlib.pyplot as plt
from statistics import mean
import math 
from scipy import stats
import numpy as np

dx = [
    25.0,
    35.0,
    45.0,
    55.0,
    65.0
]

dy = [
    1.39,
    1.39,
    1.38,
    1.39,
    1.37
]

xerr = [
    0.07,
    0.07,
    0.09,
    0.07,
    0.055
]

def f(x, m, b):
    return m*x+b

xa = np.arange(0, 100, 0.025)

dm, db, dxd, dxd2, dxd3 = stats.linregress(dx, dy)
print(stats.linregress(dx, dy))


'''
plt.style.use('seaborn-whitegrid')
plt.plot(xa, f(xa, m, b), c='cornflowerblue', label='line best fit')
plt.scatter(x, y, s=300, facecolors='none', edgecolors='black', label='points', linewidths=1.5)
plt.xlabel('Resistor Length')
plt.ylabel('Anmeter Reading')
plt.xlim(8, 24)
plt.errorbar(x, y, xerr=0.05, yerr=.5, ecolor='red', elinewidth=1, capsize=3, fmt='none')
plt.legend(loc='best', fontsize='large', frameon=True)
plt.show()          
'''
plt.style.use('seaborn-whitegrid')
plt.plot(xa, f(xa, dm, db), c='cornflowerblue', label='line of best fit')
plt.plot(xa, f(xa, dm+0.002, db-0.08), c='orange', label='max slope')
plt.plot(xa, f(xa, dm-0.002, db+0.08), c='green', label='min slope')
plt.scatter(dx, dy, s=200, facecolors='none', edgecolors='red', label='data points', linewidths=0.75)
plt.xlabel('Temperature, T (Celsius)')
plt.ylabel('Relative Index of Refraction, n')
plt.xlim(20, 70)
plt.ylim(0, 3)
plt.errorbar(dx, dy, xerr=0.5, yerr=xerr, ecolor='red', elinewidth=1, capsize=3, fmt='none')
plt.legend(loc='best', fontsize='large', frameon=True)
plt.show()    
