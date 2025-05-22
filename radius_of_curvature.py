#
# TITLE: Radius of Curvature
# AUTHOR: Hyunseung Yoo
# PURPOSE:
# REVISION:
# REFERENCE: https://www.youtube.com/playlist?list=PLJtAfFg1nIX9dsWGnbgFt2dqvwXVRSVxm
#


import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


# symbols
theta = sp.symbols('theta')
r_major = sp.symbols('r_ma')
r_minor = sp.symbols('r_mi')

#
x_pos = r_major * sp.cos(theta)
y_pos = r_minor * sp.sin(theta)

#
dx_dtheta = x_pos.diff(theta)
dy_dtheta = y_pos.diff(theta)
d2x_dtheta2 = x_pos.diff(theta, 2)
d2y_dtheta2 = y_pos.diff(theta, 2)

#
R  = (dy_dtheta**2 + dx_dtheta**2)**1.5
R /=  ((dx_dtheta*d2y_dtheta2 - dy_dtheta*d2x_dtheta2)**2)**0.5

vals = {}
vals[r_major] = 5.0
vals[r_minor] = 5.0

R_try = R.subs(vals).simplify()

# debugging
print(x_pos)
print(y_pos)
print(dx_dtheta)
print(d2x_dtheta2)
print(R)
print(R_try)
