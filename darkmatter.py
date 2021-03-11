import matplotlib.pyplot as plt
from statistics import mean
import math 
from scipy import stats
import numpy as np


nums = np.arange(-10,10,0.025)

def f(t,vel,height,angle):
    return (vel*np.sin(angle*(np.pi/180)))*t-(1/2)*(9.81*t)**2+height

plt.style.use('seaborn-whitegrid')
plt.plot(nums, f(nums,50,20,45), c='cornflowerblue', linewidth=2, label='v=50m/s')
plt.plot(nums, f(nums,10,20,45), c='orange', linewidth=2, label='v=10m/s')
plt.plot(nums, f(nums,20,20,45), c='green', linewidth=2, label='v=20m/s')
plt.plot(nums, f(nums,30,20,45), c='red', linewidth=2, label='v=30m/s')
plt.plot(nums, f(nums,40,20,45), c='purple', linewidth=2, label='v=40m/s')
plt.xlabel('Distance, d (meters)')
plt.ylabel('Height, h (meters)')
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlim(-0.1,1.5)
plt.ylim(-0.1,30)
plt.legend(loc='upper left', fontsize='large', frameon=True)
plt.show()          
