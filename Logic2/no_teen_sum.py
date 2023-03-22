def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    return 0 if 19 >= n >= 13 and n != 15 and n != 16 else n
