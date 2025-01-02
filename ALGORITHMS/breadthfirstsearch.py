# from collections import deque

# # Representing the graph as an adjacency list
# graph = {}
# graph['you'] = ['alice', 'bob', 'claire']
# graph['bob'] = ['anuj', 'peggy']
# graph['alice'] = ['peggy']
# graph['claire'] = ['thom', 'jonny']
# graph['anuj'] = []
# graph['peggy'] = []
# graph['thom'] = []
# graph['jonny'] = []

# def search(name):
#     """
#     Perform a breadth-first search to find if a person in the graph is a 'mango seller'.
    
#     Args:
#     name (str): The starting node in the graph.
    
#     Returns:
#     bool: True if a mango seller is found, False otherwise.
#     """
#     # Check if the name exists in the graph
#     if name not in graph:
#         print(f"{name} is not in the graph.")
#         return False

#     # Create a queue for BFS and add all neighbors of the starting node
#     search_queue = deque()
#     search_queue += graph[name]
    
#     # Set to keep track of people already searched to prevent infinite loops
#     searched = set()

#     # Continue while there are people in the queue
#     while search_queue:
#         # Get the first person in the queue
#         person = search_queue.popleft()

#         # If the person has not already been searched
#         if person not in searched:
#             # Check if the person is a mango seller
#             if person_is_seller(person):
#                 print(f"{person} is a mango seller")
#                 return True
#             else:
#                 # Add this person's neighbors to the search queue
#                 search_queue += graph[person]
#                 # Mark the person as searched
#                 searched.add(person)

#     # Return False if no mango seller is found
#     return False

# def person_is_seller(name):
#     """
#     Determines if a person is a 'mango seller'.
#     A mango seller is defined as someone whose name ends with the letter 'm'.
    
#     Args:
#     name (str): The name of the person to check.
    
#     Returns:
#     bool: True if the person is a mango seller, False otherwise.
#     """
#     return name[-1] == 'm'

# # Example usage
# search("you")  # Replace "you" with other names to test different starting points

# from collections import deque

# def find_shortest_path(graph, start, target):
#     """
#     Finds the shortest path in an unweighted graph using BFS.
    
#     Args:
#     graph (dict): Adjacency list representing the graph.
#     start (str): The starting node.
#     target (str): The target node.
    
#     Returns:
#     list: A list of nodes representing the shortest path, or an empty list if no path exists.
#     """
#     # Queue to manage BFS, initialized with the starting node and its path
#     queue = deque([[start]])
    
#     # Set to track visited nodes
#     visited = set()
    
#     while queue:
#         # Get the first path from the queue
#         path = queue.popleft()
#         # Get the last node in the current path
#         node = path[-1]
        
#         # If the node is the target, return the path
#         if node == target:
#             return path
        
#         # Skip if the node has already been visited
#         if node not in visited:
#             # Mark the node as visited
#             visited.add(node)
            
#             # Add paths to neighbors to the queue
#             for neighbor in graph.get(node, []):
#                 new_path = list(path)  # Copy the current path
#                 new_path.append(neighbor)  # Append the neighbor to the path
#                 queue.append(new_path)
    
#     # Return an empty list if no path is found
#     return []

# # Example usage
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

# start = 'A'
# target = 'E'

# # Find the shortest path
# shortest_path = find_shortest_path(graph, start, target)
# print("Shortest Path:", shortest_path)

from collections import deque

def find_shortest_city_path(graph, start, destination):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == destination:
            return path
        
        if node not in visited:
            visited.add(node)

            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return []

graph = {
    '1': ['2', '3'],
    '2': ['1', '4', '5'],
    '3': ['1', '6'],
    '4': ['2'],
    '5': ['2', '6'],
    '6': ['3', '5']
}

start = '4'
destination = '5'

shortest_path = find_shortest_city_path(graph, start, destination)
print("Shortest Path:", shortest_path)

from collections import deque

def find_node_level(tree, target):

    queue = deque([(1, 0)])

    while queue:
        node, level = queue.popleft()
        
        if node == target:
            return level
        
        if node in tree:
            for child in tree[node]:
                queue.append(child, level + 1)

    return -1

    


