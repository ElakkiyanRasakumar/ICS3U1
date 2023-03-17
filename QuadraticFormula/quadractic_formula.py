from math import *
import numpy
import matplotlib.pyplot as plt


def main():
    print("""
    Welcome!
    This program will help you find the roots of a quadratic in standard form. 
    ax²+bx+c = 0
    By inputting an "a", "b", "c" value 
    This program will calculate the roots
    """)

    quadratic_formula(int_or_float_check_and_returning_that_number("a"),
                      int_or_float_check_and_returning_that_number("b"),
                      int_or_float_check_and_returning_that_number("c"))


def int_or_float_check_and_returning_that_number(constant):
    while True:
        try:
            value = input(f"What is your {constant} value? ")
            if value != "0":
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
            elif constant != "b" and constant != "c":
                print(
                    f"Please enter a\033[1;31m valid\033[0m number for your \033[1;32m{constant}\033[0m value")
                # Through ASCI, I get colored text. You live you learn
                continue
            else:
                return 0
        except ValueError or TypeError:
            print(f"Please enter a\033[1;31m valid\033[0m number for your \033[1;32m{constant}\033[0m value")
            continue


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
    if c != 0:
        if c < 0:
            print(f"{c} = 0")
        else:
            print(f"+{c} = 0")
    else:
        print(f" = 0")

    d = (b ** 2) - (4 * a * c)
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.grid()
    if d < 0:
        x_midpoint = -b / 2 * a
        if x_midpoint > 0:
            x = numpy.linspace(-x_midpoint, x_midpoint + (2 * x_midpoint))
        elif x_midpoint < 0:
            x = numpy.linspace(x_midpoint - (abs(x_midpoint) - x_midpoint), abs(x_midpoint))
        else:
            x = numpy.linspace(-a, a)
        y = a * x ** 2 + b * x + c
        plt.plot(x, y)
        plt.show()
        return print("There are no specific roots")
    elif d == 0:
        zero = (-b + sqrt(d)) / (2 * a)
        if zero < 0:
            x = numpy.linspace(zero - (abs(zero) - zero), abs(zero))
        elif zero > 0:
            x = numpy.linspace(-zero, zero + (2 * zero))
        else:
            x = numpy.linspace(-a, a)
        plt.plot(x, y)
        plt.show()
        return print(f"The quadratic equation you have specified has one root, at x = {zero}")
    else:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        x_values = [x1, x2]
        middle_to_zero = (abs(x1) + abs(x2)) / 2
        lowest_x_value = (min(x_values) - middle_to_zero)
        highest_x_value = (max(x_values) + middle_to_zero)
        x = numpy.linspace(lowest_x_value, highest_x_value)
        y = a * x ** 2 + b * x + c
        plt.plot(x, y)
        plt.show()
        return print(f"Your two roots are x₁ = {x1} and x₂ = {x2}")


main()
