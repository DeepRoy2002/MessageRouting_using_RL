import networkx as nx
import random
from routing_env import QLearningAgent

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

    
    
from routing_env import QLearningAgent
env = NetworkEnvironment(num_nodes=10)
agent = QLearningAgent(env.num_nodes)

for episode in range(1000):
    state, target_node = env.reset()
    total_reward = 0

    while True:
        action = agent.select_action(state)
        next_state, reward = env.step(action)
        agent.update_q_table(state, action, reward, next_state)
        state = next_state
        total_reward += reward

        if state == target_node:
            break

    print(f"Episode: {episode}, Total Reward: {total_reward}")

env.close()



import networkx as nx
import random

def create_dummy_network(num_nodes, edge_probability):
    # Create an empty graph
    graph = nx.Graph()

    # Add nodes
    graph.add_nodes_from(range(num_nodes))

    # Add random edges based on the edge_probability
    for node1 in graph.nodes:
        for node2 in graph.nodes:
            if node1 != node2 and random.random() < edge_probability:
                graph.add_edge(node1, node2)

    return graph

# Usage:
num_nodes = 10  # Adjust this based on your project's requirements
edge_probability = 0.2  # Adjust this to control the network density
network_graph = create_dummy_network(num_nodes, edge_probability)
