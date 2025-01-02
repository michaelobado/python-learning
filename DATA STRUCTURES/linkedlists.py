# “Implementing a Stack with a Singly Linked List”

# Custom exception class for empty containers
class Empty(Exception):
    pass

# Define the LinkedList class to implement a linked list-based stack
class LinkedList:

    # Nested Node class for the internal nodes of the linked list
    class _Node:
        __slots__ = '_element', '_next'  # Use slots to limit instance attributes and save memory

        def __init__(self, element, next):
            # Initialize the node with an element (data) and a reference to the next node
            self._element = element
            self._next = next

    def __init__(self):
        # Initialize the linked list with an empty head and size of 0
        self._head = None
        self._size = 0

    def __len__(self):
        # Return the number of elements in the linked list (stack size)
        return self._size
    
    def is_empty(self):
        # Check if the linked list is empty
        return self._size == 0
    
    def push(self, e):
        # Insert a new element at the head of the list (top of stack)
        self._head = self._Node(e, self._head)  # Create a new node and make it the head
        self._size += 1  # Increment the size of the stack

    def top(self):
        # Return the element at the top of the stack without removing it
        if self.is_empty():
            raise Empty('The stack is empty')  # Raise an error if stack is empty
        return self._head._element  # Return the element of the head node
    
    def pop(self):
        # Remove and return the element at the top of the stack
        if self.is_empty():
            raise Empty('The stack is empty')  # Raise an error if stack is empty
        
        answer = self._head._element  # Save the element to return
        self._head = self._head._next  # Move head to the next node, removing the top element
        self._size -= 1  # Decrement the size of the stack

        return answer  # Return the removed element

# “Implementing a Queue with a Singly Linked List”

class LinkedQueue:
    # A nested Node class to represent each element in the queue.
    class Node:
        __slots__ = '_element', '_next'  # Optimizes memory by limiting instance attributes.

        def __init__(self, element, next):
            self._element = element  # The data stored in the node.
            self._next = next  # A reference to the next node in the queue.

    def __init__(self):
        self._head = None  # Points to the first node in the queue.
        self._tail = None  # Points to the last node in the queue.
        self._size = 0  # Tracks the number of elements in the queue.

    def __len__(self):
        # Returns the number of elements currently in the queue.
        return self._size
    
    def is_empty(self):
        # Checks if the queue is empty by verifying if the size is zero.
        return self._size == 0
    
    def first(self):
        # Retrieves the element at the front of the queue without removing it.
        if self.is_empty():  # Ensures the queue is not empty before accessing the first element.
            raise Empty('The queue is empty')  # Raises an exception if the queue is empty.
        return self._head._element  # Returns the element at the front of the queue.

    def enqueue(self, e):
        # Adds an element to the end of the queue.
        newest = self.Node(e, None)  # Creates a new node with the element and no next reference.
        if self.is_empty():
            self._head = newest  # If the queue is empty, the new node becomes the head.
        else:
            self._tail._next = newest  # Links the new node to the current tail's next reference.
        self._tail = newest  # Updates the tail to point to the new node.
        self._size += 1  # Increments the size of the queue.

    def dequeue(self):
        # Removes and returns the element at the front of the queue.
        if self.is_empty():  # Ensures the queue is not empty before attempting to dequeue.
            raise Empty('The queue is empty')  # Raises an exception if the queue is empty.
        
        answer = self._head._element  # Stores the element at the front of the queue.
        self._head = self._head._next  # Updates the head to point to the next node in the queue.
        self._size -= 1  # Decrements the size of the queue.

        if self.is_empty():  # If the queue becomes empty, reset the tail to None.
            self._tail = None

        return answer  # Returns the dequeued element.
    
