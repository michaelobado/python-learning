# Python’s set data structure is just like the sets you learned about in school: it has
# certain mathematical properties that always hold, the key characteristic being that
# duplicate values are forbidden.
# Set data structure is optimized for very speedy lookup, which makes using a
# set much faster than its equivalent list when lookup is the primary requirement. As lists
# always perform slow sequential searches, sets should always be preferred for lookup.

vowels = {'a', 'e', 'i', 'o', 'u'}
#OR
vowels2 = set('aeiou')

# Set Operations
# 1. Union
# Union Works by Combining Sets

word = 'hello'
u = sorted(vowels.union(set(word)))
print(u)

# 2. Difference
# Difference, when, given two sets, can tell you what’s in one set but not the other.

d = sorted(vowels.difference(set(word)))
print(d)

# 3. Intersection
# Intersection takes the objects in one set and compares them to those in another, then reports on any common objects found.

i = vowels.intersection(set(word))
print(i)

# 1. Sets in Python do not allow duplicates.
# 2. Like dictionaries, sets are enclosed in curly braces, but sets do not identify key/value pairs. Instead, each
# unique object in the set is separated from the next by a
# comma.
# 3. Also like dictionaries, sets do not maintain insertion order (but can be ordered with the sorted function).
# 4. You can pass any sequence to the set function to create a set of elements from the objects in the
# sequence (minus any duplicates).
# 5. Sets come pre-packaged with lots of built-in functionality, including methods to perform union, difference, and
# intersection.

# Below is a list of all the available methods for the set objects:

# update()- used to update the set with union of others and itself
# add()- used to add a single item to the set
# copy()- used to return a copy of the set
# clear()- used to remove all items of the set
# discard()- used to remove an item from the set. If the item is not an element, then nothing is done
# union()- used to return a new set as a union of sets
# difference()- used to return a new set as the difference of two or more sets
# difference_update()- used to remove intersecting items from this set
# intersection()- used to return a new set as intersection of two sets
# intersection_update()- used to update a set with the intersection of another set and itself
# pop()- used to return and remove an arbitrary set item, KeyError is raised if the set is empty
# remove()- used to remove an item from the set. KeyError is raised if an item is not a member of the set
# issubset()- if another set is contained in this set, return true
# issuperset()- if this set is contained in another set, return true
# isdisjoint()- if the intersection of two sets is null, return true
# symmetric_difference- used to return a new set as the symmetric difference of two sets 
# symmetric_difference_update()- used to update a set with the symmetric difference of another set and itself 