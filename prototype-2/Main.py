from dummy import create_dummy_network, NetworkEnvironment
from Routing import MessageRoutingEnv, QLearningAgent
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def visualize_network(graph):
    # Separate nodes based on their type
    machines = [node for node, data in graph.nodes(data=True) if data['type'] == 'machine']
    switches = [node for node, data in graph.nodes(data=True) if data['type'] == 'switch']
    routers = [node for node, data in graph.nodes(data=True) if data['type'] == 'router']
    servers = [node for node, data in graph.nodes(data=True) if data['type'] == 'server']
    
    plt.figure(figsize=(18,15))

    # Draw the network graph using matplotlib with different colors for each type
    pos = nx.spring_layout(graph)  # You can choose different layout algorithms
    nx.draw_networkx_nodes(graph, pos, nodelist=machines, node_color='lightblue', label='Machines')
    nx.draw_networkx_nodes(graph, pos, nodelist=switches, node_color='green', label='Switches')
    nx.draw_networkx_nodes(graph, pos, nodelist=routers, node_color='orange', label='Routers')
    nx.draw_networkx_nodes(graph, pos, nodelist=servers, node_color='yellow', label='Servers')
    nx.draw_networkx_edges(graph, pos)
    nx.draw_networkx_labels(graph, pos)

    # Display the legend
    plt.legend()

    # Display the graph
    plt.show()

def main():
    num_machines_per_switch = 9
    num_switches = 26
    num_routers = 8
    num_servers = 1

    dummy_network = create_dummy_network(num_machines_per_switch, num_switches, num_routers, num_servers)
    visualize_network(dummy_network)
    num_nodes = len(dummy_network.nodes)

    # Create the environment using the dummy network
    env = NetworkEnvironment(num_nodes)

    # Create the Q-learning agent
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

    best_path = env.episode_paths[np.argmax(agent.q_table[state, :])]
    print("Best Path:", best_path)

    # Visualize the network with the best path highlighted
    visualize_network(dummy_network, best_path)

if __name__ == "__main__":
    main()
