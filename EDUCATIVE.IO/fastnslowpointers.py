# Happy number solutiion
# Time Complexity: O (log n)
# Space Complexity: O(1)

def isHappyNumber(n):
    # Helper function that calculates the sum of squared digits.
    def sumOfSquaredNumbers(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2

        return total_sum
    
    slow_pointer = n
    fast_pointer = sumOfSquaredNumbers(n)

    while fast_pointer != 1 and slow_pointer != fast_pointer:
        slow_pointer = sumOfSquaredNumbers(slow_pointer)
        fast_pointer = sumOfSquaredNumbers(sumOfSquaredNumbers(fast_pointer))

    if fast_pointer == 1:
        return True    
    return False

print(isHappyNumber(1))

# Checking whether a Linked List has a cycle

def detectCycle(head):
    if head is None:
        return False

    # Initialize two pointers, slow and fast, to the head of the linked list
    slow, fast = head, head
    
    # Run the loop until we reach the end of the
    # linked list or find a cycle
    while fast and fast.next:
        # Move the slow pointer one step at a time
        slow = slow.next
        # Move the fast pointer two steps at a time
        fast = fast.next.next
        
        # If there is a cycle, the slow and fast pointers will meet
        if slow == fast:
            return True
    
    # If we reach the end of the linked list and haven't found a cycle, return False          
    return False
