# Implement a function with signature transfer(S, T) that transfers all elements from stack S onto stack T, 
# so that the element that starts at the top of S is the first to be inserted onto T, 
# and the element at the bottom of S ends up at the top of T.

class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.isempty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def isempty(self):
        return len(self._data) == 0

    def __str__(self):
        return str(self._data)

# # Function solution
def transfer(S, T):
    while not S.isempty():
        T.push(S.pop())


S = Stack()
T = Stack()
S.push(1)
S.push(2)
S.push(3)

transfer(S, T)
print(T) 

# Give a recursive method for removing all the elements from a stack.
# Note: the isempty() would be a function in a Stack class

def clear(S):
    if not S.isempty():
        S.pop()
        clear(S)

S = Stack()
S.push(1)
S.push(2)
S.push(3)
clear(S)


# In case S is just a list

def l_clear(S):
    if S:
        S.pop()
        l_clear(S)


nums = [1, 2, 3, 4]
l_clear(nums)

# Implement a function that reverses a list of elements by pushing them onto a stack in one order, 
# and writing them back to the list in reversed order.

def reverse(nums):
    S = Stack()
    reversed_list = []

    for i in nums:
        S.push(i)

    print(S)

    while not S.isempty():
        reversed_list.append(S.pop())

    return reversed_list

nums = [1, 2, 3, 4, 5]
ans = reverse(nums)
print(ans)