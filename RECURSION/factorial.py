def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(3))

# document = 'I am going home tonight?123@#'
# letters = ''
# temp = []

# for c in document:
#     if c.isalpha():
#         temp.append(c)

# letters = ''.join(temp)
# print(letters)