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
    x1, x2= quadratic_formula(a_value, b_value, c_value)
    # print(quadratic_formula(a_value, b_value, c_value))
    print(x1, x2)
def quadratic_formula(a, b, c):
    x1 = (-(b) + sqrt((b**2)-(4*a*c)))/(2*a)
    x2 = (-(b) - sqrt((b**2)-(4*a*c)))/(2*a)
    return x1, x2


main()