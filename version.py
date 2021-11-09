from ast import walk
import matplotlib.pyplot as plt
from statistics import mean
import math 
from scipy import stats
import numpy as np

dx = np.array([
    6.206,
    9.448,
    14.936,
    21.46,
    24.574,
    29.85,
    35.50,
    41.23
])

dy = np.array([
    50-5,
    50-10,
    50-15,
    50-20,
    50-25,
    50-30,
    50-35,
    50-40
])

one = np.array([
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1
])



dt = np.log(dy)
dn = one/dy

plt.style.use('seaborn-whitegrid')
#plt.plot(xa, f(xa, m, b), c='cornflowerblue', label='line best fit')
#plt.plot(dx, dy, c='cornflowerblue', label='line best fit')
plt.scatter(dx, 
    dn, 
    s=150, 
    facecolors='none', 
    edgecolors='black',  
    linewidths=1.5)
plt.scatter(dx, 
    dn,
    marker="+", 
    label='points',
    c='red'
)
#plt.xlabel('Concentration of iodate ions, [$\mathregular{IO3_{3}}{^{-}}{_{(aq)}}$], (mol$\cdot$dm$\mathregular{^{-3}}$)',fontsize=20)
plt.xlabel('Time, t (s)', fontsize=20)
plt.ylabel('Inverse of volume, V$\mathregular{^{-1}}$ (mL$\mathregular{^{-1}}$)',fontsize=20)
plt.title('Graph of the inverse of volume of water with respect to time')
plt.errorbar(dx, dy, ecolor='red', elinewidth=1, capsize=3, fmt='none')
plt.legend(loc='best', fontsize='large', frameon=True)
plt.show()          
