# to see if any give three numbers can make a triangle
def is_a_triangle(a, b, c):
    # will return direct comparison value to simplify the code
    return a + b > c and b + c > a and c + a > b

# if any side **2 == other two sides's **2 additions to determine a right triangle


def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    elif c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    elif a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    else:
        return b ** 2 == a ** 2 + c ** 2


# use heron's formula to calculate the any triangle's area
def heron(a, b, c):
    if is_a_triangle(a, b, c):
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5
    else:
        print("sorry this is not a valid triangle, please try something else")
        return


# use special formula to calculate the right triangle's area == shortest side x second shortest / 2
def right_triangle_area(a, b, c):
    if is_a_right_triangle(a, b, c):
        if a > c and a > b:
            return b * c / 2
        elif b > a and b > c:
            return a * c / 2
        else:
            return a * b / 2
    else:
        print("sorry your triangle is not a right triangle, please use heron formula to calculate the area")
        return


print(heron(1, 1, 2))
print(right_triangle_area(3, 5, 4))
print(heron(3, 4, 5))
