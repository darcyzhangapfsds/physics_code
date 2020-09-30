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

print((a(500, 30))*0.6)
