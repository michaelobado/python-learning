# Recursive algo to find sum of a list

def sum(numbers):

    if not numbers:
        return 0
    
    if len(numbers) == 1:
        return numbers[0]
    
    return numbers[0] + sum(numbers[1:])

print(sum([1, 2, 3, 10]))

# Write a recursive function to count the number of items in a list

def countItems(items):
    if not items:
        return 0
    
    return 1 + countItems(items[1:])

print(countItems([1, 2, 3, 4, 5, 6]))

# Write a recursive function to find the maximum number in a list.

def findMax(lst):
    if not lst:
        return None
    
    if len(lst) == 1:
        return lst[0]
    
    max_of_rest = findMax(lst[1:])

    if lst[0] > max_of_rest:
        return lst[0]
    else:
        return max_of_rest
    
print(findMax([1, 2, 3, 7, 9]))

