import math

graph = {
    'start': {'a': 6, 'b': 2},
    'a': {'finish': 1},
    'b': {'a': 3, 'finish': 5},
    'finish': {}
}

infinity = math.inf

costs = {
    'a': 6,
    'b': 2,
    'finish': infinity
}

parents = {
    'a': 'start',
    'b': 'start',
    'finish': None
}

processed = set()

def find_lowest_cost_node(costs): 
    lowest_cost = math.inf
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]

    for n in neighbors.keys():
        new_cost = cost + neighbors[n] 
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    
    processed.add(node)
    node = find_lowest_cost_node(costs)
