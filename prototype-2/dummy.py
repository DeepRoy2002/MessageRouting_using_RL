import networkx as nx
import random

class NetworkEnvironment:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.graph = self.create_network(num_nodes)
        self.state = None
        self.target_node = None

    def create_network(self, num_nodes):
        # Create a random network graph with nodes and edges
        graph = nx.erdos_renyi_graph(num_nodes, 0.2)
        return graph

    def reset(self):
        # Reset the environment for a new episode
        self.state = random.randint(0, self.num_nodes - 1)
        self.target_node = random.randint(0, self.num_nodes - 1)
        return self.state, self.target_node

    def step(self, action):
        # Simulate message routing based on the action
        reward = 1 if action == self.target_node else 0
        self.state = action
        return self.state, reward

    def get_neighbors(self, node):
        # Get neighbors of a given node
        return list(self.graph.neighbors(node))

def create_dummy_network(num_machines_per_switch, num_switches, num_routers, num_servers):
    # Create an empty graph
    graph = nx.Graph()

    # Add machine nodes with the 'type' attribute set to 'machine'
    machine_nodes = range(1, num_machines_per_switch * num_switches + 1)
    graph.add_nodes_from(machine_nodes, type='machine')

    # Add switch nodes with the 'type' attribute set to 'switch'
    switch_nodes = range(num_machines_per_switch * num_switches + 1, num_machines_per_switch * num_switches + num_switches + 1)
    graph.add_nodes_from(switch_nodes, type='switch')

    # Add router nodes with the 'type' attribute set to 'router'
    router_nodes = range(num_machines_per_switch * num_switches + num_switches + 1, num_machines_per_switch * num_switches + num_switches + num_routers + 1)
    graph.add_nodes_from(router_nodes, type='router')

    # Add server nodes with the 'type' attribute set to 'server'
    server_nodes = range(num_machines_per_switch * num_switches + num_switches + num_routers + 1,
                         num_machines_per_switch * num_switches + num_switches + num_routers + num_servers + 1)
    graph.add_nodes_from(server_nodes, type='server')

    # Connect machines to switches
    for machine_node in machine_nodes:
        switch_node = random.choice(switch_nodes)
        graph.add_edge(machine_node, switch_node)

    # Connect switches to routers
    for switch_node in switch_nodes:
        router_node = random.choice(router_nodes)
        graph.add_edge(switch_node, router_node)

    # Connect routers to servers
    for router_node in router_nodes:
        server_node = random.choice(server_nodes)
        graph.add_edge(router_node, server_node)

    return graph

# Usage:
#num_nodes = 10  # Adjust this based on your project's requirements
#edge_probability = 0.2  # Adjust this to control the network density
#network_graph = create_dummy_network(num_nodes, edge_probability)
