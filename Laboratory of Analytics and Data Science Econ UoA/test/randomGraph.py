import networkx as nx
import matplotlib.pyplot as plt

# Create a random graph with 20 nodes
G = nx.random_geometric_graph(20, 0.2)

# Customize node and edge styles (optional)
pos = nx.spring_layout(G)  # Node positions
node_colors = ['lightblue' for _ in G.nodes]  # Set node colors

# Draw the graph
nx.draw(G, pos, node_color=node_colors, with_labels=True)

# Save as PNG image
plt.savefig("graph_banner.png")
plt.close()
