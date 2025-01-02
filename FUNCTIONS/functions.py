# 1. Functions introduce two new keywords: def and return
# Both of these keywords are colored orange in IDLE. The def keyword names the function
# (shown in blue), and details any arguments the function may have. The use of the return
# keyword is optional, and is used to pass back a value to the code that invoked the function.

# 2. Functions can accept argument data
# A function can accept argument data (i.e., input to the function). You can specify a list of
# arguments between the parentheses on the def line, following the function’s name.

# 3. Functions contain code and (usually) documentation
# Code is indented one level beneath the def line, and should include comments where it
# makes sense. We demonstrate two ways to add comments to code: using a triple-quoted
# string (shown in green in the template and known as a docstring), and using a single-line
# comment, which is prefixed by the # symbol

# # An iterator
# def factors(n):
#     found  = []

#     for k in range(1, n+1):
#         if n % k == 0:
#             found.append(k)
    
#     print(found)

# factors(100)

# # A generator
# def factor(n):

#     for k in range(n, n+1):
#         if n % k == 0:
#             yield k                   

# for i in factor(20):
#     print(i)

# # Returns True if n is a multiple of m
# def is_multiple(n, m):
#     if n % m == 0:
#         return True
#     return False


# is_multiple(5, 2)

# # List comprehension with two for loops
# word_list = ['cat', 'dog','rabbit']
# #letter_list = [ ]

# # for a_word in word_list:
# #     for a_letter in a_word:
# #         if a_letter not in letter_list:
# #             letter_list.append(a_letter)
# seen = set()
# letter_list = (a_letter for a_word in word_list for a_letter in a_word)
# print(letter_list)

# # Returning Tue if k is Even, False if not.
# def isEven(k):
#     if k % 2 == 0:
#         return True
#     return False

# A function to return min and max numbers in a form of a tuple
def minMax(sequence):
    sequence.sort()
    n = len(sequence)
    min = sequence[0]
    max = sequence[n-1]
    
    print(min, max)
    return min, max

minMax([1, 2, 3, 4, 5, 6])
minMax([1])

# returns sum of squares of all integers less than n
def sumSquares(n):
    return sum(x**2 for x in range(n))

sumSquares(3)

def sumOddSquares(n):
    print (sum(x**2 for x in range(n) if x % 2 != 0))

sumOddSquares(5)