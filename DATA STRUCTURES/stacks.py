# A stack is a collection of objects that are inserted 
# and removed according to the last-in, first-out (LIFO) principle

# Here’s a list of common stack operations, which are essential for managing data in a Last-In-First-Out (LIFO) order:

# 1. Push: Adds an element to the top of the stack.
#    - Time Complexity**: \(O(1)\)

# 2. Pop: Removes the element from the top of the stack and returns it. Raises an error if the stack is empty.
#    - Time Complexity: \(O(1)\)

# 3. Peek/Top: Returns the element on top of the stack without removing it.
#    - Time Complexity: \(O(1)\)

# 4. isEmpty: Checks whether the stack is empty and returns `True` if it is; otherwise, it returns `False`.
#    - Time Complexity: \(O(1)\)

# 5. isFull (for fixed-size stacks): Checks whether the stack has reached its maximum capacity.
#    - Time Complexity: \(O(1)\)

# 6. Size: Returns the number of elements currently in the stack.
#    - Time Complexity: \(O(1)\)

class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self._data = []

    # Returns length of the stack
    def __len__(self):
        return len(self._data)
    
    # Returns True if Stack is empty, False if not
    def is_empty(self):
        return self._data == 0
    
    # Adds element to the top of Stack
    def push(self, e):
        self._data.append(e)

    # Returns element at the top of the Satck
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._data[-1]
    
    # Removes and returns the element at the top of the stack
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()
    
# S = ArrayStack( )               # contents: [ ]
# S.push(5)                       # contents: [5]
# S.push(3)                       # contents: [5, 3]
# print(len(S))                   # contents: [5, 3];      outputs 2
# print(S.pop( ))                 # contents: [5];         outputs 3
# print(S.is_empty())             # contents: [5];         outputs False
# print(S.pop( ))                 # contents: [ ];         outputs 5
# print(S.is_empty())             # contents: [ ];         outputs True
# S.push(7)                       # contents: [7]
# S.push(9)                       # contents: [7, 9]
# print(S.top())                 # contents: [7, 9];      outputs 9
# S.push(4)                       # contents: [7, 9, 4]
# print(len(S))                   # contents: [7, 9, 4];   outputs 3
# print(S.pop())                 # contents: [7, 9];      outputs 4
# S.push(6)                       # contents: [7, 9, 6]

def is_matched(expr):
    S = ArrayStack()
    lefty = '({['
    righty = ')}]'

    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
            
    return S.is_empty

ans = is_matched('“[(5+x)-(y+z)]”')