import os
from utils import *
from mapSolver import MapSolver
import timeit
import matplotlib.pyplot as plt
import numpy as np

# Initialize lists to store results for smaller files
algorithms = ["DFS", "BFS", "GBFS", "A*", "Custom 1 (IDS)", "Custom 2 (IDA*)"]
nodes_explored = {alg: [] for alg in algorithms}
path_lengths = {alg: [] for alg in algorithms}
execution_times = {alg: [] for alg in algorithms}
files_processed = []

txt_files = [f for f in os.listdir("Test\Performance") if f.endswith('.txt')]

for file in txt_files:
    if file == "extra_large.txt":
        continue
    
    start, goals, map = parse_grid(filename=f"Test\Performance\{file}")
    solver = MapSolver(map, start, goals)

    # DFS
    dfs_nodes, dfs_path = solver.depth_first_search()
    execution_time = timeit.timeit(lambda: solver.depth_first_search(), number=1)
    nodes_explored["DFS"].append(dfs_nodes)
    path_lengths["DFS"].append(len(dfs_path) - 1)
    execution_times["DFS"].append(execution_time)

    # BFS
    bfs_nodes, bfs_path = solver.breadth_first_search()
    execution_time = timeit.timeit(lambda: solver.breadth_first_search(), number=1)
    nodes_explored["BFS"].append(bfs_nodes)
    path_lengths["BFS"].append(len(bfs_path) - 1)
    execution_times["BFS"].append(execution_time)

    # GBFS
    gbfs_nodes, gbfs_path = solver.greedy_best_first_search()
    execution_time = timeit.timeit(lambda: solver.greedy_best_first_search(), number=1)
    nodes_explored["GBFS"].append(gbfs_nodes)
    path_lengths["GBFS"].append(len(gbfs_path) - 1)
    execution_times["GBFS"].append(execution_time)

    # A*
    astar_nodes, astar_path = solver.astar()
    execution_time = timeit.timeit(lambda: solver.astar(), number=1)
    nodes_explored["A*"].append(astar_nodes)
    path_lengths["A*"].append(len(astar_path) - 1)
    execution_times["A*"].append(execution_time)

    # Custom 1 (Iterative Deepening Search)
    cus1_nodes, cus1_path = solver.iterative_deepening_search()
    execution_time = timeit.timeit(lambda: solver.iterative_deepening_search(), number=1)
    nodes_explored["Custom 1 (IDS)"].append(cus1_nodes)
    path_lengths["Custom 1 (IDS)"].append(len(cus1_path) - 1)
    execution_times["Custom 1 (IDS)"].append(execution_time)

    # Custom 2 (IDA*)
    cus2_nodes, cus2_path = solver.ida_star()
    execution_time = timeit.timeit(lambda: solver.ida_star(), number=1)
    nodes_explored["Custom 2 (IDA*)"].append(cus2_nodes)
    path_lengths["Custom 2 (IDA*)"].append(len(cus2_path) - 1)
    execution_times["Custom 2 (IDA*)"].append(execution_time)
    
    files_processed.append(file)


bar_width = 0.15
index = np.arange(len(files_processed))

# Plot Nodes Explored
plt.figure(figsize=(12, 6))
for i, alg in enumerate(algorithms):
    plt.bar(index + i * bar_width, nodes_explored[alg], bar_width, label=alg)

plt.xlabel('Files')
plt.ylabel('Nodes Explored')
plt.title('Nodes Explored by Different Algorithms (Smaller Files)')
plt.xticks(index + bar_width * (len(algorithms) / 2), files_processed, rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Plot Path Lengths
plt.figure(figsize=(12, 6))
for i, alg in enumerate(algorithms):
    plt.bar(index + i * bar_width, path_lengths[alg], bar_width, label=alg)

plt.xlabel('Files')
plt.ylabel('Path Length')
plt.title('Path Lengths by Different Algorithms (Smaller Files)')
plt.xticks(index + bar_width * (len(algorithms) / 2), files_processed, rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Plot Execution Times
plt.figure(figsize=(12, 6))
for i, alg in enumerate(algorithms):
    plt.bar(index + i * bar_width, execution_times[alg], bar_width, label=alg)

plt.xlabel('Files')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time by Different Algorithms (Smaller Files)')
plt.xticks(index + bar_width * (len(algorithms) / 2), files_processed, rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Process and visualize extra_large.txt separately
if "extra_large.txt" in txt_files:
    start, goals, map = parse_grid(filename="extra_large.txt")
    solver = MapSolver(map, start, goals)
    
    # Store results for extra_large.txt
    large_results = {}
    large_results["DFS"] = solver.depth_first_search()
    large_results["BFS"] = solver.breadth_first_search()
    large_results["GBFS"] = solver.greedy_best_first_search()
    large_results["A*"] = solver.astar()
    large_results["Custom 1 (IDS)"] = solver.iterative_deepening_search()
    large_results["Custom 2 (IDA*)"] = solver.ida_star()

    # Visualization for extra_large.txt (nodes explored)
    plt.figure(figsize=(8, 6))
    plt.bar(algorithms, [res[0] for res in large_results.values()], color='skyblue')
    plt.xlabel('Algorithms')
    plt.ylabel('Nodes Explored')
    plt.title('Nodes Explored by Different Algorithms (extra_large.txt)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Visualization for extra_large.txt (path lengths)
    plt.figure(figsize=(8, 6))
    plt.bar(algorithms, [len(res[1]) - 1 for res in large_results.values()], color='orange')
    plt.xlabel('Algorithms')
    plt.ylabel('Path Length')
    plt.title('Path Length by Different Algorithms (extra_large.txt)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Visualization for extra_large.txt (execution times)
    execution_times_large = []
    for alg, method in large_results.items():
        execution_time = timeit.timeit(lambda: method, number=1)
        execution_times_large.append(execution_time)
    
    plt.figure(figsize=(8, 6))
    plt.bar(algorithms, execution_times_large, color='green')
    plt.xlabel('Algorithms')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time by Different Algorithms (extra_large.txt)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
