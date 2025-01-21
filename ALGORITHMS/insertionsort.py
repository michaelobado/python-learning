# Runtimes
# Best Case: O(n^2)
# Average Case: O(n^2)
# Worst Case: O(n^2)
# Space Complexity: O(1)

def insertionSort(arr, rightIndex, target):
    if target in arr:
        arr.remove(target)
    
    # Insert target at the correct position
    for i in range(rightIndex + 1):
        if target < arr[i]:  # Find the correct position for the target
            arr.insert(i, target)
            return arr  # Return only after insertion
    else:
        arr.insert(rightIndex + 1, target) # If target is greater than all elements including rightIndex
    
    return arr

# Example usage:
array = [1, 3, 5, 7, 9]
rightIndex = 4
# Case where target is greater than the value at rightIndex
value = 10
print(insertionSort(array, rightIndex, value))  # Correct output: [1, 3, 5, 7, 9, 13]

def insertion_sort(arr):
    # Loop through the array starting from the second element
    for i in range(1, len(arr)):
        # Store the current element in a variable
        current_value = arr[i]
        # Initialize the position to compare with previous elements
        position = i

        # Shift larger elements to the right
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]  # Move the larger element one position to the right
            position -= 1  # Move to the next position on the left
        
        # Insert the current element at its correct position
        arr[position] = current_value

    return arr

# Example usage
array = [7, 2, 4, 1, 5]
sorted_array = insertion_sort(array)
print(sorted_array)  # Output: [1, 2, 4, 5, 7]
# 
