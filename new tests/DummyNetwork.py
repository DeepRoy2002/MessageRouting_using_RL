import random
class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)


class Network:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def get_node_by_id(self, id):
        for node in self.nodes:
            if node.id == id:
                return node
        return None


# Create a dummy network with 10 nodes
network = Network()

for i in range(10):
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    node = Node(i, x, y)
    network.add_node(node)

# Create links between all nodes
for i in range(10):
    for j in range(i + 1, 10):
        network.get_node_by_id(i).add_neighbor(network.get_node_by_id(j))

