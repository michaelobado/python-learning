# # “Let A be an array of size n ≥ 2 containing integers from 1 to n − 1, 
# # inclusive, with exactly one repeated. Describe a fast algorithm for finding the integer in A that is repeated”

def find_repeating_number(n):
    polished_list = []

    for i in n:
        if i in polished_list:
            print(f'{i} is a repeating number')
        else:
            polished_list.append(i)

    print(polished_list)

numbers = [1, 2, 3, 4, 5, 6, 7, 5, 8, 9]
find_repeating_number(numbers)

# “Describe how the built-in sum function can be combined with Python's comprehension syntax 
# to compute the sum of all numbers in an n × n data set, represented as a list of lists.”
def sum_matric():
    numbers = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]
    total_sum = sum(sum(row) for row in numbers)

    print(total_sum)

sum_matric()

def find_integer(n, k):
    return (k in n)

numbers = ['0000', '0010', '0011']
target = '0111'
print(find_integer(numbers, target))

# “A useful operation in databases is the natural join. 
# If we view a database as a list of ordered pairs of objects, 
# then the natural join of databases A and B is the list of all ordered triples (x, y, z) such that”
# “the pair (x, y) is in A and the pair (y, z) is in B. 
# Describe and analyze an efficient algorithm for computing the natural join of a list A of n pairs and a list B of m pairs.”

def natural_join(A, B):

    # Step 1: Create a hash map for pairs in B based on the first element
    hash_map = {}    
    for y, z in B:
        if y not in hash_map:
            hash_map[y] = []
        hash_map[y].append(z)
    
    # print(hash_map)

    # Step 2: Find matching triples
    results = [] # Initialize an empty list to store the resulting triples.
    for x, y in A: # Iterate over each pair (x, y) in list A.
        if y in hash_map: # Check if y from pair (x, y) exists as a key in hash_map.
            for z in hash_map[y]: # If it does, loop over each z associated with that y.
                results.append((x,y,z)) # Add the triple (x, y, z) to the result list.

    return results

A = [(1, 2), (2, 3), (4, 2)]
B = [(2, 5), (3, 6), (2, 7)]
print(natural_join(A, B))

def add_matrices():

    matrix_A = [[1, 2, 3], [2, 3, 4], [4, 2, 5]]
    matrix_B = [[2, 5, 6], [3, 6, 7], [2, 7, 8]]
    results_matrix = [[0] * 3 for j in range(3)]

    if len(matrix_A) != 3 or len(matrix_B) != 3:
        raise ValueError('The matrices must have same number of rows')
    
    for row_A, row_B in zip(matrix_A, matrix_B):
        if len(row_A) != len(row_B):
            raise ValueError('The matrices must have same number of columns')
    
    # if any(len(row) != 3 for row in matrix_A) or any(len(row) != 3 for row in matrix_B):
    #     raise ValueError('All rows in matrices must have 3 elements')

    for i in range(3):
        for j in range(3):
            results_matrix[i][j] = matrix_A[i][j] + matrix_B[i][j]
    
    return results_matrix

answer = add_matrices()
print(answer)

import random
class RandomizedSet:
    def __init__(self):
        self.data_map = {}
        self.data_list = []

    def insert(self, val):
        if val in self.data_map:
            return False
        
        self.data_map[val] = len(self.data_list)
        self.data_list.append(val)

    def remove(self, val):
        if val not in self.data_map:
            return False
        
        idx_to_remove = self.data_map[val]
        last_element = self.data_list[-1]

        self.data_list[idx_to_remove] = last_element
        self.data_map[last_element] = idx_to_remove

        self.data_list.pop()
        del self.data_map[val]

        return True

    def randomizedChoice(self):
        return random.choice(self.data_list)

obj = RandomizedSet()
param_1 = obj.insert(20)
param_1 = obj.insert(15)
param_1 = obj.insert(6)
param_1 = obj.insert(40)
param_2 = obj.remove(6)
param_3 = obj.randomizedChoice()

# Solve the problem of finding two elements in an array that add up to a given target
# 1. Brute Force --> )(n^2)

def find_pairs(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return nums[i], nums[j]
            
        return None

arr = [2, 7, 11, 15]
value = 18
print(find_pairs(arr, value))    


def two_sum_brute_force(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return arr[i], arr[j]
    return None

# Example usage
arr = [2, 7, 11, 15]
target = 13
print(two_sum_brute_force(arr, target))  # Output should be (7, 11)


# def find_two_nums(nums, target):
#     compliments = {}
#     for num in nums:
#         if num in compliments:
#             return compliments[num], num
#         compliments[target - num] = num

#     return None