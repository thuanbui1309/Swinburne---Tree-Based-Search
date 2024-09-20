import sys
import ast
import numpy as np

from Search_Algo_Implementation.BFS import BFS

with open('RobotNav-test.txt', 'r') as file:
    "Identify grid size"
    grid_size = ast.literal_eval(file.readline())
    map = np.zeros(grid_size, dtype=int)

    "Identify intial state"
    starts = ast.literal_eval(file.readline())
    map[starts[1], starts[0]] = -1

    "Identify goals"
    goals = file.readline().strip().split(' | ')
    for goal in goals:
        goal = ast.literal_eval(goal)
        map[goal[1], goal[0]] = 1

    "Identify walls"
    for line in file:
        line = ast.literal_eval(line.strip())
        for i in range(line[3]):
            pass

        print(line.strip())

print(map)