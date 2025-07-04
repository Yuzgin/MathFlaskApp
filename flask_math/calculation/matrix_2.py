from sympy import *
from flask import flash
from flask_math.calculation.common.MATRIX import MATRIX
from flask_math.calculation.common.STR import LATEX


def calculation(matrixA, matrixB, type, k, l):
    try:
        k, l = [int(k), int(l)]
        A, Ar, Ac = MATRIX(matrixA)
        B, Br, Bc = MATRIX(matrixB)

        if type == "A":
            anser = LATEX(A)
        elif type == "B":
            anser = LATEX(B)
        elif type == "kA+lB":
            anser = LATEX(k*A + l*B)
            type = str(k) + "A+" + str(l) + "B"
        elif type == "AB":
            anser = LATEX(A * B)
        elif type == "BA":
            anser = LATEX(B * A)
        elif type == "A・B(Dot Product)":
            anser = LATEX(B.dot(A))
        elif type == "A×B(Cross Product)":
            anser = LATEX(A.cross(B))
        elif type == "B×A(Cross Product)":
            anser = LATEX(B.cross(A))
        anser = str(type) + "=" + anser
    except:
        anser = "Error"
        flash("Error: Please re-enter the input")
    return anser
