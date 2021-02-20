import sys 
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.patches import Circle 
import matplotlib.gridspec as gridspec 
  
# Function to determine electric field 
def E(q, r0, x, y): 
    den = np.hypot(x-r0[0], y-r0[1])**3
    return q * (x - r0[0]) / den, q * (y - r0[1]) / den 


  
# Grid of x, y points 
nx, ny = 128, 128
x = np.linspace(-2, 2, nx) 
y = np.linspace(-2, 2, ny) 
X, Y = np.meshgrid(x, y) 
  
# Create a multipole with nq charges of 
# alternating sign, equally spaced 
# on the unit circle. 
opp = input('opposite charges, y/n? ')
# Increase the power with increase in charge 
nq = 2**(int(input('order of bodies *dont make this greater than 3 or ur pc is fried darcy*= ')))
dens = int(input('density, also dont make this greater than 3: '))
charges = [] 
for i in range(nq): 
    if opp == 'n':
        q = i % 2 * 2 + 500
        charges.append((q, (np.cos(2 * np.pi * i / nq), 
                            np.sin(2 * np.pi * i / nq)))) 
    elif opp == 'y':
        q = i % 2 * 2 - 1
        charges.append((q, (np.cos(2 * np.pi * i / nq), 
                            np.sin(2 * np.pi * i / nq)))) 
  
# Electric field vector, E =(Ex, Ey) 
# as separate components 
Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx)) 
  
for charge in charges: 
    ex, ey = E(*charge, x = X, y = Y) 
    Ex += ex 
    Ey += ey 


fig = plt.figure(figsize =(18, 8)) 
ax = fig.add_subplot(111) 
color = 2 * np.log(np.hypot(Ex, Ey)) 
strm = ax.streamplot(x, y, Ex, Ey, color = color, 
              linewidth = 1.25, cmap = 'ocean', 
              density = dens, arrowstyle ='fancy',  
              arrowsize = 1.35)
# Plotting the streamlines with  
# proper color and arrow 
fig.colorbar(strm.lines, label='electric force in N')

# Add filled circles for the charges 
# themselves 
charge_colors = {True: '#AA0000',  
                 False: '#0000AA'} 
  
for q, pos in charges: 
    ax.add_artist(Circle(pos, 0.05,  
                         color = charge_colors[q>0])) 

  
ax.set_xlabel('X-axis') 
ax.set_ylabel('X-axis') 
ax.set_xlim(-2, 2) 
ax.set_ylim(-2, 2) 
ax.set_aspect('equal') 
plt.title(r'darcys epic vector field visualizer')
plt.ylabel('y axis')
plt.show() 