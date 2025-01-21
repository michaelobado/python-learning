# Runtimes
# Best Case: O(n log n)
# Average Case: O(n log n)
# Worst Case: O(n^2)
# Space Complexity: O(n log n)

def quicksort(array):
    """
    Implements the Quicksort algorithm to sort a list of numbers.

    Parameters:
    array (list): The list of numbers to sort.

    Returns:
    list: A new sorted list containing the elements of the input array.
    """

    # Base case: If the array has fewer than 2 elements, it is already sorted.
    if len(array) < 2:
        return array

    else:
        # Choose the first element in the array as the pivot.
        pivot = array[0]

        # Create a sublist of all elements in the array (excluding the pivot)
        # that are less than or equal to the pivot.
        lesser = [i for i in array[1:] if i <= pivot]

        # Create a sublist of all elements in the array (excluding the pivot)
        # that are greater than the pivot.
        greater = [i for i in array[1:] if i > pivot]

        # Recursively sort the 'lesser' sublist, add the pivot in between,
        # and recursively sort the 'greater' sublist. Combine the results
        # into a single sorted list and return it.
        return quicksort(lesser) + [pivot] + quicksort(greater)

# Example usage
# Call the quicksort function with an unsorted list and print the sorted list.
print(quicksort([10, 5, 2, 3]))


# Rewriting the above with the pivot randomly selected

import random

def quicksort(arr):
    """
    Sorts an array using the Quicksort algorithm with a random pivot.

    Parameters:
    arr (list): The list to be sorted.

    Returns:
    list: The sorted list.
    """
    if len(arr) <= 1:
        return arr
    
    # Choose a random pivot
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    
    # Partition the array into three parts
    less_than_pivot = [x for x in arr if x < pivot]
    equal_to_pivot = [x for x in arr if x == pivot]
    greater_than_pivot = [x for x in arr if x > pivot]
    
    # Recursively sort and combine the partitions
    return quicksort(less_than_pivot) + equal_to_pivot + quicksort(greater_than_pivot)

# Example usage
unsorted_list = [3, 6, 8, 10, 1, 2, 1]
sorted_list = quicksort(unsorted_list)
print(sorted_list)  # Output: [1, 1, 2, 3, 6, 8, 10]

def quickSort(array):

    if len(array) <= 2:
        return array
    else:
        pivot = array[0]

        lesser = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

    return quickSort(lesser) + [pivot] + quickSort(greater)

array = [10, 7, 8, 9, 1, 5]
print(quickSort(array))

# Using a mid element in the array as pivot

def quickSort(array):

    if len(array) < 2:
        return array
    else:
        mid = len(array) // 2
        pivot = array[mid]

        lesser = [i for i in array if i < pivot]
        equal = [i for i in array if i == pivot]
        greater = [i for i in array if i > pivot]

    return quickSort(lesser) + equal + quickSort(greater)

array = [10, 7, 8, 9, 1, 5]
print(quickSort(array))