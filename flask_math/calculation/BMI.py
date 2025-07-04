from flask import flash

def BMI(height, weight):
    try:
        height = float(height)
        weight = float(weight)
        bmi_value = weight * 10000 / (height * height)  # height in cm

        if bmi_value < 18.5:
            category = "You are underweight"
        elif 18.5 <= bmi_value < 25:
            category = "You are of normal weight"
        else:  # bmi_value >= 25
            category = "You are overweight"

        bmi_result = "BMI: " + str(round(bmi_value, 2))
        category_result = "Category: " + category
        result = [bmi_result, category_result]
    except:
        result = ["Error", ""]
        flash("Error: Please re-enter the input")
    return result
