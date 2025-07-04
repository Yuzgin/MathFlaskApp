from sympy import Symbol, Function, sympify, dsolve
from flask import flash
from flask_math.calculation.common.STR import LATEX

def diff_equation(formula):
    try:
        x = Symbol('x')
        y = Function('y')
        formula = sympify(formula)
        A = dsolve(formula)

        Anser = [LATEX(formula) + " = 0"]
        if isinstance(A, list):
            for sol in A:
                Anser.append(LATEX(sol))
        else:
            Anser.append(LATEX(A))
    except:
        Anser = ["Error"]
        flash("Error: Please re-enter the input")
    return Anser
