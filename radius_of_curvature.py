#
# TITLE: SymPy
# AUTHOR: Hyunseung Yoo
# PURPOSE:
# REVISION:
# REFERENCE: https://docs.sympy.org/latest/modules/plotting.html
#
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

print(x_pos)
print(y_pos)

#
dx_dtheta = x_pos.diff(theta)
dy_dtheta = y_pos.diff(theta)
d2x_dtheta2 = x_pos.diff(theta, 2)
d2y_dtheta2 = y_pos.diff(theta, 2)

print(dx_dtheta)
print(d2x_dtheta2)

#
R  = (dy_dtheta**2 + dx_dtheta**2)**1.5
R /=  ((dx_dtheta*d2y_dtheta2 - dy_dtheta*d2x_dtheta2)**2)**0.5

vals = {}
vals[r_major] = 5.0
vals[r_minor] = 4.0

R_try = R.subs(vals).simplify()

print(R)
print(R_try)

# plot parametric
vals = {}
vals[r_major] = 5.0
vals[r_minor] = 4.0

plot_x = x_pos.subs(vals).simplify()
plot_y = y_pos.subs(vals).simplify()
plot_R = R_try = R.subs(vals).simplify()

plot_xy = (plot_x, plot_y)
plot_thetaR = (theta, plot_R)

sp.plot_parametric(plot_thetaR, (theta, 0.0, 2*sp.pi))

