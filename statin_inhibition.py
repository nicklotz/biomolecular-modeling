# Nicholas Lotz
# Drug inhibition model driver
# Last edit: December 25, 2015
# Description of last edit: begin model

# Import numerical and plotting libraries
import numpy as np
import matplotlib.pyplot as pl
from scipy.integrate import odeint
# Define terms
S = []       # Cholesterol Concentration
V0 = []         # Rate of reaction
I = 0.3         # Inhibitor (statin) concentration
E = 10          # Enzyme concentration
Km = 0.5        # MM constant
Ki = 0.2
Km_app = Km*(1+I/Ki)
Vmax = 100      # Maximum reaction velocity

# Inhibitive MM Equation
n = 1
Rate = (Vmax*n)/(Km_app+n)
while n < (20):
    S.append(n)
    V0.append(Rate) # This is the MM equation for competitive inhibition
    n = n+0.01
  
# Plot Cholesterol synthesis vs cholesterol concentration
#pl.plot(S,V0)

# Integrate to find total cholesterol synthesis

# Set a constant substrate concentration
n = 5

# Now redefine Rate as function for use in odeint
def Rate(P,t):
    f = (Vmax/n)/(Km_app+n)
    return f

# Initial Condition
P0 = 0

# Time Vector
# First, create time vector
time = [0]
for n in range(1000):
    time.append(n)



# Integrate the rate law
P = odeint(Rate,P0,time)
pl.plot(time,P[:,0])
