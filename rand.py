import numpy as np
import math

x = [
    7.6,
    11.4,
    14.5,
    18.0,
    21.5,
    7.5,
    11.5,
    14.6,
    17.9,
    21.4,
    7.5,
    11.1,
    14.5,
    17.8,
    21.6,
    7.5,
    11.2,
    14.4,
    17.8,
    21.4,
    7.4,
    11.1,
    14.9,
    17.9,
    21.5
]

z = []

for i in range(len(x)):
    z.append(x[i]-0.5)

for i in range(len(z)):
    a = np.sin(np.deg2rad(z[i]))
    print(round(a, 3))

