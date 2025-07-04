from flask_math.calculation.common.STR import LATEX
from flask import flash


def latex(formula):
    try:
        anser = LATEX(formula)
        return anser
    except:
        flash("Error: Please re-enter the input")
        return "Error"
