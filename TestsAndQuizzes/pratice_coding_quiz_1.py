"""ICS 3U1 PRACTICE CODING QUIZ #1					March 7, 2023

Once you’ve done the questions below, copy the code from your file into an email, send it to me AND share the replit
with me. Call the replit “Practice Coding Quiz #1”. Marks will be given primarily for correctness of code,
but also a little for efficiency of code i.e. all other things being equal, a shorter, more efficient solution
will  get a slightly higher mark than a longer, less efficient solution.

Copy the code given below and complete the function definition so that the function, if given a string whose length
is divisible by 3, will return the first third of the string. If given a string whose length is not divisible by 3,
the function should return “String not divisible into thirds”. The string passed to the function will always have at
least 1 character. Four sample function calls and their expected results are given to you. Include these function
calls in your code.

def third(str):
  #write your code here


print (third ("abc"))	#should return a
print (third ("x"))	#should return “String not divisible…”
print (third ("pq"))	#should return “String not divisible…”
print (third (“abcdefghi”) #should return abc

Insert “print ()” after the above to print a blank line. Then,Into the same file, copy the code given below,
 and complete the function so that it returns true if the middle 2 digits of a 4 digit number are within 10 of 50
 i.e. if the middle 2 digits range from 40-60. Four sample function calls and their expected results are given to you.
 Include these function calls in your code.

def middle_two (n):
    #write your code here

print (middle_two (1805))	#should return False
print (middle_two (1504))	#should return True
print (middle_two (5448))	#should return True
print (middle_two (4086))	#should return False

"""


def third(str):
    return "String not divisible..." if len(str) % 3 != 0 else str[:len(str) // 3]


print(third("abc"))  # should return a
print(third("x"))  # should return “String not divisible…”
print(third("pq"))  # should return “String not divisible…”
print(third("abcdefghi"))

print()


def middle_two(n):
    n = str(n)
    n = str(n[1:3])
    n = int(n)
    return True if 10 <= n <= 50 else False


print(middle_two(1805))  # should return False
print(middle_two(1504))  # should return True
print(middle_two(5448))  # should return True
print(middle_two(4086))  # should return False
