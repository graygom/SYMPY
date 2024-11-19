#
# TITLE: 
# AUTHOR: Hyunseung Yoo 
# PURPOSE: symbolic computation
# REVISION:
# REFERENCE: symbolic computation with python and sympy 4th ed. (2023)
#
# chapter 11 derivatives
# chapter 12 integrals
#
#
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
    print('')

    # diff() function, multiple derivatives
    
    x, y = sp.symbols('x, y')
    g = 3*(x**5)*(y**2) + 5*x + 2*y + 6*(y**3)*x

    d3g_dxdy2_1 = sp.diff(g, x, y, y)
    d3g_dxdy2_2 = sp.diff(g, x, y, 2)

    print('(11.3) g = ', g)
    print('(11.3) d3g/dydx2 = ', d3g_dxdy2_1)
    print('(11.3) d3g/dydx2 = ', d3g_dxdy2_2)
    print('')

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
    print('')

    # diff() method

    x, y = sp.symbols('x, y')
    g = 3*(x**5)*(y**2) + 5*x + 2*y + 6*(y**3)*x

    eval_der_2 = g.diff(x, 2, y)
    uneval_der_2 = g.diff(x, 2, y, evaluate=False)      # still unevaluated

    print('(11.5) d3g/dx2dy = ', eval_der_2)
    print('(11.6) g3g/dx2dy = ', uneval_der_2)
    print('')

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
    print('')

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
    print('')



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

    # equation must be written in the form [left-hand side] - [right-hand side]
    eq_lhs = x**2 + y**2
    eq_rhs = 1
    eq = eq_lhs - eq_rhs

    eq_ider = sp.idiff(eq, y, x)

    print('(1.11) eq = ', eq)
    print('(11.11) dy/dx = ', eq_ider)
    print('')

    # two independent variables

    eq_lhs = x**2 + y + z
    eq_rhs = 1.0
    eq = eq_lhs - eq_rhs

    eq_ider = sp.idiff(eq, [y, z], x, 2)
    eq_ider_2 = eq_ider.doit()
    eq_ider_3 = eq_ider.simplify()
    
    print('(1.12) eq = ', eq)
    print('(1.12) ', eq_ider)
    print('(1.13) ', eq_ider_2)
    print('(1.13) ', eq_ider_3)
    print('')

    # if you are interested to manipulate the result,
    # then it is recommanded to create an expression containing applied undefined functions
    # and call the diff() method

    y = sp.Function('y')(x)
    z = sp.Function('z')(x)

    eq_lhs = x**2 + y + z
    eq_rhs = 1.0
    eq = eq_lhs - eq_rhs

    eq_ider = eq.diff(x, 2)

    print('(1.14) ', eq_ider)
    print('')



#----------------------------------------------------
# 11.3 advanced topic > evaluation of derivatives
#
# implicit function = at least one of the variables is a function of the other
#
    
if True:

    #

    x = sp.symbols('x')
    expr = x**2 + x * sp.sin(x)
    expr_diff = expr.diff(x)

    print('(11.15) ', expr)
    print('(11.15) ', expr_diff)



#----------------------------------------------------
# 12.1 the integrate() function
#
# used to compute both indefinite and definite integra;s
#
# parameters
# -. the expression to integrate
# -. the integration variables
#    > symbol ~ computing indefinite integral
#    > tuple (symbol, a) ~ computing indefinite integral & substituting a to symbol in the result
#    > tuple (symbol, a, b) ~ computing definite integral in the interval [a, b] 
# -. various keyword arguments
#    > conds ~ 'piecewise' (default), 'separate', 'none'
#    > specifying the algorithm ~ meijerg, risch, manual
#
# using a number of algorithms to compute integrals
# -. several heuristic algorithms ~ fastest
#    > rational functions, trigonometric functions,
#      functions with 'DiracDelta' objects or functions containing 'SingularityFunction'
# -. Risch algorithm ~ a general method for calculating antiderivatives of elementary functions
# -. for non-elementary definite integrals, sympy using so-called Meijer G-functions 
# -. Sympy Gamma ~ like calculus, seeing how to compute the integral by hand
#
#

    
if True:

    # indefinite integral

    x = sp.symbols('x', real=True)
    C = sp.symbols('C', real=True)

    r1 = sp.integrate(x**2, x)          # no constant of integration
    r2 = r1 + C

    print('(12.1) ', r1)
    print('(12.1) ', r2)
    print('')

    # indefinite multiple integral

    x, y = sp.symbols('x, y', real=True)

    expr = 42*y**2 - 12*x

    int_expr = sp.integrate(expr, x, y)

    print('(12.2) ', expr)
    print('(12.3) ', int_expr)
    print('')

    # definite multiple integral over a specified domain

    x, y = sp.symbols('x, y', real=True)

    expr = 42*y**2 - 12*x
    int_range_1 = (y, (x-2)**2, 6)
    int_range_2 = (x, 0, 4)
    int_expr = sp.integrate(expr, (y, (x-2)**2, 6), (x, 0, 4))

    print('(12.4) ', expr)
    print('(12.4) ', int_range_1)
    print('(12.4) ', int_range_2)
    print('(12,5) ', int_expr)
    print('')

    # integrate undefined functions
    # -> the result is an object of type Integral

    x = sp.symbols('x')
    f = sp.Function('f')

    int_f = sp.integrate(f(x), x)
    int_f_2 = int_f.subs(f(x), x**2)        # substitution
    int_f_3 = int_f_2.doit()

    print('(12.6) ', int_f)
    print('(12.6) ', int_f_2)
    print('(12.7) ', int_f_3)
    print('')

    # integrate() method

    x, y = sp.symbols('x, y')

    expr = 42*y**2 - 12*x

    int_expr = expr.integrate(x, y)

    print('(12.8) ', expr)
    print('(12.8) ', int_expr)
    print('')

    # instantiate the Integral class and eventually call the doit() method

    # options in case of returning an unevaluated integral
    #
    # -. changing the method of integration: meijerg, risch, manual
    # -. manipulating the expression before performing the integration
    # -. performing a change of variables (or u-substitution) using the transform() method in Integral class
    #

    # integration capabilities of different CAS over the same dataset of integrals
    #
    # --- Rubi (Rule-Based Integrator) ---
    #  1. it applies an extensitve collection of integration rules to file the optimal
    #     antiderivative of large classes of mathematical expressions.
    #  2. the rules are organized as a decision tree on the form of the integrand
    #  3. the integrator is built on top of Mathematica,
    #     but the collection of rules is open source,
    #     meaning anyone could build a Rubi for a given CAS.
    #
    # it is clear that integration is one of the weakest points of Sympy. 
    # one of the reasons is that the risch algorithm implemented on Sympy only supports a small
    # subset of the full algorithm
    #
    
    












    

    
