def dfs_tree(root, target, start):
    # Initialize a stack with the starting node (1 in this case).
    # Using a stack instead of a queue is the only difference between BFS and DFS.
    # Using a stack to implement DFS means that the last node added to the stack is the first one to be processed.
    stack = [start]

    while stack:
        # Pop a node from the stack
        node = stack.pop()

        # Check if the current node is the target
        if node == target:
            return True

        # Add all children of the current node to the stack
        for child in root.get(node, []):
            stack.append(child)

    # Return False if the target is not found
    return False

root = {1: [2, 3],
        2: [4, 5],
        3: [6],
        4: [],
        5: [],
        6: []}
target = 6
start = 1

print(dfs_tree(root, target, start))  # Output: True
