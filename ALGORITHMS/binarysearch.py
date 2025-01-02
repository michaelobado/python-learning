# Time complexity is log n
# Only works if your list is in a sorted order

def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1

    return None

mylist = [1, 5, 7, 8, 9, 11]
print(binary_search(mylist, 11))