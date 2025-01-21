# Remove all adjacent duplicates in a string
def removeDUplicates(s):

    # Initailize an empty stack
    stack = []

    # Iterate through the characters in the string
    for char in s:
        # If stack is not empty, compare top element with the chars in string
        if stack and stack[-1] == char:
            # If element is same as top element, pop it from the stack
            stack.pop()
        else:
            # If element is not same as the top element, push it to the stack
            stack.append(char)

    #Join elements in the stack without any spaces
    return "".join(stack)

print(removeDUplicates('abbddaccaaabcd'))