# Circular Linked Lists
class CircularQueue:
    # A class to represent the nodes of the circular queue.
    class Node:
        __slots__ = '_element', '_next'  # Define fixed attributes for efficiency.
        
        def __init__(self, element, next):
            self._element = element  # Store the element of the node.
            self._next = next  # Reference to the next node in the queue.

    def __init__(self):
        self._tail = None  # The tail node of the queue (points to the last node).
        self._size = 0  # The number of elements in the queue.

    def __len__(self):
        # Return the size of the queue.
        return self._size
    
    def is_empty(self):
        # Check if the queue is empty.
        return self._size == 0
    
    def first(self):
        # Retrieve the element at the front of the queue without removing it.
        if self.is_empty():
            raise Empty('The queue is empty')  # Raise an exception if the queue is empty.
        
        head = self._tail._next  # The head node is the node after the tail.
        return head._element  # Return the element at the front of the queue.
    
    def dequeue(self):
        # Remove and return the element at the front of the queue.
        if self.is_empty():
            raise Empty('The queue is empty')  # Raise an exception if the queue is empty.
        
        oldhead = self._tail._next  # The node at the front of the queue.
        if self._size == 1:
            # If there is only one element, the queue becomes empty.
            self._tail = None
        else:
            # Update the tail's next pointer to bypass the old head.
            self._tail._next = oldhead._next

        self._size -= 1  # Decrement the size of the queue.
        return oldhead._element  # Return the removed element.
    
    def enqueue(self, e):
        # Add a new element to the back of the queue.
        newest = self._Node(e, None)  # Create a new node with the given element.
        if self.is_empty():
            # If the queue is empty, the new node points to itself.
            newest._next = newest
        else:
            # Otherwise, insert the new node after the tail.
            newest._next = self._tail._next
            self._tail._next = newest
        
        self._tail = newest  # Update the tail to the new node.
        self._size += 1  # Increment the size of the queue.

    def rotate(self):
        # Rotate the front element to the back of the queue.
        if self._size > 0:
            self._tail = self._tail._next  # Move the tail pointer to the next node.


# Doubly Linked Lists

class _DoublyLinkedBase:
    # Base class for a doubly linked list structure.

    class _Node:
        # Lightweight, non-public class for storing a doubly linked node.
        __slots__ = '_element', '_next', '_prev'  # Use __slots__ to save memory by avoiding a dynamic dictionary.

        def __init__(self, element, next, prev):
            """
            Initialize a node with an element, and links to the next and previous nodes.
            :param element: The data stored in the node.
            :param next: Reference to the next node in the list.
            :param prev: Reference to the previous node in the list.
            """
            self._element = element
            self._next = next
            self._prev = prev

    def __init__(self):
        """
        Initialize an empty doubly linked list with header and trailer sentinel nodes.
        These sentinels simplify edge-case handling for insertions and deletions.
        """
        self._header = self._Node(None, None, None)  # Create a header sentinel node.
        self._trailer = self._Node(None, None, None)  # Create a trailer sentinel node.
        self._header._next = self._trailer  # Link header to trailer.
        self._trailer._prev = self._header  # Link trailer to header.
        self._size = 0  # Initialize the size of the list to 0.

    def __len__(self):
        """
        Return the number of elements in the doubly linked list.
        """
        return self._size

    def is_empty(self):
        """
        Check if the list is empty.
        :return: True if the list contains no elements, False otherwise.
        """
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """
        Add an element between two existing nodes.
        :param e: The element to insert.
        :param predecessor: The node that will precede the new node.
        :param successor: The node that will follow the new node.
        :return: The newly created node containing the element.
        """
        newest = self._Node(e, predecessor, successor)  # Create a new node.
        predecessor._next = newest  # Update the predecessor's next reference.
        successor._prev = newest  # Update the successor's previous reference.
        self._size += 1  # Increment the size of the list.
        return newest

    def _delete_node(self, node):
        """
        Delete a non-sentinel node from the list and return its element.
        :param node: The node to remove.
        :return: The element stored in the removed node.
        """
        predecessor = node._prev  # Get the node before the one to delete.
        successor = node._next  # Get the node after the one to delete.
        predecessor._next = successor  # Link the predecessor to the successor.
        successor._prev = predecessor  # Link the successor to the predecessor.
        self._size -= 1  # Decrement the size of the list.

        element = node._element  # Save the element stored in the node.
        # Clear the node's references to prevent memory leaks.
        node._prev = node._next = node._element = None
        return element  # Return the element.

# Implementing a Dequeue with a Doubly Linked List

