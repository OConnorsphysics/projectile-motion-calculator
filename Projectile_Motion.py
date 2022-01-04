# A simple projectile motion calculator.

import math
import numpy as np
print("This program will calculate the distance that an idealized projectile will travel when fired from a cannon at (0,0). Please enter the following,")
V_i = float(input("What is the initial velocity of the cannon ball (m/s)? "))
angle = float(input("What is the angle of the cannon of the ground (deg.)? "))
print("""The acceleration due to gravity on earth is -9.81m/s^2.
The acceleration due to gravity on the moon is -1.6m/s^2.
The acceleration due to gravity on mars is -3.7m/s^2.""")
accel = float(input("What is the acceleration do to gravity in our scenario? "))
mass = float(input("What is the mass of our projectile (kg)? "))

angle = angle *np.pi/180
V_ix = V_i *math.cos(angle)
V_iy = V_i *math.sin(angle)

time = (-2* V_iy)/accel
x = time *V_ix
print(f" The initial velocity in x is {V_ix}m/s, and the initial velocity in y is {V_iy}m/s.")
print(f"The projectile travelled {round(x,1)} meters in {round(time,1)} seconds, before it hit the ground.")