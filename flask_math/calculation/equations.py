from sympy import solve
from flask import flash
from flask_math.calculation.common.STR import LATEX


def equations(formula, number):
    try:
        A = solve(formula)
        Anser = []

        if number == 1:
            for solution in A:
                for variable, value in solution.items():
                    anser = LATEX(variable) + " = " + LATEX(value)
                    Anser.append(anser)
        else:
            for variable, value in A.items():
                anser = LATEX(variable) + " = " + LATEX(value)
                Anser.append(anser)
    except:
        Anser = ["Error"]
        flash("Error: Please re-enter the input")
    return Anser
