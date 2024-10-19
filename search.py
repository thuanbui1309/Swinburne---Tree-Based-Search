import sys
from utils import *
from mapSolver import MapSolver
from map import *

def main():
    filename = sys.argv[1]
    start, goals, map = parse_grid(filename=filename)
    # print(map)

    # for line in map:
    #     print(line)

    solver = MapSolver(map, start, goals)

    if (len(sys.argv) == 3):
        if sys.argv[2] == "ALL":
            path = solver.astar_multi_goals()
            print([direction for _, direction in path[:-1]])  
        else:
            if (sys.argv[2] == "DFS"):
                nodes, path = solver.depth_first_search()
            elif (sys.argv[2] == "BFS"):
                nodes, path = solver.breadth_first_search()
            elif (sys.argv[2] == "GBFS"):
                nodes, path = solver.greedy_best_first_search()
            elif (sys.argv[2] == "AS"):
                nodes, path = solver.astar()
            elif (sys.argv[2] == "CUS1"):
                nodes, path = solver.iterative_deepening_search()
            elif (sys.argv[2] == "CUS2"):
                nodes, path = solver.ida_star()

            # Show result
            if (path != None):
                print(f"{filename} {sys.argv[2]}")
                print(f"<Node {path[-1][0]}> {nodes}")
                if len(path[:-1]) > 0:
                    print([direction for _, direction in path[:-1]])  
                else:
                    print("Already at the goal")
            else:
                print(f"{filename} {sys.argv[2]}")
                print(f"No goal is reachable; {nodes}")

    elif(len(sys.argv) == 2):
        map_viz = MapSolverVisualization(solver)
        map_viz.mainloop()

if __name__ == "__main__":
    main()