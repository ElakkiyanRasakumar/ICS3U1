from math import *
def main():
    print("""
    Welcome!
    This program will help you find the roots of a quadratic in standard form. 
    ax²+bx+c
    By inputting an "a", "b", "c" value 
    This program will caluclate the roots
    """)
    a_value = int(input("What is your a value? "))
    b_value = int(input("What is your b value? "))
    c_value = int(input("What is your c value? "))
    quadratic_formula(a_value, b_value, c_value)
    # print(x1, x2)
def quadratic_formula(a, b, c):
    print("With the values give this is your standard form: ")
    if a == 1:
        print(f"x{chr(178)}", end="")
    if a == -1:
        print(f"-x{chr(178)}", end="")
    if b < 0:
        print(f"{b}x", end="")
    else:
        print(f"+{b}x", end="")
    if c < 0:
        print(f"{c} = 0", end="")
    else:
        print(f"+{c} = 0")

    d = (b**2) - (4*a*c)
    if d < 0:
        return print("There are no specific roots")
    elif d == 0:
        return print(f"The quadratic equation you have specified has one root, at x = {(-(b) + sqrt(d))/(2*a)}")
    else:
        x1 = (-(b) + sqrt(d))/(2*a)
        x2 = (-(b) - sqrt(d))/(2*a)
        return print(x1, x2)


main()