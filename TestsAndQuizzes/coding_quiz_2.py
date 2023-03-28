"""
CodingBat Test #2 - Logic-1 and Logic-2

Place all three programs into one Replit. Call the Replit CodingBat Test #2. At the end of the test, copy the code
into an email, send it to me, and share the Replit with me.Your code will be marked on correctness of the results as
well as efficiency of the code. Make sure you include all the test cases shown below. If you try the code with other
calls, erase them.

The rule for determining if a year is a leap year or not is that all years divisible by 4 are leap years, except for
those which are divisible by 100 but not by 400. Years not evenly divisible by 4 are never leap years.

def leapYear (year):
         #write your code here

Here are some sample calls to this method and the output that should result:
print (leapYear (1999)) → False
print (leapYear (1900)) → False
print (leapYear (2020)) → True
print (leapYear (2000)) → True
"""


def leapYear(year):
    if year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0:
        return True
    return False


print(leapYear(1999))
print(leapYear(1900))
print(leapYear(2020))
print(leapYear(2000))

"""
At a certain oceanfront location, swimming is considered okay if the water temperature is between 22 Celsius and 33 Celsius inclusive and it is night, or, if it's not nighttime, between 21 Celsius and 32 Celsius inclusive. However, swimming is not considered okay if it's high tide, regardless of the water temperature. Fill in the body of the function so that it returns true if swimming is considered okay, false if it's not. Make sure you include the print() for spacing purposes.
print ()
def swimming (temp, nightTime, highTide):
       #write your code here

Here are some sample calls to this function and the results that they are supposed to give:

print(swimming (24, False, True))→ False
print(swimming (33, False, False))→ False
print(swimming (22, True, False))→ True
print(swimming (27, True, False))→ True
"""


def swimming(temp, nightTime, highTide):
    if highTide:
        return False
    if nightTime and 33 >= temp >= 22:
        return True
    if not nightTime and 32 >= temp >= 21:
        return True
    else:
        return False


print(swimming(24, False, True))
print(swimming(33, False, False))
print(swimming(22, True, False))
print(swimming(27, True, False))


"""
Given 3 int values, a b c, return their sum. However, if any of the values is odd, it should be changed to the even number that immediately precedes e.g. 1013 would be changed to 1012. Write the helper function "def fix_odd(n):"that takes in an int value and returns that value fixed for this rule. If the value is not odd, then the fix_odd function should not change the value. Some sample runs and the expected results are included. Make sure you include the print() for spacing purposes.

print ()
def fix_odd (n):
    #write your code here
    
def no_odds (a, b, c):
    return fix_odd(a) + fix_odd (b) + fix_odd (c)
    
print (no_odds (5, 9, 15)) → 26
print (no_odds (4, 10, 20)) → 34
print (no_odds (3, 8, 14)) → 24
print (no_odds (127, 202, 255)) → 582
"""


def fix_odd(n):
    return n - 1 if n % 2 != 0 else n


def no_odds(a, b, c):
    return fix_odd(a) + fix_odd(b) + fix_odd(c)


print(no_odds(5, 9, 15))
print(no_odds(4, 10, 20))
print(no_odds(3, 8, 14))
print(no_odds(127, 202, 255))
