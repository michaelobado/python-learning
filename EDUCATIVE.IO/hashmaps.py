# Logger rate limiter.

# Initialize an empty dictionary to store request - timestamp pairs
logger = {}
# Define the limit
limit = 7

def requestLogger(request, timestamp):
    # Optional, but typically means -- use the global logger dictionary
    global logger

    # Check if the request is not in logger or timestamp is greater than or equals to set limit
    # If that's the case, add to dictionary
    if request not in logger or timestamp - logger[request] >= limit:
        logger[request] = timestamp
        return True
    else:
        return False
    
print(requestLogger('Hello', 1))
print(requestLogger('Hello', 2))
print(requestLogger('Good', 7))
print(requestLogger('Good', 11))

# Given the two distinct integer arrays, nums1 and nums2, 
# where nums1 is a subset of nums2, 
# find all the next greater elements for nums1 values in the corresponding places of nums2.

def nextGreaterElement(nums1, nums2):
    
    stack = []
    greater = {}

    # Go through nums2, if num is greater than element on top of stack
    # Pop it, using it as a key in your dict with num as the value 
    for num in nums2:
        while stack and num > stack[-1]:
            greater[stack.pop()] = num
        # Push the num to the stack
        stack.append(num)

    # Remaining elements in the stack whose next greater element wasn't found
    # Pop the using them as key and set their values to -1
    while stack:
        map[stack.pop()] = -1

    # Initialize an empty list to store results
    ans = []
    # Using nums as key, append their corresponding values to ans
    for num in nums1:
        ans.append(greater[num])

    return ans

# Given two strings, check whether two strings are isomorphic to each other or not

def isIsomorphic(string1, string2):
    # Initialize two empty dicts to store mappings from string1 to string2 and vice versa
    s1_s2 = {}
    s2_s1 = {}

    for i in range(len(string1)):
        char_str1 = string1[i]
        char_str2 = string2[i]
        
        # returning false if char_1 in string1 exist in hashmap
        # and the char_1 has different mapping in hashmap
        if char_str1 in s1_s2 and s1_s2[char_str1] != char_str2:
            return False
        
        # returning false if char_2 in string2 exist in hashmap
        # and the char_2 has different mapping in hashmap
        if char_str2 in s2_s1 and s2_s1[char_str2] != char_str1:
            return False
        
        # mapping of char of one string to another and vice versa
        s1_s2[char_str1] = char_str2
        s2_s1[char_str2] = char_str1

    return True
print('######')
print(isIsomorphic('egg', 'all'))
print(isIsomorphic('foo', 'bar'))