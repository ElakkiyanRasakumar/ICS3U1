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

    discriminant = (b ** 2) - (4 * a * c)
    if discriminant < 0:
        x_midpoint = -b / 2 * a
        print("There are no specific roots")
        get_and_plot_graph_values(x_midpoint, a, b, c, None, None)
    elif discriminant == 0:
        zero = (-b + sqrt(discriminant)) / (2 * a)
        print(f"The quadratic equation you have specified has one root, at x = {zero}")
        get_and_plot_graph_values(zero, a, b, c, None, None)
    else:
        x1 = (-b + sqrt(discriminant)) / (2 * a)
        x2 = (-b - sqrt(discriminant)) / (2 * a)
        print(f"Your two roots are x₁ = {x1} and x₂ = {x2}")
        get_and_plot_graph_values(None, a, b, c, x1, x2)


def get_and_plot_graph_values(midpoint, a, b, c, x1, x2):
    if x1 is None:  # If there is not 2 roots
        if midpoint < 0:  # If midpoint is less than 0
            x = numpy.linspace(midpoint - (abs(midpoint) - midpoint), abs(midpoint))
        elif midpoint > 0:  # If midpoint is greater than 0
            x = numpy.linspace(-midpoint, midpoint + (2 * midpoint))
        else:  # If midpoint is right on 0
            x = numpy.linspace(-a, a)
    else:  # If there are 2 zeros
        x_values = [x1, x2]
        middle_to_zero = (abs(x1) + abs(x2)) / 2
        lowest_x_value = (min(x_values) - middle_to_zero)
        highest_x_value = (max(x_values) + middle_to_zero)
        x = numpy.linspace(lowest_x_value, highest_x_value)
    plt.axhline(0, color="black")  # X-Axis Line
    plt.axvline(0, color="black")  # Y-Axis Line
    plt.grid()  # Show grid
    y = a * x ** 2 + b * x + c
    plt.plot(x, y)
    plt.show()


main()
