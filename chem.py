import matplotlib.pyplot as plt
from statistics import mean
import math 
from scipy import stats
import numpy as np

dx = [
    1.20*10**-2,
    1.20*10**-2,
    9.60*10**-3,
    9.60*10**-3,
    7.20*10**-3,
    7.20*10**-3,
    4.80*10**-3,
    4.80*10**-3,
    2.40*10**-3,
    2.40*10**-3
]

dy = [
    0.0319795330988,
    0.0325839035516,
    0.0279251605697,
    0.0322684737012,
    0.0112359550562,
    0.0109481059777,
    0.013764624914,
    0.0124486493215,
    0.00539898499082,
    0.00516049127877
]

#xa = np.arange(0, 100, 0.025)


xerr = [
    2.412*10**-4, 
    2.412*10**-4,
    2.16*10**-4,
    2.16*10**-4,
    1.9224*10**-4,
    1.9224*10**-4,
    1.68*10**-4,
    1.68*10**-4,
    1.44*10**-4,
    1.44*10**-4
]
'''
def f(x, m, b):
    return m*x+b



dm, db, dxd, dxd2, dxd3 = stats.linregress(dx, dy)
print(stats.linregress(dx, dy))
'''


plt.style.use('seaborn-whitegrid')
#plt.plot(xa, f(xa, m, b), c='cornflowerblue', label='line best fit')
#plt.plot(dx, dy, c='cornflowerblue', label='line best fit')
plt.scatter(dx, 
    dy, 
    s=150, 
    facecolors='none', 
    edgecolors='black', 
    label='points', 
    linewidths=1.5)
plt.xlabel('Concentration of iodate ions, [$\mathregular{IO3_{3}}{^{-}}{_{(aq)}}$], (mol$\cdot$dm$\mathregular{^{-3}}$)',fontsize=20)
plt.ylabel('Rate of redox reaction, r (t$\mathregular{^{-1}}$)',fontsize=20)
#plt.title("concentration of NO2", fontsize = 50 )
plt.errorbar(dx, dy, xerr=xerr, yerr=0, ecolor='red', elinewidth=1, capsize=3, fmt='none')
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
'''