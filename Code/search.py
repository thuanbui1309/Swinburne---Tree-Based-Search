import sys
from utils import *
from mapSolver import MapSolver

def main():
    filename = sys.argv[1]
    start, goals, map = parse_grid(filename=filename)

    # Create a map solver instance
    solver = MapSolver(map)

    if (len(sys.argv) == 3):
        if (sys.argv[2] == "DFS"):
            nodes, path = solver.depth_first_search(start, goals)
        elif (sys.argv[2] == "BFS"):
            nodes, path = solver.breadth_first_search(start, goals)
        elif (sys.argv[2] == "GBFS"):
            nodes, path = solver.greedy_best_first_search(start, goals)
        elif (sys.argv[2] == "ASTAR"):
            nodes, path = solver.astar(start, goals)
        elif (sys.argv[2] == "CUS1"):
            nodes, path = solver.iterative_deepening(start, goals)
        elif (sys.argv[2] == "CUS2"):
            nodes, path = solver.ida_star(start, goals)

        # Show result
        if (path != None):
            print(f"{filename} {sys.argv[2]}")
            print(f"<Node {path[-1][0]}> {nodes}")
            print([direction for cell, direction in path[:-1]])  
        else:
            print(f"{filename} {sys.argv[2]}")
            print(f"No goal is reachable; {nodes}")
    elif(len(sys.argv) == 2):
        print("hehe")

if __name__ == "__main__":
    main()