class LinkedDeque(_DoublyLinkedBase):  
    # Class inherits from _DoublyLinkedBase, which provides fundamental operations for a doubly linked list.

    def first(self):
        """Return the first element in the deque."""
        if self.is_empty():  # Check if the deque is empty.
            raise Exception('Deque is empty!')  # Raise an error if there are no elements.
        
        return self._header._next._element  # Return the element after the header node (front of deque).

    def last(self):
        """Return the last element in the deque."""
        if self.is_empty():  # Check if the deque is empty.
            raise Exception('Deque is empty!')  # Raise an error if there are no elements.
        
        return self._trailer._prev._element  # Return the element before the trailer node (back of deque).

    def insert_first(self, e):
        """Insert an element e at the front of the deque."""
        self._insert_between(e, self._header, self._header._next)  
        # Insert a new node between the header and its next node.

    def insert_last(self, e):
        """Insert an element e at the end of the deque."""
        self._insert_between(e, self._trailer._prev, self._trailer)  
        # Insert a new node between the trailer's previous node and the trailer.

    def delete_first(self):
        """Remove and return the first element of the deque."""
        if self.is_empty():  # Check if the deque is empty.
            raise Exception('Deque is empty')  # Raise an error if there are no elements.
        
        return self._delete_node(self._header._next)  
        # Remove and return the node after the header (front of deque).

    def delete_last(self):
        """Remove and return the last element of the deque."""
        if self.is_empty():  # Check if the deque is empty.
            raise Exception('Deque is empty')  # Raise an error if there are no elements.
        
        return self._delete_node(self._trailer._prev)  
        # Remove and return the node before the trailer (end of deque).

# Doubly Link Implementation using a Positional List
class PositionalList(_DoublyLinkedBase):
    """A sequential container that allows access and modifications using positions."""

    class Position:
        """Represents a location in the list and provides access to an element."""
        
        def __init__(self, container, node):
            """Initialize a new Position instance."""
            self._container = container  # The list this Position belongs to
            self._node = node  # The node this Position encapsulates

        def element(self):
            """Retrieve the element stored at this position."""
            return self._node._element

        def __eq__(self, other):
            """Check if two positions refer to the same node."""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Check if two positions refer to different nodes."""
            return not (self == other)

    def _validate(self, p):
        """
        Verify that p is a valid Position object and return its underlying node.

        Raises:
            TypeError: If p is not a Position instance.
            ValueError: If p is invalid or doesn't belong to this list.
        """
        if not isinstance(p, self.Position):
            raise TypeError('p must be a proper Position Type')
        if p._container is not self:
            raise ValueError('p does not belong to this Container')
        if p._node._next is None:  # Sentinel nodes or deleted nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """
        Create a Position instance for a node, or return None if it's a sentinel.

        Returns:
            A Position instance wrapping the given node, or None if it's a boundary.
        """
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        """
        Return the first position in the list, or None if the list is empty.
        """
        return self._make_position(self._header._next)

    def last(self):
        """
        Return the last position in the list, or None if the list is empty.
        """
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """
        Return the position just before position p, or None if p is the first.

        Args:
            p: A valid Position instance.
        """
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """
        Return the position just after position p, or None if p is the last.

        Args:
            p: A valid Position instance.
        """
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """
        Generate a forward iteration of the elements in the list.

        Yields:
            Elements stored in the list, one at a time.
        """
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, successor):
        """
        Insert an element between two nodes and return its new Position.

        Args:
            e: The element to insert.
            predecessor: The node before the new element.
            successor: The node after the new element.

        Returns:
            A Position instance for the new node.
        """
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """
        Add an element to the front of the list and return its Position.
        """
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """
        Add an element to the back of the list and return its Position.
        """
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """
        Insert a new element before position p and return its Position.

        Args:
            p: A valid Position before which the element is inserted.
            e: The element to add.
        """
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """
        Insert a new element after position p and return its Position.

        Args:
            p: A valid Position after which the element is inserted.
            e: The element to add.
        """
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def _delete_node(self, node):
        """
        Delete a node and return its element.

        Args:
            node: The node to delete.

        Returns:
            The element stored in the deleted node.
        """
        original = self._validate(node)
        return super()._delete_node(original)

    def replace(self, p, e):
        """
        Replace the element at position p with a new value and return the old value.

        Args:
            p: A valid Position instance.
            e: The new element to store.

        Returns:
            The element previously stored at position p.
        """
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

