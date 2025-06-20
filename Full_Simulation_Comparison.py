import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import math

# --- Parameters ---
NUM_NODES = 30
SEARCH_RADIUS = 0.2
START_NODE = 0

# Generate same node positions 
np.random.seed(42)
pos = {i: (np.random.rand(), np.random.rand()) for i in range(NUM_NODES)}

# --- Helper ---
def distance(p1, p2):
    # Calculates euclidean distance between two points
    return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))

# --- Simulation ---
def simulation(tipe_heuristik, jdl):
    # Run a pathfinding simulation based on the given heuristic type 
    # and generate a visualization plot.

    # Variables to track status
    physically_visited = []
    radius_visited = set()
    edge_trail = []
    total_weight = 0

    curr_node = START_NODE
    
    # Main algorithm loop
    while len(physically_visited) + len(radius_visited) < NUM_NODES:
        
        if curr_node not in physically_visited and curr_node not in radius_visited:
            physically_visited.append(curr_node)

            for i in range(NUM_NODES):
                if i != curr_node and i not in physically_visited and i not in radius_visited:
                    if distance(pos[curr_node], pos[i]) < SEARCH_RADIUS:
                        radius_visited.add(i)

        all_visited_node = set(physically_visited).union(radius_visited)
        unvisited_node = [n for n in range(NUM_NODES) if n not in all_visited_node]

        if not unvisited_node:
            break

        if tipe_heuristik == 'lethal_company_style':
# Lethal Company Heuristic NN : Find the closest node from the physically visited prev node
            ref_node = physically_visited[-2] if len(physically_visited) > 1 else START_NODE
        else:
# Classic NN : Find the closest node to the curr node
            ref_node = curr_node
            
        shortest_dist = float('inf')
        next_node = -1

        for candidate_node in unvisited_node:
            dist_to_ref = distance(pos[ref_node], pos[candidate_node])
            if dist_to_ref < shortest_dist:
                shortest_dist = dist_to_ref
                next_node = candidate_node
        
        if next_node == -1:
            break
            
        edge_weight = distance(pos[curr_node], pos[next_node])
        total_weight += edge_weight
        edge_trail.append((curr_node, next_node))
        curr_node = next_node

    # --- Visualization ---
    G = nx.Graph()
    G.add_nodes_from(range(NUM_NODES))
    
    # Set node colors
    node_color = []
    for i in range(NUM_NODES):
        if i in physically_visited:
            node_color.append('skyblue')
        elif i in radius_visited:
            node_color.append('lightgreen')
        else:
            node_color.append('lightgray')

    # Create the plot
    plt.figure(figsize=(13, 13))
    plt.title(f"{jdl}\nWeight total (distance): {total_weight:.4f}", fontsize=16)

    # Draw edges and nodes
    nx.draw_networkx_edges(G, pos, alpha=0.1, edge_color='gray')
    nx.draw_networkx_nodes(G, pos, node_color=node_color, node_size=500)
    
    # Draw the path taken by the enemy
    D = nx.DiGraph()
    D.add_edges_from(edge_trail)
    nx.draw_networkx_edges(
        D, pos, 
        edge_color='red', 
        width=2.0, 
        arrows=True, 
        arrowstyle='->', 
        arrowsize=20
    )

    # Draw node labels
    node_labels = {n: str(n) for n in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels = node_labels, font_color='black', 
                            font_weight='bold', font_size=10)

    # Legenda
    element = [
        plt.Line2D([0], [0], color='skyblue', marker='o', 
                   linestyle='', markersize=10, label='Node Dikunjungi Fisik (Physically Visited)'),
        plt.Line2D([0], [0], color='lightgreen', marker='o', 
                   linestyle='', markersize=10, label='Node Dikunjungi via Radius (Radius-Visited)'),
        plt.Line2D([0], [0], color='lightgray', marker='o', 
                   linestyle='', markersize=10, label='Node Belum Dikunjungi (Unvisited)'),
        plt.Line2D([0], [0], color='red', lw=2, label='Lintasan Enemy (Path)')
    ]
    plt.legend(handles=element, loc='upper right')

    plt.xlabel("Koordinat X")
    plt.ylabel("Koordinat Y")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.axis('on')
    plt.show()
    
    return total_weight

# --- Run both simulation ---
print("MRunning simulation for Classic Nearest Neighbor (NN)...")
classic_weighted_nn = simulation('classic_nn', "Classic Nearest Neighbor (NN)")

print("\nRunning simulation for Lethal Company Heuristic Nearest Neighbor...")
heuristic_weighted_nn = simulation('lethal_company_style', "Lethal Company Heuristic Nearest Neighbor")


# --- Final comparison ---
print("\n--- TOTAL WEIGHT COMPARISON ---")
print(f"Classic Nearest Neighbor: {classic_weighted_nn:.4f}")
print(f"Lethal Company Heuristic Nearest Neighbor: {heuristic_weighted_nn:.4f}")

if classic_weighted_nn < heuristic_weighted_nn:
    print("\nKesimpulan: Heuristik Klasik NN menghasilkan lintasan yang lebih pendek (lebih optimal).")
else:
    print("\nKesimpulan: Heuristik Asli (Gaya Lethal Company) menghasilkan lintasan yang lebih pendek (lebih optimal).")