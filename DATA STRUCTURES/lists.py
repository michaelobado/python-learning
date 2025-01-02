# A list is an ordered collection of items. In Python, lists are heteregenous and dynamic.

vowels = ['a', 'e', 'i', 'o', 'u']

# Iterating over a list by doing some comparison
# Using IN to check for membership in a list
# Can also use NOT IN to check for a lack of membership. Illustration in the append section.
word = 'Milliways'

for letter in word:
    if letter in vowels:
        print(letter)


# List Manipulation
# 1. Append
found = []
found.append('a')
found.append('e')
found.append('i')
found.append('o')
found.append('u')
print(found)

#Doesn't execute though because U already in list
if 'u' not in found:
    found.append('u')

# Logical example. Check if letter in word is available in vowels and append to available list
vowels = ['a', 'e', 'i', 'o', 'u']
# sampleWord = input('Provide a word to search for vowels: ')
sampleWord = 'Provide a word to search for vowels'
available = []

# Iterating over sampleWord and checking whether letter is in vowels. If so, append to available list
for letter in sampleWord:
    if letter in vowels:
        if letter not in available:
            available.append(letter)

# Printing found words appended in available list
for vowel in available:
    print(vowel)


# Removing Objects from a list
# 2. Remove
# Remove: takes an object’s value as its sole argument
# The remove method removes the first occurrence of a specified data value from a list. If
# the data value is found in the list, the object that contains it is removed from the list (and
# the list shrinks in size by one). If the data value is not in the list, the interpreter will raise an
# error. The remove method is great for when you know the value of the object you
# want to remove.

nums = [1, 2, 3, 4, 5]
print(nums)
print('Removing 3 from the list...')
nums.remove(3)
print(nums)

# 3. Pop
# Pop: takes an optional index value as its argument
# The pop method removes and returns an object from an existing list based on the
# object’s index value. If you invoke pop without specifying an index value, the last
# object in the list is removed and returned. If you specify an index value, the object
# in that location is removed and returned. If a list is empty or you invoke pop with
# a nonexistent index value, the interpreter raises an error.

# Not specifying index automatically removes last item in the list
print('Popping last item from the list...')
nums.pop()
print(nums)

# Removing first element in the list
print('Popping item in index 0 from the list...')
nums.pop(0)
print(nums)

# Extending a List with Objects
# 4. Extend
# Extend: takes a list of objects as its sole argument
# The extend method takes a second list and adds each of its objects to an existing
# list. This method is very useful for combining two lists into one.

print('Exteding nums list with a list of [6, 7]...')
nums.extend([6, 7])
print(nums)

# Inserting an Object into a List
# 5.Insertion
# Insert: takes an index value and an object as its arguments
# The insert method inserts an object into an existing list before a specified index
# value. This lets you insert the object at the start of an existing list or anywhere
# within the list. It is not possible to insert at the end of the list, as that’s what the
# append method does.

print('Inserting 0 at index 0 of nums list...')
nums.insert(0, 0)
print(nums)

# 6. Copying a list to another
# Avoid copying lists to another using the assignment '=' operator.
# When you do so, they'll both be pointing to the same data and a change in one will reflect in the other
# So take care when copying one list to another. If you want to have another variable reference an existing list,
# use the assignment operator (=). If you want to make a copy of the objects in an existing list and use them
# to initialize a new list, be sure to use the copy method instead.

first = [1, 2, 3, 4, 5, 6, 7, 8, 9]
second = first.copy()

""" Unlike a lot of other programming languages, Python lets you access the list relative to
each end: positive index values count from left to right, whereas negative index values
count from right to left """

# 7. Lists Slicing

# Print from index to end of list
print(first[3:])

# Print every second item starting from 0 but not including item in the index location 8
print(first[0:8:2])

# All items upto, but not including index 8
print(first[:8])

# Print every second item in the list
print(first[::2])

# Print everything from the last item in the list backwards
print(first[::-1])

""" Slicing a List Is Nondestructive
Slicing a list is nondestructive, as extracting objects from an
existing list does not alter it; the original data remains intact. """