from collections import deque

# Representing the graph as an adjacency list
graph = {
    'you': ['alice', 'bob', 'claire'],
    'bob': ['anuj', 'peggy'],
    'alice': ['peggy'],
    'claire': ['thom', 'jonny'],
    'anuj': [],
    'peggy': [],
    'thom': [],
    'jonny': []
}

def search(name):
    """
    Perform a breadth-first search to find if a person in the graph is a 'mango seller'.
    
    Args:
    name (str): The starting node in the graph.
    
    Returns:
    bool: True if a mango seller is found, False otherwise.
    """
    # Check if the name exists in the graph
    if name not in graph:
        print(f"{name} is not in the graph.")
        return False

    # Create a queue for BFS and add all neighbors of the starting node
    search_queue = deque()
    search_queue += graph[name]
    
    # Set to keep track of people already searched to prevent infinite loops
    searched = set()

    # Continue while there are people in the queue
    while search_queue:
        # Get the first person in the queue
        person = search_queue.popleft()

        # If the person has not already been searched
        if person not in searched:
            # Check if the person is a mango seller
            if person_is_seller(person):
                print(f"{person} is a mango seller")
                return True
            else:
                # Add this person's neighbors to the search queue
                search_queue += graph[person]
                # Mark the person as searched
                searched.add(person)

    # Return False if no mango seller is found
    return False

def person_is_seller(name):
    """
    Determines if a person is a 'mango seller'.
    A mango seller is defined as someone whose name ends with the letter 'm'.
    
    Args:
    name (str): The name of the person to check.
    
    Returns:
    bool: True if the person is a mango seller, False otherwise.
    """
    return name[-1] == 'm'

# Example usage
search("you")  # Replace "you" with other names to test different starting points

from collections import deque

def find_shortest_path(graph, start, target):
    """
    Finds the shortest path in an unweighted graph using BFS.
    
    Args:
    graph (dict): Adjacency list representing the graph.
    start (str): The starting node.
    target (str): The target node.
    
    Returns:
    list: A list of nodes representing the shortest path, or an empty list if no path exists.
    """
    # Queue to manage BFS, initialized with the starting node and its path
    queue = deque([[start]])

    # Set to track visited nodes
    visited = set()
    
    while queue:
        # Get the first path from the queue
        path = queue.popleft()
        # Get the last node in the current path
        node = path[-1]
        
        # If the node is the target, return the path
        if node == target:
            return path
        
        # Skip if the node has already been visited
        if node not in visited:
            # Mark the node as visited
            visited.add(node)
            
            # Add paths to neighbors to the queue
            for neighbor in graph.get(node, []):
                new_path = list(path)  # Copy the current path
                new_path.append(neighbor)  # Append the neighbor to the path
                queue.append(new_path)
    
    # Return an empty list if no path is found
    return []

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
target = 'E'

# Find the shortest path
shortest_path = find_shortest_path(graph, start, target)
print("Shortest Path:", shortest_path)

from collections import deque

def find_shortest_city_path(graph, start, destination):
    # Initialize the BFS queue with the start node as the first path
    queue = deque([[start]])
    visited = set()  # Set to keep track of visited nodes to avoid cycles

    while queue:
        path = queue.popleft()  # Get the first path from the queue
        node = path[-1]  # The current node is the last element of the path

        # If we reach the destination node, return the current path
        if node == destination:
            return path

        # If the node hasn't been visited yet, visit it and explore its neighbors
        if node not in visited:
            visited.add(node)  # Mark the node as visited

            # Add all neighbors of the current node to the queue
            for neighbor in graph.get(node, []):
                new_path = list(path)  # Create a new path by copying the current one
                new_path.append(neighbor)  # Add the neighbor to the path
                queue.append(new_path)  # Enqueue the new path

    # If no path is found, return an empty list
    return []

# Example city map (graph)
graph = {
    '1': ['2', '3'],
    '2': ['1', '4', '5'],
    '3': ['1', '6'],
    '4': ['2'],
    '5': ['2', '6'],
    '6': ['3', '5']
}

start = '1'
destination = '6'

# Call the function and print the result
shortest_path = find_shortest_city_path(graph, start, destination)
print("Shortest Path:", shortest_path)


from collections import deque

def find_node_level(tree, target):
    """
    Finds the level of a target node in a tree using BFS.

    Parameters:
    - tree (dict): A dictionary representing the tree where keys are parent nodes,
                   and values are lists of child nodes.
    - target (int): The target node to find the level for.

    Returns:
    - int: The level of the target node in the tree. If the node is not found, returns -1.
    """

    # Initialize the BFS queue with the root node (1) and its level (0)
    queue = deque([(1, 0)])

    # Perform BFS until the queue is empty
    while queue:
        # Dequeue the current node and its level
        node, level = queue.popleft()

        # If the target node is found, return its level
        if node == target:
            return level

        # If the current node has children in the tree, enqueue them with their levels
        if node in tree:
            for child in tree[node]:
                queue.append((child, level + 1))  # Add each child with an incremented level

    # If the target node is not found, return -1
    return -1


# Shortest path from to cab to bat

from collections import deque

def find_shortest_path(graph, start, finish):

    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == finish:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return []

graph = {
    'cab': ['cat', 'car'],
    'cat': ['mat', 'bat'],
    'car': ['cat', 'bar'],
    'mat': ['bat'],
    'bar': ['bat'],
    'bat': []
}

start = 'cab'
finish = 'bat'

shortest_path = find_shortest_path(graph, start, finish)
print("Shortest Path:", shortest_path)


