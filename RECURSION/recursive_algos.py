# “Recursion is a technique by which a function makes one or more calls to itself during execution, 
# or by which a data structure relies upon smaller instances of the very same type of structure in its representation.”

# Binary list recursive function solution
def binary_search(data, target, low, high):

    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            high = mid - 1
            return binary_search(data, target, low, high)
        else:
            low = mid + 1
            return binary_search(data, target, low, high)        

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results = binary_search(numbers, 9, 0, 8)
print(f'Target found at {results}')

def search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None


def verify(index):
    if index is not None:
        print(f'Target found at {index}')
    else:
        print('Target not found in list')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results = search(numbers, 11)
verify(results)

# File system sample function to return number of bytes used by a file/folder and any descendants
import os

def disk_usage(path):

    total = os.path.getsize(path) # Account for direct usage
    # Check if path is directory, then return the child directories or filenames in it
    if os.path.isdir(path): # If this is a directory
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
    
    print('{0:<7}'.format(total), path)
    return total

disk_usage('/Users/michaelobado/Documents/Programming')

def linear_sum(S, n):
    if n == 0:
        return 0
    else:
        return linear_sum(S, n -1) + S[n-1]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    
sum = linear_sum(numbers, 5)
print(sum)

# Normal function to return largest number
def findMax(S):
    largest = 0
    for i in S:
        if i > largest:
            largest = i
    return largest

numbers = [5, 103, 68, 3, 91]
ans = findMax(numbers)
print(ans)

# Recursive function to find largest number
def find_largest(S, n):

    if n == 1:
        return S[0]
    else:
        previous = find_largest(S, n-1)
        current = S[n-1]
        if previous > current:
            return previous
        else:
            return current

numbers = [5002, 103, 68, 3, 917]
length = len(numbers)
ans = find_largest(numbers, length)
print(ans)

# Write a short recursive Python function that finds the minimum and maximum values in a seq wihtout using any loops
def find_min_max(seq, n):
    if n == 0:
        return -1
    elif n == 1:
        return seq[0], seq[0]
    else:
        min, max = find_min_max(seq, n - 1)
        current = seq[n - 1]
        if current < min:
            min = current
        if current > max:
            max = current
        
        return (min, max)
        
numbers = [1, 1032, 4, 3, 917]
length = len(numbers)
ans = find_min_max(numbers, length)
print(ans)

# Give a recursive algorithm to compute the product of two positive integers, m and n, using only addition and subtraction.

def product(m, n):
    if n == 0:
        return 0
    elif n == 1:
        return m
    else:
        return m + product(m, n -1)
    
result = product(0, 5)
print(result)

def towers_of_hanoi(n, source, target, auxilliary):
    # Base case: If there is only one disk, move it directly from source to target
    if n == 0:
        #print(f'Move disk {n} from {source} to {target}')
        return
    
    # Recursive case: move n-1 disks from source to auxiliary
    towers_of_hanoi(n-1, source, auxilliary, target)

    # Move the nth disk from source to target
    print(f'Move disk {n} from {source} to {target}')

    towers_of_hanoi(n-1, auxilliary, target, source)

n = 4 # Number of disks
towers_of_hanoi(n, 'a', 'c', 'b')

# Write a recursive function that will output all the subsets of a set of n elements (without repeating any subsets)
def generate_subsets(input_set):
    # Base case: if the set is empty, return a set containing an empty set
    if not input_set:
        return [set()]
    
    # Convert the input set to a list to access elements by index
    input_list = list(input_set)
    first_element = input_list[0]
    
    # Generate all subsets excluding the first element
    subsets_without_first = generate_subsets(set(input_list[1:]))
    
    # Generate all subsets including the first element
    subsets_with_first = [subset | {first_element} for subset in subsets_without_first]
    
    # Combine the subsets with and without the first element
    return subsets_without_first + subsets_with_first

# Example usage
input_set = {4, 2, 3}
all_subsets = generate_subsets(input_set)
for subset in all_subsets:
    print(subset)

# Write a short recursive Python function that takes a character string s and outputs its reverse. 
# For example, the reverse of ‘pots&pans’ would be ‘snap&stop’.
def reverse_string(s):
    # Base case: if the string is empty or has one character, return it as is
    if len(s) <= 1:
        return s
    # Recursive case: take the last character and add it to the reverse of the rest
    return s[-1] + reverse_string(s[:-1])

# Example usage
print(reverse_string("pots&pans"))  # Output: snap&stop

# Write a short recursive Python function that determines if a string s is a palindrome, that is, it is equal to its reverse. 
# For example, ‘racecar’ and ‘gohangasalamiimalasagnahog’ are palindromes
def is_palindrome(s):
    # Base case: if the string is empty or has one character, it’s a palindrome
    if len(s) <= 1:
        return True
    # Check the first and last characters; if they’re different, it’s not a palindrome
    if s[0] != s[-1]:
        return False
    # Recursive call on the substring without the first and last characters
    return is_palindrome(s[1:-1])

# Example usage
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False

# Use recursion to write a Python function for determining if a string s has more vowels than consonants.
def has_more_vowels(s, vowel_count=0, consonant_count=0):
    # Base case: if the string is empty, compare vowel and consonant counts
    if not s:
        return vowel_count > consonant_count

    # Check if the first character is a vowel or consonant
    first_char = s[0].lower()
    if first_char in "aeiou":
        vowel_count += 1
    elif first_char.isalpha():
        consonant_count += 1

    # Recursive call with the rest of the string
    return has_more_vowels(s[1:], vowel_count, consonant_count)

# Example usage
print(has_more_vowels("hello"))  # Output: False
print(has_more_vowels("education"))  # Output: True

# Given an unsorted sequence, S, of integers and an integer k, describe a recursive algorithm for 
# rearranging the elements in S so hat all elements less than an integer k appear before those greater than or equal to k
# Solution below not fully working right
def rearrange_sequence(S, k):
    if not S:
        return []
    
    first = S[0]
    rest = S[1:0]

    if first < k:
        return [first] + rearrange_sequence(rest, k)
    else:
        return rearrange_sequence(rest, k) + [first]
    
numbers = [3, 8, 9, 4, 7, 2, 6]
print(rearrange_sequence(numbers, 2))

# Suppose you are given an n-element sequence, S, containing distinct integers that are listed in increasing order. 
# Given a number k, describe a recursive algorithm to find two integers in S that sum to k, if such a pair exists.
def find_pair_with_sum(S, k, start=0, end=None):
    if end is None:
        end = len(S) - 1
    
    # Base case: if start pointer crosses end pointer
    if start >= end:
        return None
    
    current_sum = S[start] + S[end]
    
    # Check if current pair equals k
    if current_sum == k:
        return (S[start], S[end])
    elif current_sum < k:
        # Increment start pointer to increase sum
        return find_pair_with_sum(S, k, start + 1, end)
    else:
        # Decrement end pointer to decrease sum
        return find_pair_with_sum(S, k, start, end - 1)

# Example usage
S = [1, 3, 5, 6, 9]
k = 8
print(find_pair_with_sum(S, k))  # Output should be a pair, like (1, 9), that sums to k

    

