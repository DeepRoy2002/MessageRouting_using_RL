import numpy as np

def distance(node1, node2):
    x1, y1 = node1.x, node1.y
    x2, y2 = node2.x, node2.y
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def dynamic_programming(network, source, destination):
    # Create a 2D array to store the minimum distances
    distances = np.full((len(network.nodes), len(network.nodes)), np.inf)

    # Distance from the source node to itself is 0
    distances[source.id, source.id] = 0

    # Initialize the predecessor array
    predecessors = np.full((len(network.nodes), len(network.nodes)), None)

    # Fill the distances array using dynamic programming
    for k in range(len(network.nodes)):
        for i in range(len(network.nodes)):
            for j in range(len(network.nodes)):
                if distances[i, k] != np.inf and distances[k, j] != np.inf:
                    new_distance = distances[i, k] + distance(network.get_node_by_id(k), network.get_node_by_id(j))
                    if new_distance < distances[i, j]:
                        distances[i, j] = new_distance
                        predecessors[i, j] = k

    # Reconstruct the shortest path using the predecessor array
    path = []
    current_node = destination
    while current_node is not None:
        path.append(current_node)
        current_node = predecessors[source.id, current_node.id]

    return path[::-1]
