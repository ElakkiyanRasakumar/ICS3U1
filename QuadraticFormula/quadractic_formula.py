from math import *

def main():
    print("""
    Welcome!
    This program will help you find the roots of a quadratic in standard form. 
    ax²+bx+c = 0
    By inputting an "a", "b", "c" value 
    This program will calculate the roots
    """)

    quadratic_formula(int_or_float_check("a"), int_or_float_check("b"), int_or_float_check("c"))


def int_or_float_check(constant):
    while True:
        try:
            value = input(f"What is your {constant} value? ")
            is_float = False
            if "." in value:
                for i in value[value.index(".") + 1:]:
                    if i != "0":
                        is_float = True
                        value = float(value)
                        break
                if not is_float:
                    value = round(float(value))
                    return int(value)
                if is_float:
                    return float(value)
            else:
                return int(value)

        except ValueError or TypeError:
            continue


"""
^^^ Theodore's Solution to this:
value = input(f"What is your {constant} value? ")
if not value.replace(".", "", 1).isdigit():
    continue
break
return float(value) if "." in value else int(value)
"""


def quadratic_formula(a, b, c):
    print("With the values given this is your standard form: ")

    if abs(a) == 1:
        if a == -1:
            print(f"-x{chr(178)}", end="")
        else:
            print(f"x{chr(178)}", end="")
    else:
        print(f"{a}x{chr(178)}", end="")
    if b != 0:
        if abs(b) == 1:
            if b == -1:
                print(f"-x", end="")
            else:
                print(f"+x", end="")
        else:
            if b > 0:
                print(f"+{b}x", end="")
            else:
                print(f"{b}x", end="")
        if c < 0:
            print(f"{c} = 0")
        else:
            print(f"+{c} = 0")
    else:
        print(f" = 0")

    d = (b ** 2) - (4 * a * c)
    if d < 0:
        return print("There are no specific roots")
    elif d == 0:
        return print(f"The quadratic equation you have specified has one root, at x = {(-b + sqrt(d)) / (2 * a)}")
    else:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return print(f"Your two roots are x₁ = {x1} and x₂ = {x2}")


main()
