from flask import flash

def Euclidean_Algorithm(number_x, number_y):
    try:
        x, y = int(number_x), int(number_y)

        r = x % y
        while r > 0:
            x, y = y, r
            r = x % y
        else:
            gcd = y
        anser = f"The greatest common divisor of {number_x} and {number_y} is {gcd}"
    except:
        anser = "Error"
        flash("Error: Please re-enter the input")
    return anser
