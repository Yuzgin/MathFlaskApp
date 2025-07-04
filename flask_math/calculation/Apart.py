from sympy import Symbol, apart
from flask import flash
from flask_math.calculation.common.STR import LATEX


def Apart(formula):
    try:
        x = Symbol('x')
        anser = apart(formula)
        anser = LATEX(formula) + "=" + LATEX(anser)
    except:
        anser = "Error"
        flash("Error: Please re-enter the input")
    return anser
