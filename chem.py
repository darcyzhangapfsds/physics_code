import matplotlib.pyplot as plt
from statistics import mean
import math 
from scipy import stats
import numpy as np



dy = [
    -4.037068494,
    -2.468099531,
    -6.717562828,
    -7.35046479,
    -4.844265824,
    -4.82775358,
    -3.684620397,
    -5.322766047,
    -3.47537678,
    -5.406094959,
    -3.174714929,
    -4.462915138,
    -3.927699485,
    -2.768204124,
    -7.783224016,
    -3.363841595,
    -7.263525814,
    -3.637059705,
    -7.852295218,
    -6.171094986,
    -5.762177161,
    -4.189806246,
    -6.694388776,
    -7.134420622,
    -7.839415296
]

dx = [
    0.003025719,
    0.002836075,
    0.003299241,
    0.003376097,
    0.003096934,
    0.003095975,
    0.002918004,
    0.003096934,
    0.002911208,
    0.003096934,
    0.002839296,
    0.003004808,
    0.002840909,
    0.003004808,
    0.003380663,
    0.002920561,
    0.00330033,
    0.003019324,
    0.003195909,
    0.003194888,
    0.003192848,
    0.003002101,
    0.00330033,
    0.003299241,
    0.003380663
]

xerr = [
    0.000000915497310,
    0.000000804332068,
    0.000001088499233,
    0.000001139803252,
    0.000000959100042,
    0.000000958506264,
    0.000000851474784,
    0.000000959100042,
    0.000000847513290,
    0.000000959100042,
    0.000000806160095,
    0.000000902886927,
    0.000000807076446,
    0.000000902886927,
    0.000001142887968,
    0.000000852967508,
    0.000001089217833,
    0.000000911631543,
    0.000001021383585,
    0.000001020731048,
    0.000001019427848,
    0.000000901261324,
    0.000001089217833,
    0.000001088499233,
    0.000001142887968
]

yerr = [
    0.03562538381929,
    0.10458048862168,
    0.00406238680927,
    0.00236057883181,
    0.01907041108384,
    0.01932183454912,
    0.04625433589246,
    0.01298552341291,
    0.05378175146760,
    0.01213434853367,
    0.06636109801594,
    0.02572581933599,
    0.03866607092748,
    0.08688650734218,
    0.00162150500340,
    0.05819795147264,
    0.00254453429392,
    0.04788124941264,
    0.00152671558857,
    0.00644554634966,
    0.00905888750005,
    0.03173614789957,
    0.00414328520795,
    0.00284373554958,
    0.00154397005105
]



'''


def f(x, m, b):
    return m*x+b



dm, db, dxd, dxd2, dxd3 = stats.linregress(dx, dy)
print(stats.linregress(dx, dy))
'''
print(stats.linregress(dx, dy))

plt.style.use('seaborn-whitegrid')
#plt.plot(xa, f(xa, m, b), c='cornflowerblue', label='line best fit')
#plt.plot(dx, dy, c='cornflowerblue', label='line best fit')
plt.scatter(dx, 
    dy, 
    s=150, 
    facecolors='none', 
    edgecolors='black',  
    linewidths=1.5)
plt.errorbar(dx, dy, xerr=xerr, yerr=yerr, ecolor='red', elinewidth=1, capsize=3, fmt='none')
'''
plt.scatter(dx, 
    dt, 
    s=150, 
    facecolors='none', 
    edgecolors='black', 
    linewidths=1.5)
plt.scatter(dx, 
    dt,
    marker="+", 
    label='P points', 
    c='cornflowerblue'
)
'''
#plt.xlabel('Concentration of iodate ions, [$\mathregular{IO3_{3}}{^{-}}{_{(aq)}}$], (mol$\cdot$dm$\mathregular{^{-3}}$)',fontsize=20)
plt.xlabel('Inverse of temperature', fontsize=20)
plt.ylabel('Natural log of the rate constant',fontsize=20)
plt.title("Plot of the natural log of the reaction rate constant with respect to inverse temperature", fontsize = 25)
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