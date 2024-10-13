import unittest
from mapSolver import MapSolver
from utils import parse_grid

class TestMapSolver(unittest.TestCase):

    def setUp(self):
        self.small_map_start, self.small_goals, self.small_map = parse_grid("Test/t1.txt")
        self.medium_map_start, self.medium_goals, self.medium_map = parse_grid("Test/t2.txt")
        self.large_map_start, self.large_goals, self.large_map = parse_grid("Test/t3.txt")
        # self.blocked_map_start, self.blocked_goals, self.blocked_map = parse_grid("Test Map/t4.txt")

        self.small_solver = MapSolver(self.small_map)
        self.medium_solver = MapSolver(self.medium_map)
        self.large_solver = MapSolver(self.large_map)
        # self.blocked_solver = MapSolver(self.blocked_map)
        
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

    def test_parseGrid_returnsCorrectGrid(self):
        # Test if map is accurately retrived
        accurate_small_map = [[0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 0, 0], [1, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0]]
        accurate_medium_map = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0]]
        accurate_large_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1], [0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1], [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1], [0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0], [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0], [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1], [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0]]
        
        self.assertEqual(self.small_map, accurate_small_map)
        self.assertEqual(self.medium_map, accurate_medium_map)
        self.assertEqual(self.large_map, accurate_large_map)

    def test_smallMapSolver_ReturnCorrectPath(self):
        # Test if the map solver accurately solves the map in small scale
        dfs_path = [direction for _, direction in self.small_solver.depth_first_search(self.small_map_start, self.small_goals)[1][:-1]]
        bfs_path = [direction for _, direction in self.small_solver.breadth_first_search(self.small_map_start, self.small_goals)[1][:-1]]
        gbfs_path = [direction for _, direction in self.small_solver.greedy_best_first_search(self.small_map_start, self.small_goals)[1][:-1]]
        astar_path = [direction for _, direction in self.small_solver.astar(self.small_map_start, self.small_goals)[1][:-1]]
        cus1_path = [direction for _, direction in self.small_solver.iterative_deepening_search(self.small_map_start, self.small_goals)[1][:-1]]
        cus2_path = [direction for _, direction in self.small_solver.ida_star(self.small_map_start, self.small_goals)[1][:-1]]

        dfs_accurate_path = ['right', 'right', 'down', 'down', 'down', 'right', 'right', 'up', 'up', 'up', 'right', 'down']
        bfs_accurate_path = ['right', 'right', 'right', 'right', 'down', 'right']
        gbfs_accurate_path = ['right', 'right', 'right', 'right', 'down', 'right']
        astar_accurate_path = ['right', 'right', 'right', 'right', 'down', 'right']
        cus1_accurate_path = ['right', 'right', 'right', 'right', 'down', 'right']
        cus2_accurate_path = ['right', 'right', 'right', 'right', 'down', 'right']

        self.assertEqual(dfs_path, dfs_accurate_path)
        self.assertEqual(bfs_path, bfs_accurate_path)
        self.assertEqual(gbfs_path, gbfs_accurate_path)
        self.assertEqual(astar_path, astar_accurate_path)
        self.assertEqual(cus1_path, cus1_accurate_path)
        self.assertEqual(cus2_path, cus2_accurate_path)

    def test_mediumMapSolver_ReturnCorrectPath(self):
        # Test if the map solver accurately solves the map in small scale
        dfs_path = [direction for _, direction in self.medium_solver.depth_first_search(self.medium_map_start, self.medium_goals)[1][:-1]]
        bfs_path = [direction for _, direction in self.medium_solver.breadth_first_search(self.medium_map_start, self.medium_goals)[1][:-1]]
        gbfs_path = [direction for _, direction in self.medium_solver.greedy_best_first_search(self.medium_map_start, self.medium_goals)[1][:-1]]
        astar_path = [direction for _, direction in self.medium_solver.astar(self.medium_map_start, self.medium_goals)[1][:-1]]
        cus1_path = [direction for _, direction in self.medium_solver.iterative_deepening_search(self.medium_map_start, self.medium_goals)[1][:-1]]
        cus2_path = [direction for _, direction in self.medium_solver.ida_star(self.medium_map_start, self.medium_goals)[1][:-1]]

        dfs_accurate_path = ['up', 'up', 'up', 'right', 'right', 'up', 'up', 'up', 'up', 'right', 'right', 'right', 'down', 'right', 'up', 'right', 'right', 'right', 'right', 'down', 'down']
        bfs_accurate_path = ['up', 'right', 'right', 'right', 'right', 'right', 'up', 'right', 'right', 'down', 'down']
        gbfs_accurate_path = ['up', 'right', 'right', 'down', 'right', 'right', 'right', 'up', 'up', 'right', 'right', 'down', 'down']
        astar_accurate_path = ['up', 'right', 'right', 'right', 'right', 'right', 'up', 'right', 'right', 'down', 'down']
        cus1_accurate_path = ['up', 'right', 'right', 'down', 'right', 'up', 'right', 'down', 'right', 'up', 'up', 'right', 'right', 'down', 'down']
        cus2_accurate_path = ['up', 'right', 'right', 'down', 'right', 'up', 'right', 'down', 'right', 'up', 'up', 'right', 'right', 'down', 'down']

        self.assertEqual(dfs_path, dfs_accurate_path)
        self.assertEqual(bfs_path, bfs_accurate_path)
        self.assertEqual(gbfs_path, gbfs_accurate_path)
        self.assertEqual(astar_path, astar_accurate_path)
        self.assertEqual(cus1_path, cus1_accurate_path)
        self.assertEqual(cus2_path, cus2_accurate_path)

    def test_largeMapSolver_ReturnCorrectPath(self):
        # Test if the map solver accurately solves the map in small scale
        dfs_path = [direction for _, direction in self.large_solver.depth_first_search(self.large_map_start, self.large_goals)[1][:-1]]
        bfs_path = [direction for _, direction in self.large_solver.breadth_first_search(self.large_map_start, self.large_goals)[1][:-1]]
        gbfs_path = [direction for _, direction in self.large_solver.greedy_best_first_search(self.large_map_start, self.large_goals)[1][:-1]]
        astar_path = [direction for _, direction in self.large_solver.astar(self.large_map_start, self.large_goals)[1][:-1]]
        cus1_path = [direction for _, direction in self.large_solver.iterative_deepening_search(self.large_map_start, self.large_goals)[1][:-1]]
        cus2_path = [direction for _, direction in self.large_solver.ida_star(self.large_map_start, self.large_goals)[1][:-1]]

        dfs_accurate_path = ['up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'right', 'right', 'right', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'left', 'left', 'up', 'up', 'left', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'right', 'up', 'right', 'up', 'up', 'right', 'down', 'down', 'down', 'right', 'right', 'right', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'right', 'up', 'up', 'right', 'down', 'down', 'right', 'down', 'down', 'down', 'down', 'right', 'right', 'down', 'right', 'up', 'up', 'up', 'right', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'left', 'left', 'up', 'up', 'up', 'up', 'up', 'up']
        bfs_accurate_path = ['down', 'down', 'down', 'right', 'right', 'right', 'up', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'down', 'down', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'down', 'down', 'right', 'right']
        gbfs_accurate_path = ['up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'right', 'right', 'right', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'right', 'right', 'down', 'right', 'right', 'up', 'up', 'right', 'right', 'down', 'down', 'down', 'down', 'right', 'down', 'down', 'right', 'down', 'right', 'right', 'down', 'down', 'down', 'right', 'right', 'up', 'up', 'up', 'up', 'right', 'right', 'down', 'down', 'down', 'down', 'right', 'right']
        # astar_accurate_path = 
        cus1_accurate_path = ['up', 'right', 'right', 'down', 'right', 'up', 'right', 'down', 'right', 'up', 'up', 'right', 'right', 'down', 'down']
        cus2_accurate_path = ['up', 'right', 'right', 'down', 'right', 'up', 'right', 'down', 'right', 'up', 'up', 'right', 'right', 'down', 'down']

        self.assertEqual(dfs_path, dfs_accurate_path)
        self.assertEqual(bfs_path, bfs_accurate_path)
        self.assertEqual(gbfs_path, gbfs_accurate_path)
        # self.assertEqual(astar_path, astar_accurate_path)
        self.assertEqual(cus1_path, cus1_accurate_path)
        self.assertEqual(cus2_path, cus2_accurate_path)

    # def test_noGoalIsReachable_ReturnCorrectMessage(self):
    #     # Test if the map solver accurately returns the message when no goal is reachable
    #     pass

    # def test_cantAccessAllGoals_ReturnCorrectMessage(self):
    #     # Test if the map solver accurately returns the message when no goal is reachable
    #     pass

    # def test_orderMovement_ReturnCorrectOrder(self):
    #     # Test if the map solver accurately returns the order of movement
    #     pass

    # def test_goToWalls_ReturnCorrectPath(self):
    #     # Test if the map solver accurately returns the path to the walls
    #     pass

    # def test_WrongNumberOfNodes_ReturnCorrectMessage(self):
        # Test if the map solver accurately returns the message when the number of nodes is wrong
        pass

if __name__ == "__main__":
    unittest.main()