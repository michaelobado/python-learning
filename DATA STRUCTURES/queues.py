# A queue is a collection of objects that are inserted 
# and removed according to the first-in, first-out (FIFO) principle. 
# That is, elements can be inserted at any time, but only the element that has been in the queue the longest can be next removed.

# Here’s a list of common queue operations, essential for managing data in a First-In-First-Out (FIFO) order:

# 1. **Enqueue**: Adds an element to the end of the queue.
#    - **Time Complexity**: \(O(1)\)

# 2. **Dequeue**: Removes the element from the front of the queue and returns it. Raises an error if the queue is empty.
#    - **Time Complexity**: \(O(1)\)

# 3. **Front/First/Peek**: Returns the element at the front of the queue without removing it.
#    - **Time Complexity**: \(O(1)\)

# 4. **isEmpty**: Checks if the queue is empty and returns `True` if it is; otherwise, it returns `False`.
#    - **Time Complexity**: \(O(1)\)

# 5. **isFull** (for fixed-size queues): Checks if the queue has reached its maximum capacity.
#    - **Time Complexity**: \(O(1)\)

# 6. **Size/Len**: Returns the number of elements currently in the queue.
#    - **Time Complexity**: \(O(1)\)

class Empty(Exception):
    pass

class ArrayQueue:
    # Set a default capacity for the queue to prevent frequent resizing
    DEFAULT_CAPACITY = 10

    def __init__(self):
        # Initializes an empty queue with a fixed-size list of default capacity
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        # Tracks the current number of elements in the queue
        self._size = 0
        # Keeps track of the front index of the queue
        self._front = 0

    def __len__(self):
        # Returns the current number of elements in the queue
        return self._size
    
    def _is_empty(self):
        # Checks if the queue is empty
        return self._size == 0
    
    def first(self):
        # Returns the front element in the queue without dequeuing it
        if self._is_empty():
            raise Empty('The queue is empty')
        return self._data[self._front]
    
    def dequeue(self):
        # Removes and returns the front element of the queue
        if self._is_empty():
            raise Exception('The queue is empty')
        
        answer = self._data[self._front]
        # Clear the front element to avoid loitering
        self._data[self._front] = None
        # Update the front index using modular arithmetic for circular behavior
        self._front = (self._front + 1) % len(self._data)
        # Reduce the size counter as an element is removed
        self._size -= 1

        # Check if the array can be resized down to save memory
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)

        return answer
    
    def enqueue(self, e):
        # Adds a new element to the end of the queue
        if self._size == len(self._data):
            # Double the array size if the queue is full
            self._resize(2 * len(self._data))

        # Calculate the next available index for the new element
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        # Increment the size counter
        self._size += 1

    def _resize(self, cap):
        # Resizes the underlying array to a new capacity 'cap'
        old = self._data
        # Create a new array of the specified capacity
        self._data = [None] * cap
        # Start from the front element and shift all elements to the new array
        walk = self._front

        # Copy elements to the new list in a consecutive order
        for k in range(self._size):
            self._data[k] = old[walk]
            # Use modular arithmetic to wrap around if needed
            walk = (walk + 1) % len(old)

        # Reset the front index to the start of the new array
        self._front = 0

letsQueue = ArrayQueue()
letsQueue.enqueue(5)
letsQueue.enqueue(13)
letsQueue.enqueue(26)
letsQueue.enqueue(40)
print(letsQueue.first())
print(letsQueue._is_empty())
print(letsQueue.dequeue())
print(letsQueue.dequeue())
print(letsQueue.first())



