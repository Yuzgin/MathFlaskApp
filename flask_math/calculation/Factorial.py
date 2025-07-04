import math
from flask import flash
from flask_math.calculation.common.STR import LATEX


def Factorial(formula):
    try:
        A = math.factorial(int(formula))
        anser = LATEX(formula)+"! = "+LATEX(A)
    except:
        anser = "Error"
        flash("Error: Please re-enter the input")
    return anser
