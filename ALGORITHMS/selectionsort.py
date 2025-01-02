# Runtimes
# Best Case: O(n^2)
# Average Case: O(n^2)
# Worst Case: O(n^2)
# Space Complexity: O(1)

def findSmallest(arr):
    """
    Find the smallest element in an array and return its index.
    
    Parameters:
    arr (list): The list to search for the smallest element.

    Returns:
    int: The index of the smallest element in the list.
    """
    # Assume the first element is the smallest
    smallest = arr[0]
    smallestIndex = 0

    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # Update the smallest value and its index if a smaller element is found
        if arr[i] < smallest:
            smallest = arr[i]
            smallestIndex = i

    # Return the index of the smallest element
    return smallestIndex


def selectionSort(arr):
    """
    Perform selection sort on a given array and return a new sorted array.
    
    Parameters:
    arr (list): The list to sort.

    Returns:
    list: A new list containing the sorted elements of the input list.
    """
    # Initialize a new empty list to store the sorted elements
    newArr = []
    # Create a copy of the input list to avoid modifying the original list
    copiedArr = list(arr)

    # Repeat until all elements are sorted
    for i in range(len(copiedArr)):
        # Find the index of the smallest element in the remaining list
        smallest = findSmallest(copiedArr)
        # Remove the smallest element from the copied list and append it to the sorted list
        newArr.append(copiedArr.pop(smallest))

    # Return the sorted list
    return newArr


# Example usage of selectionSort
print(selectionSort([5, 3, 6, 2, 10]))  # Output: [2, 3, 5, 6, 10]


# Another way to write the selection sort without relying on the findSmallest helper function

def selectionSort(arr):
    """
    Perform selection sort on a given array and return a new sorted array.

    Parameters:
    arr (list): The list to sort.

    Returns:
    list: A new list containing the sorted elements of the input list.
    """
    newArr = []  # Initialize a new list to store sorted elements
    copiedArr = list(arr)  # Create a copy of the original list to avoid modifying it

    while copiedArr:  # Continue until all elements are sorted
        # Find the smallest element and remove it from the copiedArr
        smallest = min(copiedArr)  # Use the built-in min() function to find the smallest
        copiedArr.remove(smallest)  # Remove the smallest element from copiedArr
        
        # Append the smallest element to the new sorted list
        newArr.append(smallest)

    return newArr  # Return the sorted list


# Example usage
print(selectionSort([5, 3, 6, 2, 10]))  # Output: [2, 3, 5, 6, 10]
