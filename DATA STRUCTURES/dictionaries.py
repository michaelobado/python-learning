# Unlike a list, which is a collection of related objects, the dictionary is used
# to hold a collection of key/value pairs, where each unique key has a value
# associated with it. The dictionary is often referred to as an associative array by
# computer scientists, and other programming languages often use other names
# for dictionary (such as map, hash, and table).

person = {'Name': 'Michael',
          'Gender': 'Male',
          'Occupation': 'Software Engineer',
          'Home Planet': 'Betelgeuse Seven'}

print(person)
# Unlike lists, which keep your objects arranged in the order in which you
# inserted them, Python’s dictionary does not. This means you cannot assume
# that the rows in any dictionary are in any particular order; for all intents and
# purposes, they are unordered.

# Dictionaries use keys to access their associated data values.
print(person['Name'])
print(person['Gender'])

# Adding elements to a dictionary
person['Age'] = 33
print(person)

# Iterating over a dictionary
# Displaying only the keys in dictionary
for k in person:
    print(k)

# Displaying key and values
# Remember to always include the items()
for k, v in person.items():
    print(k, ':', v)

# Frequency count
vowels = ['a', 'e', 'i', 'o', 'u']
word = "Provide a word to search for vowels"

found = {}
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

for letter in word:
    if letter in vowels:
        found[letter] +=  1

print(found)

# Using setdefault method to set keys to a default value when they don't exist in the dictionary
for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1

# 1. By default, every dictionary is unordered, as insertion order is not maintained. If you need to sort a dictionary
# on output, use the sorted built-in function.
# 2. The items method allows you to iterate over a dictionary by row—that is, by key/value pair. On each
# iteration, the items method returns the next key and its associated value to your for loop.
# 3. Trying to access a nonexistent key in an existing dictionary results in a KeyError. When a
# KeyError occurs, your program crashes with a runtime error.
# 4. You can avoid a KeyError by ensuring every key in your dictionary has a value associated with it before
# you try to access it. Although the in and not in operators can help here, the established technique is to
# use the setdefault method instead.

# Dictionary of dictionaries

people = {}
people['Ford'] = {'Name': 'Ford Prefect',
                  'Gender': 'Male',
                  'Occupation': 'Researcher',
                  'Home Planet': 'Betelgeuse Seven' }

people['Arthur'] = {'Name': 'Arthur Dent',
                    'Gender': 'Male',
                    'Occupation': 'Sandwich-Maker',
                    'Home Planet': 'Earth' }

people['Trillian'] = {'Name': 'Tricia McMillan',
                      'Gender': 'Female',
                      'Occupation': 'Mathematician',
                      'Home Planet': 'Earth' }

import pprint
pprint.pprint(people)

# Printing Ford's occupation
print(people['Ford']['Occupation'])

# Printing Ford's home planet
print(people['Ford']['Home Planet'])