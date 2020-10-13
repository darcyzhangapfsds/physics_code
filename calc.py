'''
import numpy
import math
'''

def p(mass, velocity):
    mass = float(mass)
    velocity = float(velocity)
    return mass*velocity

def p2(Force, time):
    Force = float(Force)
    time = float(time)
    return Force*time

def a(mass, Force):
    mass = float(mass)
    Force = float(Force)
    return Force/mass

a = (0.2927*0.734)+(0.3437*-0.717)
b = (0.2927*-0.390)+(0.3437*0.489)
print(((abs(a-b))/(((a+b)/2)))*100)