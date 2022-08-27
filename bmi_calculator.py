# Body Mass Index (BMI).
# BMI equals weight in kilograms divided by height in meters squared

def ft_and_inch_to_m(ft, inch=0.0):
    return ft * 0.3048 + inch * 0.0254


def lb_to_kg(lb):
    return lb * 0.45359237


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None

    return weight / height ** 2


def weight_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Healthy Weight"
    elif 25.0 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obesity"


bmi = bmi(weight=lb_to_kg(176), height=ft_and_inch_to_m(5, 7))
print(weight_status(bmi))
