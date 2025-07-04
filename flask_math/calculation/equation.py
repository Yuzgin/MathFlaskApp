from sympy import Symbol, solve
from flask import flash
from flask_math.calculation.common.STR import LATEX


def equation(formula, type):
    try:
        x = Symbol('x')
        solutions = solve(formula, dict=True)
        result = ["Equation: " + LATEX(formula) + " = 0", ""]

        if type == "analytical":
            for sol in solutions:
                for var, value in sol.items():
                    answer = LATEX(var) + " = " + LATEX(value)
                    result.append(answer)

        elif type == "numerical":
            for sol in solutions:
                for var, value in sol.items():
                    answer = LATEX(var) + " = " + LATEX(value.evalf())
                    result.append(answer)
    except:
        result = ["Error"]
        flash("Error: Please re-enter the input")
    
    return result
