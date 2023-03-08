"""
ICS 3U1 CODING QUIZ #1							March 8, 2023

Once you’ve done the questions below, copy the code from your file into an email, send it to me AND share the replit with me. Call the Replit “Coding Quiz #1”. Marks will be given primarily for correctness of code, but also a little bit for efficiency of code i.e. all other things being equal, a shorter, efficient solution will get a slightly higher mark than a longer, less efficient solution. Once I announce time is up, I’ll give you a minute or so to email me your code. After that, marks will be subtracted at the rate of 1 mark for every minute late.

Copy the code given below and complete the function definition so that the function, if given an odd length string will return the string’s middle character and, if given an even length string, will return the two middle characters. You may assume that the string passed to the function will always have at least 1 character. Four sample function calls and their expected results are given to you. Include these function calls in your code. If you try your code with other calls, erase them prior to submission.

def middle (str):
  #write your code here


print (middle ("abcd"))	#should return bc
print (middle ("x"))		#should return x
print (middle ("pq"))		#should return pq
print (middle ("radar"))	#should return d

Into the same file, copy the code given below and complete the function so that it returns true if the number passed to it is within 10 of any multiple of 100 from 0 up to whatever is the largest integer Python can store (what that actual value is is irrelevant). Five sample function calls and their expected results are given to you. Include these function calls in your code. For full marks, your solution should be strictly mathematical.

def near_a_multiple (n):
    #write your code here

print (near_a_multiple (1690))	#should return True
print (near_a_multiple (10005))	#should return True
print (near_a_multiple (51))	#should return False
print (near_a_multiple (411))	#should return False
print (near_a_multiple (1000001))#should return True
"""
def middle (str):
  return str[len(str)//2] if len(str) % 2 else str[len(str)//2-1: len(str)//2+1]


print (middle ("abcd"))	#should return bc
print (middle ("x"))		#should return x
print (middle ("pq"))		#should return pq
print (middle ("radar"))	#should return d


def near_a_multiple(n):
    return n % 100 <= 10 or n % 100 >= 90


print(near_a_multiple(1690))  # should return True
print(near_a_multiple(10005))  # should return True
print(near_a_multiple(51))  # should return False
print(near_a_multiple(411))  # should return False
print(near_a_multiple(1000001))  # should return True

