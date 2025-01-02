# # Give an algorithm for finding the second-to-last node in a singly linked list 
# # in which the last node is indicated by a next reference of None

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def find_second_to_last(head):
#     # Edge case: empty list or list with one node
#     if head is None or head.next is None:
#         return None  # No second-to-last node exists

#     # Traverse the list until current.next.next is None
#     current = head
#     while current.next and current.next.next:
#         current = current.next

#     # Return the second-to-last node
#     return current

# # Example Usage
# # Creating a linked list: 1 -> 2 -> 3 -> 4 -> None
# node4 = Node(4)
# node3 = Node(3, node4)
# node2 = Node(2, node3)
# node1 = Node(1, node2)

# # Finding the second-to-last node
# result = find_second_to_last(node1)
# if result:
#     print("Second-to-last node value:", result.value)
# else:
#     print("No second-to-last node exists.")


# Write a Python program to create a singly linked list, append some items and iterate through the list.


class SinglyLinkedList:

    class Node:
        __slots__ = 'element', 'next'
        def __init__(self, element=None):
            self.element = element
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def iterate_item(self):

        current_item = self.head
        while current_item:
            val = current_item.element
            current_item = current_item.next

            yield val

    def append_items(self, element):
        node = self.Node(element)

        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        
        self.count += 1

    def search_item(self, val):

        for item in self.iterate_item():
            if val == item:
                return True
        return False
    
    def __getitem__(self, index):
        if index > self.count - 1:
            return 'Index is out of range'
        
        current_val = self.head
        for n in range(index):
            current_val = current_val.next

        return current_val.element
    
    def __setitem__(self, index, data):
        if index > self.count - 1:
            return 'Index is out of range'
        
        current_val = self.head
        for _ in range(index):
            current_val = current_val.next

        current_val.element = data

items = SinglyLinkedList()
items.append_items('Sugar')
items.append_items('Flour')
items.append_items('Rice')
items.append_items(1000)
results = items.search_item('Mango')

for val in items.iterate_item():
    print(val)

print('The first element in the list is: ', items.head.element)
print('The last element in the list is: ', items.tail.element)
print(items.count)
print(results)
print(items[0])
print(items[1])
print('-------------')
items[0] = 1
print(items[0])
for val in items.iterate_item():
    print(val)