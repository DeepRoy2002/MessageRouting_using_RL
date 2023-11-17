from DummyNetwork import network
from RoutingAlgo import dynamic_programming

# Get the source and destination nodes
source_id = 0
destination_id = 9

# Route the message
path = dynamic_programming(network, network.get_node_by_id(source_id), network.get_node_by_id(destination_id))

# Print the path
print(path)
