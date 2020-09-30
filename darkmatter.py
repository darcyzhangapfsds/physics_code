import matplotlib.pyplot as plt
from statistics import mean
import math 
from scipy import stats

points = [
    [1, 2.47],
    [2, 2.28],
    [3, 2.15],
    [4, 1.86]
]

x, y = [], []
for i in range(len(points)):
    x.append(points[i][0])
    y.append(points[i][1])

 
for i in range(len(points)):
    print(((2*math.pi*(0.34)))/(y[i]/5))

plt.style.use('seaborn-whitegrid')
plt.scatter(x, y)
plt.plot(x, y)
plt.xlabel('number of washers')
plt.ylabel('time for 5 periods')
plt.show()
