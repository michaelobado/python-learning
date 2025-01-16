def linear_search(arr, target):

    if not arr:
        return False
    
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    
    return False

mylist = [1, 5, 7, 8, 9, 11]

print(linear_search(mylist, 11))  # Output: 5