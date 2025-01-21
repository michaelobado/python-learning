# Write a function that takes a string, s, as an input and determines whether or not it is a palindrome

def isPalindromeTwoPointers(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = ''.join(s.split()).lower()

    # Initialize two pointers
    left, right = 0, len(s) - 1

    while left < right:
        # If characters at pointers don't match, it's not a palindrome
        if s[left] != s[right]:
            return False
        # Move pointers towards the center
        left += 1
        right -= 1

    return True

# Example usage
print(isPalindromeTwoPointers("Racecar"))  # Output: True
print(isPalindromeTwoPointers("hello"))    # Output: False
print(isPalindromeTwoPointers("A man a plan a canal Panama"))  # Output: True

# Given an array of integers, nums, and an integer value, target, 
# determine if there are any three integers in nums whose sum is equal to the target, 
# that is, nums[i] + nums[j] + nums[k] == target. 
# Return TRUE if three such integers exist in the array. Otherwise, return FALSE.

def threeSum(nums, target):
    # Step 1: Sort the array to enable the two-pointer technique
    nums.sort()

    # Step 2: Iterate through the array, fixing one element at a time
    for i in range(len(nums) - 2):
        # Initialize two pointers: one just after the fixed element and one at the end of the array
        left, right = i + 1, len(nums) - 1

        # Step 3: Use a while loop to find pairs that, with nums[i], sum to the target
        while left < right:
            # Calculate the current sum of the triplet
            current_sum = nums[i] + nums[left] + nums[right]

            # Step 4: Check if the current sum equals the target
            if current_sum == target:
                # If a valid triplet is found, return True
                return True
            # Step 5: Adjust pointers based on the current sum
            elif current_sum < target:
                # If the current sum is less than the target, move the left pointer to the right
                # to increase the sum
                left += 1
            else:
                # If the current sum is greater than the target, move the right pointer to the left
                # to decrease the sum
                right -= 1

    # Step 6: If no triplet is found that sums to the target, return False
    return False

# Example usage:
nums = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0
print(threeSum(nums, target))  # Output: True

# Remove nth node from a linked list
# Separate classes provided as part of the solution

from linkedList import LinkedList
from linkedListNode import LinkedListNode

def remove_nth_last_node(head, n):

    # Point two pointers, right and left, at head.
    right = head
    left = head

    # Move right pointer n elements away from the left pointer.
    for _ in range(n):
        right = right.next
    
    # Removal of the head node if right now points to null, meaning it has reached end of list.
    if not right:
        return head.next
    
    # Move both pointers until right pointer reaches the last node.
    while right.next:
        right = right.next
        left = left.next

    # At this point, left pointer points to (n-1)th element.
    # So link it to next to next element of left.
    left.next = left.next.next

    return head

# Fast and slow pointers
# Check whether or not a linked list contains a cycle

class LinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def has_cycle(head):
    # Initialize two pointers, slow and fast
    slow = head
    fast = head
    
    while fast is not None and fast.next is not None:
        slow = slow.next          # Move slow pointer one step
        fast = fast.next.next     # Move fast pointer two steps
        
        if slow == fast:          # Cycle detected
            return True
    
    return False  # No cycle if fast pointer reaches the end of the list

# Example usage
node1 = LinkedListNode(1)
node2 = LinkedListNode(2)
node3 = LinkedListNode(3)
node4 = LinkedListNode(4)
node5 = LinkedListNode(5)

# Linking nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3  # This creates a cycle (node3 -> node5 -> node3)

# Check if the list contains a cycle
print(has_cycle(node1))  # Output: True (since there is a cycle)

# If you remove the cycle by commenting the line `node5.next = node3` above
# The output will be False as there is no cycle anymore.
