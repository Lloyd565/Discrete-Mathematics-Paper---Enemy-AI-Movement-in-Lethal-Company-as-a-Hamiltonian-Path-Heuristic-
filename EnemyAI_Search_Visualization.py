import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math

# --- Parameters ---
NUM_NODES = 30
SEARCH_RADIUS = 0.2
START_NODE = 0

# Generate node positions
np.random.seed(42)
pos = {i: (np.random.rand(), np.random.rand()) for i in range(NUM_NODES)}

# Using Euclidean distance (for simplicity)
def distance(p1, p2):
    return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))

# Initialize tracking variables
physically_visited = []
radius_visited = set()
path_edges = []

# Nearest Neigbor Heuristic Algorithm
curr_node = START_NODE
prev_node_for_ref = START_NODE

while len(physically_visited) + len(radius_visited) < NUM_NODES:
    # 1. Node visited physicallt
    if curr_node not in physically_visited and curr_node not in radius_visited:
        physically_visited.append(curr_node)

        # 2. Mark the surrounding nodes (nodes within the search radius) as radius_visited
        for i in range(NUM_NODES):
            if i != curr_node and i not in physically_visited and i not in radius_visited:
                if distance(pos[curr_node], pos[i]) < SEARCH_RADIUS:
                    radius_visited.add(i)

    # 3. Next node
    all_visited_nodes = set(physically_visited).union(radius_visited)
    unvisited_nodes = [n for n in range(NUM_NODES) if n not in all_visited_nodes]

    if not unvisited_nodes:
        break 

    # Heuristic in lethal company: Find the node closest to the previous visited node
    # On the first real move, the reference is the start node itself.
    if len(physically_visited) > 1:
        prev_node_for_ref = physically_visited[-2]

    min_dist = float('inf')
    next_node = -1

    for node in unvisited_nodes:
        dist_to_ref = distance(pos[prev_node_for_ref], pos[node])
        if dist_to_ref < min_dist:
            min_dist = dist_to_ref
            next_node = node
            
    if next_node == -1:
        break

    # 4. Add the edge to the path and update the current node
    path_edges.append((curr_node, next_node))
    curr_node = next_node

# --- Visualization ---
G = nx.Graph()
for i in range(NUM_NODES):
    G.add_node(i)

# Set node colors
node_colors = []
for i in range(NUM_NODES):
    if i in physically_visited:
        node_colors.append('skyblue') # Blue for physicaly visited
    elif i in radius_visited:
        node_colors.append('lightgreen') # Green for radius visited
    else:
        node_colors.append('lightgray') # Gray for unvisited node

# Create the plot
plt.figure(figsize=(12, 12))
plt.title("Visualisasi Lintasan Hamiltonian dengan Heuristik & Radius Presisi (Tanpa Urutan)")

nx.draw_networkx_edges(G, pos, alpha=0.1, edge_color='gray')

# Draw the nodes
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=500)

# Draw the path taken by the enemy
D = nx.DiGraph()
D.add_edges_from(path_edges)
nx.draw_networkx_edges(
    D,
    pos,
    edge_color='red',
    width=2.0,
    arrows=True,
    arrowstyle='->',
    arrowsize=20
)

# Draw node labels
node_labels = {n: str(n) for n in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=node_labels, font_color='black', font_weight='bold', font_size=10)

# Legenda
plt.scatter([], [], c='skyblue', label='Node Dikunjungi Fisik (Physically Visited)')
plt.scatter([], [], c='lightgreen', label='Node Dikunjungi via Radius (Radius-Visited)')
plt.scatter([], [], c='lightgray', label='Node Tidak Dikunjungi (Unvisited)')
plt.plot([], [], 'r-', label='Lintasan Enemy (Path)')
plt.legend(loc='upper right')

plt.xlabel("Koordinat X")
plt.ylabel("Koordinat Y")
plt.grid(True, linestyle='--', alpha=0.5)
plt.axis('on')
plt.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
plt.show()