from flask import flash
from sympy.logic.boolalg import simplify_logic  # Not used in this function, consider removing if unnecessary

def base_conversion(before_conversion):
    try:
        base = str(before_conversion)[0:2]
        before_conversion = str(before_conversion)[2:]

        if base == "0b":
            bin_value = before_conversion
            oct_value = format(int(bin_value, 2), "o")
            dec_value = int(bin_value, 2)
            hex_value = format(int(bin_value, 2), "x")
        elif base == "0o":
            oct_value = before_conversion
            bin_value = format(int(oct_value, 8), "b")
            dec_value = int(oct_value, 8)
            hex_value = format(int(oct_value, 8), "x")
        elif base == "0d":
            dec_value = int(before_conversion)
            bin_value = format(dec_value, 'b')
            oct_value = format(dec_value, 'o')
            hex_value = format(dec_value, 'x')
        elif base == "0x":
            hex_value = before_conversion
            bin_value = format(int(hex_value, 16), "b")
            oct_value = format(int(hex_value, 16), "o")
            dec_value = int(hex_value, 16)

        anser = [
            "Binary: " + str(bin_value),
            "Octal: " + str(oct_value),
            "Decimal: " + str(dec_value),
            "Hexadecimal: " + str(hex_value)
        ]
    except:
        anser = ["Error", "Error", "Error", "Error"]
        flash("Error: Please re-enter the input")
    return anser
