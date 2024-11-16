
# TITLE: 
# AUTHOR: Hyunseung Yoo 
# PURPOSE: symbolic computation
# REVISION:
# REFERENCE: symbolic computation with python and sympy 4th ed. (2023)
#
#


import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


#----------------------------------------------------
# 11.1 explicit differentiation
#
# explicit function = a function having the dependent variable expressed directly
#                     in terms of the independent variables
#

if True:

    # diff() function
    
    x = sp.symbols('x')
    f = x**3 + 2*x**2 + x + 1
    
    df_dx = sp.diff(f, x)
    d3f_dx3_1 = sp.diff(f, x, x, x)
    d3f_dx3_2 = sp.diff(f, x, 3)
    
    print('(11.1) f = ', f)
    print('(11.1) df/dx = ', df_dx)
    print('(11.2) d3f/dx3 = ', d3f_dx3_1)
    print('(11.2) d3f/dx3 = ', d3f_dx3_2)

    # diff() function, multiple derivatives
    
    x, y = sp.symbols('x, y')
    g = 3*(x**5)*(y**2) + 5*x + 2*y + 6*(y**3)*x

    d3g_dxdy2_1 = sp.diff(g, x, y, y)
    d3g_dxdy2_2 = sp.diff(g, x, y, 2)

    print('(11.3) g = ', g)
    print('(11.3) d3g/dydx2 = ', d3g_dxdy2_1)
    print('(11.3) d3g/dydx2 = ', d3g_dxdy2_2)

    # Derivative class (unevaluated derivative)
    # useful for delaying the evaluation,
    #        for creating terms in differential equations and
    #        for printing purpose

    x, y = sp.symbols('x, y')
    g = 3*(x**5)*(y**2) + 5*x + 2*y + 6*(y**3)*x
    
    uneval_der = sp.Derivative(g, x, y, 2)
    eval_der = uneval_der.doit()                # doit() method

    print('(11.4) d3g/dxdy2 = ', uneval_der)
    print('(11.4) d3g/dxdy2 = ', eval_der)

    # diff() method

    x, y = sp.symbols('x, y')
    g = 3*(x**5)*(y**2) + 5*x + 2*y + 6*(y**3)*x

    eval_der_2 = g.diff(x, 2, y)
    uneval_der_2 = g.diff(x, 2, y, evaluate=False)      # still unevaluated

    print('(11.5) d3g/dx2dy = ', eval_der_2)
    print('(11.6) g3g/dx2dy = ', uneval_der_2)

    # undefined function

    x, y = sp.symbols('x, y')
    f = sp.Function('f')(x, y)

    f_der = f.diff(x, y, 2)
    expr = 3 * x**5 * y**2 + 5*x + 2*y + 6*y**3*x
    expr_der = f_der.subs(f, expr)                  # still unevaluated
    expr_der2 = expr_der.doit()                     # doit() method

    print('(11.7) d3f/dxdy2 = ', f_der)
    print('(11.8) d3expr/dxdy2 = ', expr_der)
    print('(11.8) d3expr/dxdy2 = ', expr_der2)

    # arguments of an object of type Derivative

    x, y = sp.symbols('x, y')
    f = sp.Function('f')(x, y)

    f_der = f.diff(x, y, 2)
    expr = 3 * x**5 * y**2 + 5*x + 2*y + 6*y**3*x
    expr_der = f_der.subs(f, expr)

    print('(11.9) ', expr_der.args)
    print('(11.9) ', expr_der.args[0])
    print('(11.9) ', expr_der.args[1][0], expr_der.args[1][1])
    print('(11.9) ', expr_der.args[2][0], expr_der.args[2][1])



#----------------------------------------------------
# 11.2 implicit differentiation
#
# implicit function = at least one of the variables is a function of the other
#
    
if True:

    # idiff() function
    # - 1st argument = an expression representing the implicit function
    # - 2nd argument = the dependent variable or a list of dependent variables
    # - 3rd argument = independent variable

    x, y, z = sp.symbols('x, y, z')
    eq_lhs = x**2 + y**2
    eq_rhs = 1

    eq = eq_lhs - eq_rhs

    

    
