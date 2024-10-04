from collections import OrderedDict, deque

class MapSolver:
    def __init__(self, map: dict):
        """
        Initializes the MapSolver with a given map.

        Args:
            map: A dictionary representing the map.
        """
        self.map = map
    
    def depth_first_search(self, start: tuple, goals: set):
        """
        Function that solves the map with Depth First Search(DFS)

        Args:
            start: Coordinate of a point
            goals: A set of all possible goals
        Return:
            nodes: Number of nodes traversed
            path: A list including all moves to a goal. Return None if no goal is reachable
        """
        visited = set()  # A set to store visited cells
        frontier = [start]  # A list as frontier
        parent = {}  # A dictionary to store checked movements

        parent[start] = (None, 0)

        while frontier:  # While there are nodes to explore
            cell = frontier.pop()  # Pop the last node from the frontier
            visited.add(cell)  # Mark the cell as visited

            if self.goal_meet(cell, goals):
                path = self.parse_path(start, cell, parent)
                return len(parent), path
            
            for i in range(len(self.map[cell])):
                index = len(self.map[cell]) - 1 - i
                neighbor = self.map[cell][index]
            
                if neighbor[0] not in visited and neighbor[0] not in frontier:
                    frontier.append(neighbor[0])
                    parent[neighbor[0]] = (cell, neighbor[1])

        return len(parent), None
    
    def breadth_first_search(self, start: tuple, goals: set) -> tuple[int, list]:
        """
        Function that solves the map with Breath First Search(BFS)

        Args:
            start: Coordinate of a point
            goals: A set of all possible goals
        Return:
                nodes: Number of nodes traversed
            path: A list including all moves to a goal. Return None if no goal is reachable
        """
        visited = set()             # A set to store visited cell
        frontier = deque([start])   # A queue as frontier 
        parent = {}                 # A dictionary to store checked movement

        parent[start] = (None, 0)

        while frontier:
            node = frontier.popleft()
            visited.add(node)

            if self.goal_meet(node, goals):
                path = self.parse_path(start, node, parent)
                return len(parent), path

            for neighbor in self.map[node]:
                if neighbor[0] not in visited and neighbor[0] not in frontier:
                    parent[neighbor[0]] = (node, neighbor[1])

                    frontier.append(neighbor[0])

        return len(parent), None
    
    def greedy_best_first_search(self, start: tuple, goals: set, cost_type: str = "manhattan"):
        """
        Function that solves the map with Greedy Best First Search(GBFS)

        Args:
            start: Coordinate of a point
            goals: A set of all possible goals
        Return:
            nodes: Number of nodes traversed
            path: A list including all moves to a goal. Return None if no goal is reachable
        """
        visited = set()             # A set to store visited cell
        frontier = {}               # A frontier to store 
        parent = {}                 # A dictionary to store final path

        frontier[start] = self.heuristic_cost(start, goals, cost_type)
        parent[start] = (None, 0)

        while frontier:
            # Get the key with the lowest cost
            v = min(frontier, key=frontier.get)
            del frontier[v]

            if self.goal_meet(v, goals):
                path = self.parse_path(start, v, parent)
                return len(parent), path
            
            visited.add(v)
            
            for neighbor in self.map[v]:
                if neighbor[0] not in visited and neighbor[0] not in frontier:
                    cost = self.heuristic_cost(neighbor[0], goals, cost_type)
                    frontier[neighbor[0]] = cost
                    parent[neighbor[0]] = (v, neighbor[1])

        return len(parent), None
    
    def a_star(self, start: tuple, goals: set, cost_type: str = "manhattan"):
        """
        Function that solves the map with A* Search

        Args:
            start: Coordinate of a point
            goals: A set of all possible goals
            cost_type: The type of heuristic cost function to use
        Return:
            nodes: Number of nodes traversed
            path: A list including all moves to a goal. Return None if no goal is reachable
        """
        visited = set()             # A set to store visited cell
        frontier = {}               # A frontier to store 
        parent = {}                 # A dictionary to store final path
        g_costs = {start : 0}

        frontier[start] = self.heuristic_cost(start, goals, cost_type)
        parent[start] = (None, None, 0)

        while frontier:
            # Get the key with the lowest cost
            v = min(frontier, key=frontier.get)
            del frontier[v]

            if self.goal_meet(v, goals):
                path = self.parse_path(start, v, parent)
                return len(parent), path
            
            visited.add(v)
            
            for neighbor in self.map[v]:
                if neighbor[0] not in visited:
                    f_cost = self.heuristic_cost(v, [neighbor[0]], cost_type) + g_costs[v]
                    h_cost = self.heuristic_cost(neighbor[0], goals, cost_type)
                    total_cost = f_cost + h_cost
    
                    if neighbor[0] not in frontier:
                        frontier[neighbor[0]] = total_cost
                        parent[neighbor[0]] = (v, neighbor[1], total_cost)
                        g_costs[neighbor[0]] = f_cost
                    else:
                        frontier[neighbor[0]] = min(frontier[neighbor[0]], total_cost)
                        g_costs[neighbor[0]] = min(g_costs[neighbor[0]], f_cost)

        return len(parent), None
    
    def iterative_deepening(self, start: tuple, goals: set):
        """
        Function that solves the map with Iterative Deepening

        Args:
            start: Coordinate of a point
            goals: A set of all possible goals
        Return:
            nodes: Number of nodes traversed
            path: A list including all moves to a goal. Return None if no goal is reachable
        """

        limit = 0

        while True:
            current_layer = 0
            
            while current_layer <= limit:
                visited = set()  # A set to store visited cells
                frontier = [start]  # A list as frontier
                parent = {}  # A dictionary to store checked movements

                parent[start] = (None, 0)
                temp_frontier = []
                while frontier:  # While there are nodes to explore
                    cell = frontier.pop()  # Pop the last node from the frontier
                    visited.add(cell)  # Mark the cell as visited

                    if self.goal_meet(cell, goals):
                        path = self.parse_path(start, cell, parent)
                        return len(parent), path
                    
                    for i in range(len(self.map[cell])):
                        index = len(self.map[cell]) - 1 - i
                        neighbor = self.map[cell][index]
                    
                        if neighbor[0] not in visited:
                            temp_frontier.append(neighbor[0])
                            parent[neighbor[0]] = (cell, neighbor[1])

                if (len(temp_frontier) == 0):
                    break
                else:
                    frontier = temp_frontier

                if current_layer == limit:
                    break

            current_layer+=1

        return len(parent), None
    
    def ida_star(self, start: tuple, goals: set, cost_type: str = "manhattan"):
        """
        Function that solves the map with IDA* Search

        Args:
            start: Coordinate of a point
            goals: A set of all possible goals
            cost_type: The type of heuristic cost function to use
        Return:
            nodes: Number of nodes traversed
            path: A list including all moves to a goal. Return None if no goal is reachable
        """
        def dfs(current, g_cost, threshold, parent, visited):
            """
            Recursive depth-first search for IDA* with cost threshold.
            """
            h_cost = self.heuristic_cost(current, goals, cost_type)
            f_cost = g_cost + h_cost

            # If the total cost exceeds the threshold, return f_cost as the minimum exceeded cost
            if f_cost > threshold:
                return f_cost, None

            # If goal is reached, return the path
            if self.goal_meet(current, goals):
                return f_cost, self.parse_path(start, current, parent)

            visited.add(current)

            # Set minimum cost that exceeds threshold to infinity
            min_exceeded_cost = float('inf')
            path = None

            for neighbor in self.map[current]:
                if neighbor[0] not in visited:
                    parent[neighbor[0]] = (current, neighbor[1], g_cost + 1)  # Track parent node and move
                    # Recursively search for the neighbor
                    new_cost, new_path = dfs(neighbor[0], g_cost + 1, threshold, parent, visited)

                    # If we find a valid path, return it immediately
                    if new_path is not None:
                        return new_cost, new_path

                    # Update the minimum exceeded cost
                    if new_cost < min_exceeded_cost:
                        min_exceeded_cost = new_cost

            visited.remove(current)
            return min_exceeded_cost, None

        # Initialize threshold with heuristic cost of the start node
        threshold = self.heuristic_cost(start, goals, cost_type)
        parent = {start: (None, None, 0)}  # Track parent and movement path for each node
        total_nodes_traversed = 0  # Count the total number of nodes traversed

        while True:
            visited = set()
            cost, path = dfs(start, 0, threshold, parent, visited)

            total_nodes_traversed += len(visited)

            if path is not None:  # If a valid path is found, return the result
                return total_nodes_traversed, path

            # If no path found and the minimum exceeded cost is infinity, return failure
            if cost == float('inf'):
                return total_nodes_traversed, None

            # Update threshold to the minimum exceeded cost
            threshold = cost
    
    def goal_meet(self, point: tuple, goals: set) -> bool:
        """
        Function that checks if the goal is met or not

        Args:
            point: Coordinate of a point
            goals: A set including all possible goals
        Return:
            true: Checking point is one of the goal
            false: Checking point is not one of the goal
        """
        return point in goals
    
    def manhattan_distance(self, point, goals):
        """
        Function that calculates the Manhattan distance from a point to a set of goals

        Args:
            point: Coordinate of a starting point
            goals: A set of all possible goals
        Return:
            cost: The minimum Manhattan distance to any goal
        """
        distances = [abs(point[0] - goal[0]) + abs(point[1] - goal[1]) for goal in goals]
        return min(distances)
    
    def euclidean_distance(self, point, goals):
        """
        Function that calculates the Euclidean distance from a point to a set of goals

        Args:
            point: Coordinate of a starting point
            goals: A set of all possible goals
        Return:
            cost: The minimum Euclidean distance to any goal
        """
        distances = [((point[0] - goal[0])**2 + (point[1] - goal[1])**2)**0.5 for goal in goals]
        return min(distances)
    
    def chebyshev_distance(self, point, goals):
        """
        Function that calculates the Chebyshev distance from a point to a set of goals

        Args:
            point: Coordinate of a starting point
            goals: A set of all possible goals
        Return:
            cost: The minimum Chebyshev distance to any goal
        """
        distances = [max(abs(point[0] - goal[0]), abs(point[1] - goal[1])) for goal in goals]
        return min(distances)
    
    def heuristic_cost(self, point, goals, type) -> int:
        """
        Function that calculates the heuristic cost from a point to a set of goals

        Args:
            point: Coordinate of a starting point
            goals: A set of all possible goals
            type: The type of heuristic cost function to use
        Return:
            cost: The cost to the nearest goal
        """
        if (type == "manhattan"):
            return self.manhattan_distance(point, goals)
        elif (type == "euclidean"):
            return self.euclidean_distance(point, goals)
        elif (type == "chebyshev"):
            return self.chebyshev_distance(point, goals)
        
    def parse_path(self, start: tuple, vertex: tuple, parent: dict) -> list:
        """
        Function that retrieves the path when a goal is reached

        Args:
            start: Coordinate of a starting point
            vertex: Coordinate of the reached goal
            parent: A dictionary including all possible movements so far
        Return:
            path: A list containing the final path
        """
        path = []
        path.insert(0, (vertex, None))

        while vertex != start:
            path.insert(0, parent[vertex][:2])
            vertex = parent[vertex][0]

        return path