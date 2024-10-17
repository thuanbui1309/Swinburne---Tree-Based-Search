import unittest
from mapSolver import MapSolver
from utils import parse_grid

class TestMapSolver(unittest.TestCase):

    def setUp(self):
        self.small_map_start, self.small_goals, self.small_map = parse_grid("Test/small_map.txt")
        self.medium_map_start, self.medium_goals, self.medium_map = parse_grid("Test/medium_map.txt")
        self.large_map_start, self.large_goals, self.large_map = parse_grid("Test/large_map.txt")
        self.blocked_map_start, self.blocked_goals, self.blocked_map = parse_grid("Test/none_goal.txt")
        self.already_at_goal_start, self.already_at_goal_goals, self.already_at_goal_map = parse_grid("Test/already_at_goal.txt")
        self.find_all_goal_start, self.find_all_goal_goals, self.find_all_goal_map = parse_grid("Test/find_all_goal.txt")
        self.not_all_goal_start, self.not_all_goal_goals, self.not_all_goal_map = parse_grid("Test/not_all_goal.txt")

        self.small_solver = MapSolver(self.small_map, self.small_map_start, self.small_goals)
        self.medium_solver = MapSolver(self.medium_map, self.medium_map_start, self.medium_goals)
        self.large_solver = MapSolver(self.large_map, self.large_map_start, self.large_goals)
        self.blocked_solver = MapSolver(self.blocked_map, self.blocked_map_start, self.blocked_goals)
        self.already_at_goal_solver = MapSolver(self.already_at_goal_map, self.already_at_goal_start, self.already_at_goal_goals)
        self.find_all_goal_solver = MapSolver(self.find_all_goal_map, self.find_all_goal_start, self.find_all_goal_goals)
        self.not_all_goal_solver = MapSolver(self.not_all_goal_map, self.not_all_goal_start, self.not_all_goal_goals)
        
    def test_identifyStartPoint_returnsCorrectStartPoint(self):
        # Test if start point is accurately retrived
        self.assertEqual(self.small_map_start, (0,0))
        self.assertEqual(self.medium_map_start, (0,7))
        self.assertEqual(self.large_map_start, (0,9))

    def test_identifyGoals_returnsCorrectGoals(self):
        # Test if goals are accurately retrived
        self.assertEqual(self.small_goals, set([(5,1), (5,3)]))
        self.assertEqual(self.medium_goals, set([(7,7), (10,2)]))
        self.assertEqual(self.large_goals, set([(11,0), (15,0), (18, 5), (19, 19)]))

    def test_identifyWalls_returnsCorrectWalls(self):
        # Correct wall indexes
        small_walls_index = [(1, 0), (1, 1), (1, 3), (2, 0), (2, 1), (2, 3)]
        medium_walls_index = [(0, 1), (1, 1), (1, 4), (1, 7), (1, 8), (1, 9), (2, 1), (2, 4), (2, 5), (2, 9), (3, 1), (3, 4), (3, 5), (3, 9), (4, 4), (4, 7), (4, 8), (4, 9), (5, 1), (5, 2), (5, 3), (5, 4), (6, 6), (6, 10), (7, 1), (7, 6), (7, 10)]
        large_walls_index = [(0, 10), (0, 14), (0, 19), (1, 1), (1, 2), (1, 7), (1, 8), (1, 9), (1, 10), (1, 14), (1, 15), (1, 19), (2, 1), (2, 2), (2, 4), (2, 7), (2, 8), (2, 9), (2, 10), (2, 12), (2, 13), (2, 14), (2, 15), (2, 17), (3, 1), (3, 2), (3, 4), (3, 7), (3, 8), (3, 9), (3, 10), (3, 12), (3, 13), (3, 14), (3, 15), (3, 17), (4, 1), (4, 2), (4, 4), (4, 7), (4, 8), (4, 9), (4, 10), (4, 12), (4, 13), (4, 14), (4, 15), (4, 17), (5, 1), (5, 2), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 10), (5, 12), (5, 13), (5, 14), (5, 15), (5, 17), (5, 19), (6, 1), (6, 2), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 10), (6, 14), (6, 17), (6, 19), (7, 2), (7, 4), (7, 6), (7, 8), (7, 10), (7, 14), (7, 19), (8, 2), (8, 4), (8, 6), (8, 8), (8, 10), (8, 11), (8, 12), (8, 14), (8, 19), (9, 2), (9, 4), (9, 6), (9, 10), (9, 11), (9, 12), (9, 14), (9, 16), (9, 17), (9, 19), (10, 2), (10, 6), (10, 10), (10, 11), (10, 12), (10, 14), (10, 16), (10, 17), (10, 19), (11, 2), (11, 10), (11, 11), (11, 12), (11, 14), (11, 16), (11, 17), (11, 18), (11, 19), (12, 8), (12, 10), (12, 11), (12, 12), (12, 14), (12, 16), (12, 17), (12, 18), (12, 19), (13, 2), (13, 4), (13, 5), (13, 7), (13, 8), (13, 11), (13, 14), (13, 16), (13, 17), (14, 1), (14, 2), (14, 4), (14, 5), (14, 7), (14, 8), (14, 11), (14, 14), (14, 16), (14, 17), (15, 1), (15, 2), (15, 4), (15, 5), (15, 7), (15, 8), (16, 1), (16, 5), (16, 8), (16, 10), (16, 14), (16, 16), (16, 18), (16, 19), (17, 1), (17, 5), (17, 8), (17, 10), (17, 11), (17, 12), (17, 14), (17, 16), (17, 18), (17, 19), (18, 5), (18, 7), (18, 8), (18, 10), (18, 11), (18, 12), (18, 14), (18, 16), (19, 7), (19, 8), (19, 10), (19, 11), (19, 12), (19, 16)]

        # Test walls
        for index in small_walls_index:
            cell = self.small_map[index[0]][index[1]]
            self.assertEqual(cell, 1)

        for index in medium_walls_index:
            cell = self.medium_map[index[0]][index[1]]
            self.assertEqual(cell, 1)

        for index in large_walls_index:
            cell = self.large_map[index[0]][index[1]]
            self.assertEqual(cell, 1)

    def test_parseGrid_returnsCorrectGrid(self):
        # Test if map is accurately retrived
        accurate_small_map = [[0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 0, 0], [1, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0]]
        accurate_medium_map = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0]]
        accurate_large_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1], [0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1], [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1], [0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0], [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0], [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1], [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0]]
        
        self.assertEqual(self.small_map, accurate_small_map)
        self.assertEqual(self.medium_map, accurate_medium_map)
        self.assertEqual(self.large_map, accurate_large_map)

    def test_solvingMap_ReturnCorrectPath(self):
        # Test if the map solver accurately solves the map in small scale
        dfs_small_path = [direction for _, direction in self.small_solver.depth_first_search()[1][:-1]]
        bfs_small_path = [direction for _, direction in self.small_solver.breadth_first_search()[1][:-1]]
        gbfs_small_path = [direction for _, direction in self.small_solver.greedy_best_first_search()[1][:-1]]
        astar_small_path = [direction for _, direction in self.small_solver.astar()[1][:-1]]
        cus1_small_path = [direction for _, direction in self.small_solver.iterative_deepening_search()[1][:-1]]
        cus2_small_path = [direction for _, direction in self.small_solver.ida_star()[1][:-1]]

        dfs_medium_path = [direction for _, direction in self.medium_solver.depth_first_search()[1][:-1]]
        bfs_medium_path = [direction for _, direction in self.medium_solver.breadth_first_search()[1][:-1]]
        gbfs_medium_path = [direction for _, direction in self.medium_solver.greedy_best_first_search()[1][:-1]]
        astar_medium_path = [direction for _, direction in self.medium_solver.astar()[1][:-1]]
        cus1_medium_path = [direction for _, direction in self.medium_solver.iterative_deepening_search()[1][:-1]]
        cus2_medium_path = [direction for _, direction in self.medium_solver.ida_star()[1][:-1]]

        dfs_large_path = [direction for _, direction in self.large_solver.depth_first_search()[1][:-1]]
        bfs_large_path = [direction for _, direction in self.large_solver.breadth_first_search()[1][:-1]]
        gbfs_large_path = [direction for _, direction in self.large_solver.greedy_best_first_search()[1][:-1]]
        astar_large_path = [direction for _, direction in self.large_solver.astar()[1][:-1]]
        cus1_large_path = [direction for _, direction in self.large_solver.iterative_deepening_search()[1][:-1]]
        cus2_large_path = [direction for _, direction in self.large_solver.ida_star()[1][:-1]]

        # Accurate path
        dfs_small_accurate_path = ['right', 'right', 'down', 'down', 'down', 'right', 'right', 'up', 'up', 'up', 'right', 'down']
        bfs_small_accurate_path = ['right', 'right', 'right', 'right', 'down', 'right']
        gbfs_small_accurate_path = ['right', 'right', 'right', 'right', 'down', 'right']
        astar_small_accurate_path = ['right', 'right', 'right', 'right', 'down', 'right']
        cus1_small_accurate_path = ['right', 'right', 'right', 'right', 'down', 'right']
        cus2_small_accurate_path = ['right', 'right', 'right', 'right', 'down', 'right']

        dfs_accurate_medium_path = ['up', 'up', 'up', 'right', 'right', 'up', 'up', 'up', 'up', 'right', 'right', 'right', 'down', 'right', 'up', 'right', 'right', 'right', 'right', 'down', 'down']
        bfs_accurate_medium_path = ['up', 'right', 'right', 'right', 'right', 'right', 'up', 'right', 'right', 'down', 'down']
        gbfs_accurate_medium_path = ['up', 'right', 'right', 'down', 'right', 'right', 'right', 'up', 'up', 'right', 'right', 'down', 'down']
        astar_accurate_medium_path = ['up', 'right', 'right', 'right', 'right', 'right', 'up', 'right', 'right', 'down', 'down']
        cus1_accurate_medium_path = ['up', 'right', 'right', 'down', 'right', 'up', 'right', 'down', 'right', 'up', 'up', 'right', 'right', 'down', 'down']
        cus2_accurate_medium_path = ['up', 'right', 'right', 'down', 'right', 'up', 'right', 'down', 'right', 'up', 'up', 'right', 'right', 'down', 'down']

        dfs_accurate_large_path = ['up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'right', 'right', 'right', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'left', 'left', 'up', 'up', 'left', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'right', 'up', 'right', 'up', 'up', 'right', 'down', 'down', 'down', 'right', 'right', 'right', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'right', 'up', 'up', 'right', 'down', 'down', 'right', 'down', 'down', 'down', 'down', 'right', 'right', 'down', 'right', 'up', 'up', 'up', 'right', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'left', 'left', 'up', 'up', 'up', 'up', 'up', 'up']
        bfs_accurate_large_path = ['down', 'down', 'down', 'right', 'right', 'right', 'up', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'down', 'down', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'down', 'down', 'right', 'right']
        gbfs_accurate_large_path = ['up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'left', 'left', 'left', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'right', 'right', 'down', 'right', 'right', 'up', 'up', 'right', 'right', 'down', 'down', 'down', 'down', 'right', 'down', 'down', 'right', 'down', 'right', 'right', 'down', 'down', 'down', 'right', 'right', 'up', 'up', 'up', 'up', 'right', 'right', 'down', 'down', 'down', 'down', 'right', 'right']
        astar_accurate_large_path = ['right', 'down', 'down', 'down', 'right', 'right', 'up', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'right', 'down', 'down', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'down', 'down', 'right', 'right']
        cus1_accurate_large_path = ['up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'right', 'right', 'right', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'left', 'left', 'up', 'up', 'left', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'right', 'up', 'right', 'up', 'up', 'right', 'down', 'down', 'down', 'right', 'right', 'right', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'right', 'up', 'up', 'right', 'down', 'down', 'right', 'down', 'down', 'down', 'down', 'right', 'right', 'down', 'right', 'up', 'up', 'up', 'right', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'left', 'left', 'up', 'up', 'up', 'up', 'up', 'up']
        cus2_accurate_large_path = ['up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'right', 'right', 'right', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'right', 'up', 'up', 'right', 'down', 'down', 'right', 'up', 'right', 'up', 'up', 'right', 'down', 'down', 'right', 'down', 'down', 'down', 'down', 'right', 'right', 'down', 'right', 'up', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'down', 'down', 'right', 'right']

        # Perform test
        # Small map test
        self.assertEqual(dfs_small_path, dfs_small_accurate_path)
        self.assertEqual(bfs_small_path, bfs_small_accurate_path)
        self.assertEqual(gbfs_small_path, gbfs_small_accurate_path)
        self.assertEqual(astar_small_path, astar_small_accurate_path)
        self.assertEqual(cus1_small_path, cus1_small_accurate_path)
        self.assertEqual(cus2_small_path, cus2_small_accurate_path)

        # Medium map test
        self.assertEqual(dfs_medium_path, dfs_accurate_medium_path)
        self.assertEqual(bfs_medium_path, bfs_accurate_medium_path)
        self.assertEqual(gbfs_medium_path, gbfs_accurate_medium_path)
        self.assertEqual(astar_medium_path, astar_accurate_medium_path)
        self.assertEqual(cus1_medium_path, cus1_accurate_medium_path)
        self.assertEqual(cus2_medium_path, cus2_accurate_medium_path)

        # Large map test
        self.assertEqual(dfs_large_path, dfs_accurate_large_path)
        self.assertEqual(bfs_large_path, bfs_accurate_large_path)
        self.assertEqual(gbfs_large_path, gbfs_accurate_large_path)
        self.assertEqual(astar_large_path, astar_accurate_large_path)
        self.assertEqual(cus1_large_path, cus1_accurate_large_path)
        self.assertEqual(cus2_large_path, cus2_accurate_large_path)

    def test_alreadyAtGoal_ReturnCorrectMessage(self):
        _, dfs_path = self.already_at_goal_solver.depth_first_search()
        _, bfs_path = self.already_at_goal_solver.breadth_first_search()
        _, gbfs_path = self.already_at_goal_solver.greedy_best_first_search()
        _, astar_path = self.already_at_goal_solver.astar()
        # _, cus1_path = self.already_at_goal_solver.iterative_deepening_search()
        _, cus2_path = self.already_at_goal_solver.ida_star()

        self.assertEqual(len(dfs_path[:-1]), 0)
        self.assertEqual(len(bfs_path[:-1]), 0)
        self.assertEqual(len(gbfs_path[:-1]), 0)
        self.assertEqual(len(astar_path[:-1]), 0)
        # self.assertEqual(len(cus1_path[:-1]), 0)
        self.assertEqual(len(cus2_path[:-1]), 0)

    def test_UnreachableGoal_ReturnCorrectMessage(self):
        # Test if the map solver accurately returns the message when the goal is unreachable
        _, dfs_path = self.blocked_solver.depth_first_search()
        _, bfs_path = self.blocked_solver.breadth_first_search()
        _, gbfs_path = self.blocked_solver.greedy_best_first_search()
        _, astar_path = self.blocked_solver.astar()
        _, cus1_path = self.blocked_solver.iterative_deepening_search()
        _, cus2_path = self.blocked_solver.ida_star()

        self.assertIsNone(dfs_path)
        self.assertIsNone(bfs_path)
        self.assertIsNone(gbfs_path)
        self.assertIsNone(astar_path)
        self.assertIsNone(cus1_path)
        self.assertIsNone(cus2_path)

    def test_findAllGoals_ReturnCorrectMessage(self):
        # Test if the map solver accurately returns the message when there are multiple goals
        full_path = [direction for _, direction in self.find_all_goal_solver.astar_multi_goals()[:-1]]
        accurate_full_path = ['down', 'down', 'down', 'right', 'right', 'right', 'up', 'up', 'up', 'left', 'right', 'right', 'right', 'up', 'right', 'right', 'down', 'down', 'down', 'down', 'down', 'left', 'left', 'up', 'up']

        self.assertEqual(full_path, accurate_full_path)

    def test_cantReachAllGoals_ReturnCorrectMessage(self):
        # Test if the map solver accurately returns the message when there are multiple goals
        full_path = self.not_all_goal_solver.astar_multi_goals()
        self.assertIsNone(full_path)

    def test_correctNodesTraversed_ReturnCorrectResult(self):
        # Test if the map solver accurately returns the number of nodes traversed
        dfs_small_nodes = self.small_solver.depth_first_search()[0]
        bfs_small_nodes = self.small_solver.breadth_first_search()[0]
        gbfs_small_nodes = self.small_solver.greedy_best_first_search()[0]
        astar_small_nodes = self.small_solver.astar()[0]
        cus1_small_nodes = self.small_solver.iterative_deepening_search()[0]
        cus2_small_nodes = self.small_solver.ida_star()[0]

        dfs_medium_nodes = self.medium_solver.depth_first_search()[0]
        bfs_medium_nodes = self.medium_solver.breadth_first_search()[0]
        gbfs_medium_nodes = self.medium_solver.greedy_best_first_search()[0]
        astar_medium_nodes = self.medium_solver.astar()[0]
        cus1_medium_nodes = self.medium_solver.iterative_deepening_search()[0]
        cus2_medium_nodes = self.medium_solver.ida_star()[0]

        dfs_large_nodes = self.large_solver.depth_first_search()[0]
        bfs_large_nodes = self.large_solver.breadth_first_search()[0]
        gbfs_large_nodes = self.large_solver.greedy_best_first_search()[0]
        astar_large_nodes = self.large_solver.astar()[0]
        cus1_large_nodes = self.large_solver.iterative_deepening_search()[0]
        cus2_large_nodes = self.large_solver.ida_star()[0]

        # Perform test
        self.assertEqual(dfs_small_nodes, 18)
        self.assertEqual(bfs_small_nodes, 17)
        self.assertEqual(gbfs_small_nodes, 11)
        self.assertEqual(astar_small_nodes, 11)
        self.assertEqual(cus1_small_nodes, 13)
        self.assertEqual(cus2_small_nodes, 11)

        self.assertEqual(dfs_medium_nodes, 34)
        self.assertEqual(bfs_medium_nodes, 46)
        self.assertEqual(gbfs_medium_nodes, 21)
        self.assertEqual(astar_medium_nodes, 26)
        self.assertEqual(cus1_medium_nodes, 47)
        self.assertEqual(cus2_medium_nodes, 34)

        self.assertEqual(dfs_large_nodes, 138)
        self.assertEqual(bfs_large_nodes, 182)
        self.assertEqual(gbfs_large_nodes, 103)
        self.assertEqual(astar_large_nodes, 163)
        self.assertEqual(cus1_large_nodes, 126)
        self.assertEqual(cus2_large_nodes, 133)

if __name__ == "__main__":
    unittest.main()