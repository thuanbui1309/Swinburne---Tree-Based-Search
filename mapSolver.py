from collections import deque

class MapSolver:
    def __init__(self, map: list):
        """
        Initializes the MapSolver with a given map.

        Args:
            map: A 2D array representing the map.
        """
        self.map = map

    def depth_first_search(self, start: tuple, goals: set) -> tuple[int, list]:
        """
        Function that solves the map with Depth First Search(DFS)

        Args:
            start: Coordinate of a point
            goals: A set of all possible goals
        Return:
            nodes: Number of nodes traversed
            path: A list including all moves to a goal. Return None if no goal is reachable
        """
        visited = set()
        frontier = [start]
        parent = {}

        parent[start] = (None, None)

        while frontier:
            cell = frontier.pop()
            if cell not in visited:
                visited.add(cell)

                if self.goal_meet(cell, goals):
                    path = self.parse_path(start, cell, parent)
                    return len(parent), path
                
                neighbors = self.get_neighbors(cell)
                # Reverse the order of neighbors to ensure the order of execution is up, left, down, right
                for neighbor in reversed(neighbors):
                    if neighbor[0] not in visited:
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
        visited = set()             
        frontier = deque([start]) 
        parent = {}

        parent[start] = (None, None)

        while frontier:
            cell = frontier.popleft()
            if cell not in visited: 
                visited.add(cell)

                if self.goal_meet(cell, goals):
                    path = self.parse_path(start, cell, parent)
                    return len(parent), path
                
                neighbors = self.get_neighbors(cell)
                for neighbor in neighbors:
                    if neighbor[0] not in visited and neighbor[0] not in parent.keys():
                        # If parent already contain a path to this neighbor cell
                        # Meaning there is a nearer path to reach it 
                        # It can be from near cell, or from prioritized order
                        # Avoid duplicate to ensure shortest path found (main goal of BFS)
                        parent[neighbor[0]] = (cell, neighbor[1])
                        frontier.append(neighbor[0])
        return len(parent), None
    
    def greedy_best_first_search(self, start: tuple, goals: set, cost_type: str = "manhattan") -> tuple[int, list]:
        """
        Function that solves the map with Greedy Best First Search(GBFS)

        Args:
            start: Coordinate of a point
            goals: A set of all possible goals
        Return:
            nodes: Number of nodes traversed
            path: A list including all moves to a goal. Return None if no goal is reachable
        """
        visited = set()
        frontier = {}
        parent = {}

        frontier[start] = self.heuristic_cost(start, goals, cost_type)
        parent[start] = (None, None)

        while frontier:
            # Get the key with the lowest cost
            cell = min(frontier, key=frontier.get)
            del frontier[cell]
            visited.add(cell)

            if self.goal_meet(cell, goals):
                path = self.parse_path(start, cell, parent)
                return len(parent), path

            neighbors = self.get_neighbors(cell)
            for neighbor in neighbors:
                if neighbor[0] not in visited and neighbor[0] not in frontier:
                    cost = self.heuristic_cost(neighbor[0], goals, cost_type)
                    frontier[neighbor[0]] = cost
                    parent[neighbor[0]] = (cell, neighbor[1])

        return len(parent), None
    
    def astar(self, start: tuple, goals: set, cost_type: str ="manhattan") -> tuple[int, list]:
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
        frontier = {}               
        visited = {}              
        parent = {}                 

        frontier[start] = 0
        parent[start] = (None, None, 0)

        while frontier:
            costs = {key: value + self.heuristic_cost(key, goals, cost_type) for key, value in frontier.items()}
            cell = min(costs, key=costs.get)

            current_cell_cost = frontier[cell]
            del frontier[cell]
            visited[cell] = current_cell_cost

            if self.goal_meet(cell, goals):
                path = self.parse_path(start, cell, parent)
                return len(parent), path
            
            neighbors = self.get_neighbors(cell)
            for neighbor in neighbors:
                g_cost = self.heuristic_cost(neighbor[0], [cell], cost_type) + current_cell_cost
                h_cost = self.heuristic_cost(neighbor[0], goals, cost_type)
                f_cost = g_cost + h_cost

                if neighbor[0] in frontier:
                    if f_cost < frontier[neighbor[0]]:
                        frontier[neighbor[0]] = f_cost
                        parent[neighbor[0]] = (cell, neighbor[1])
                elif neighbor[0] in visited:
                    if f_cost < visited[neighbor[0]]:
                        del visited[neighbor[0]]
                        frontier[neighbor[0]] = f_cost
                        parent[neighbor[0]] = (cell, neighbor[1]) 
                else:
                    frontier[neighbor[0]] = f_cost
                    parent[neighbor[0]] = (cell, neighbor[1])

        return len(parent), None
    
    def iterative_deepening_search(self, start: tuple, goals: set) -> tuple[int, list]:
        """
        Function that solves the map with Iterative Deepening Search

        Args:
            start: Coordinate of a point
            goals: A set of all possible goals
            cost_type: The type of heuristic cost function to use
        Return:
            nodes: Number of nodes traversed
            path: A list including all moves to a goal. Return None if no goal is reachable
        """
        def limited_search(cell: tuple, goals: set, depth: int) -> tuple:
            """
            This function recursively performs a Depth-First Search (DFS) to find a goal within a given depth limit.

            Args:
                cell: The current cell being explored, represented as a tuple of coordinates.
                goals: A set of all possible goal cells.
                depth: The current depth of the search, used to limit the search depth.

            Returns:
                goal: The coordinate of a reachable goal cell if found, otherwise returns None.
            """
            # Mark the current cell as visited to avoid revisiting it
            visited.add(cell)

            # Check if the current cell is a goal
            if self.goal_meet(cell, goals):
                return cell
            
            # If the current depth is 0, stop expanding nodes to avoid exceeding the depth limit
            if depth == 0:
                return None
            
            # Get all neighboring cells of the current cell
            neighbors = self.get_neighbors(cell)
            for neighbor in neighbors:
                if neighbor[0] not in visited:
                    # Store the path to the neighbor in the parent dictionary for backtracking
                    parent[neighbor[0]] = (cell, neighbor[1])

                    # Recursively search the neighbor with a reduced depth
                    goal = limited_search(neighbor[0], goals, depth-1)

                    # If a goal is found, return it
                    if goal:
                        return goal
                    
            # If no goal is found, return None
            return None

        # Initialize the depth to 0 and start an infinite loop to incrementally increase the depth
        depth = 0
        while True:
            # Reset the parent and visited sets for each depth increment
            parent = {}
            visited = set()
            parent[start] = (None, None)

            # Perform the limited search starting from the given start cell
            goal = limited_search(start, goals, depth)
            # If a goal is found, parse the path to the goal and return the number of nodes traversed and the path
            if goal:
                path = self.parse_path(start, goal, parent)
                return len(parent), path
            
            # Increment the depth for the next iteration
            depth += 1

    def ida_star(self, start: tuple, goals: set, cost_type: str ="manhattan") -> tuple[int, list]:
        """
        Function that solves the map with Iterative Deepening A*

        Args:
            start: Coordinate of a point
            goals: A set of all possible goals
        Return:
            nodes: Number of nodes traversed
            path: A list including all moves to a goal. Return None if no goal is reachable
        """
        threshold = self.heuristic_cost(start, goals, cost_type)

        while True:
            frontier = [(start, 0)]
            parent = {start: (None, None)}
            visited = set()
            next_threshold = float("inf")

            while frontier:
                cell, g_cost = frontier.pop()
                if cell not in visited:
                    visited.add(cell)

                    h_cost = self.heuristic_cost(cell, goals, cost_type)
                    f_cost = g_cost + h_cost

                    # print(f"Cell: {cell} with f_cost: {f_cost} in threshold: {threshold}")

                    if self.goal_meet(cell, goals):
                        path = self.parse_path(start, cell, parent)
                        # print(parent)
                        return len(parent), path


                    if f_cost > threshold:
                        next_threshold = min(next_threshold, f_cost)
                        # print("Forwarding...")
                        continue
                    
                    neighbors = self.get_neighbors(cell)
                    for neighbor in reversed(neighbors):
                        if neighbor[0] not in visited:
                            # print(f"Neighbor: {neighbor[0]} of {cell} in threshold: {threshold}")
                            frontier.append((neighbor[0], g_cost + self.heuristic_cost(cell, [neighbor[0]], cost_type)))
                            parent[neighbor[0]] = (cell, neighbor[1])

                    # print("\n")
                
            if next_threshold == float("inf"):
                return len(visited), None

            # print("\nNext Threshold:")
            threshold = next_threshold

    def cell_in_map(self, cell: tuple) -> bool:
        """
        Function that checks if a cell is within the map boundaries

        Args:
            cell: Coordinate of a cell
        Return:
            true: If the cell is within the map boundaries
            false: If the cell is outside the map boundaries
        """
        return cell[0] >= 0 and cell[0] < len(self.map) and cell[1] >= 0 and cell[1] < len(self.map[0])

    def cell_is_wall(self, cell: tuple) -> bool:
        """
        Function that checks if a cell is a wall

        Args:
            cell: Coordinate of a cell
        Return:
            true: If the cell is a wall
            false: If the cell is not a wall
        """
        return self.map[cell[0]][cell[1]] == 1

    def get_neighbors(self, cell: tuple) -> list:
        """
        Function that retrieves the neighbors of a cell
        Neighbors list will follow order "up", "left", "down", "right"

        Args:
            cell: Coordinate of a cell
        Return:
            neighbors: A list of all valid neighbors of the cell
        """
        neighbors = []
        # Need to reverse coordinates to access element accurately
        cell_x = cell[1]
        cell_y = cell[0]

        directions = {(-1, 0) : "up", 
                      (0, -1) : "left", 
                      (1, 0) : "down", 
                      (0, 1) : "right"}

        for coor, direction in directions.items():
            neighbor_x = cell_x + coor[0]
            neighbor_y = cell_y + coor[1]
            neighbor = (neighbor_x, neighbor_y)

            if self.cell_in_map(neighbor) and not self.cell_is_wall(neighbor):
                neighbors.append(((neighbor_y, neighbor_x), direction))

        return neighbors

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
    
    def manhattan_distance(self, point: tuple, goals: set) -> float:
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
    
    def euclidean_distance(self, point: tuple, goals: set) -> float:
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
    
    def chebyshev_distance(self, point: tuple, goals: set) -> int:
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
    
    def heuristic_cost(self, point: tuple, goals: set, type: str) -> int:
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
    
    def astar_multi_goals(self, start: tuple, goals: set, cost_type: str = "manhattan") -> tuple[int, list]:
        """
        Function that solves the map with A* Search and aims to reach all goals with the shortest path.

        Args:
            start: Coordinate of a starting point.
            goals: A set of all possible goal cells.
            cost_type: The type of heuristic cost function to use.

        Returns:
            nodes: Total number of nodes traversed.
            path: A list of all moves to all goals in sequence. Returns "can't reach all goals" if not all goals are reachable.
        """
        total_nodes = 0
        total_path = []

        original_goals = goals.copy()
        while True:
            frontier = {}
            visited = {}
            parent = {}
            
            frontier[start] = 0
            parent[start] = (None, None, 0)
            
            found_goal = None
            while frontier:
                costs = {key: value + self.heuristic_cost(key, original_goals, cost_type) for key, value in frontier.items()}
                cell = min(costs, key=costs.get)
                current_cell_cost = frontier[cell]
                del frontier[cell]
                visited[cell] = current_cell_cost

                if cell in original_goals:
                    found_goal = cell
                    break
                
                neighbors = self.get_neighbors(cell)
                for neighbor in neighbors:
                    g_cost = self.heuristic_cost(neighbor[0], [cell], cost_type) + current_cell_cost
                    h_cost = self.heuristic_cost(neighbor[0], original_goals, cost_type)
                    f_cost = g_cost + h_cost

                    if neighbor[0] in frontier:
                        if f_cost < frontier[neighbor[0]]:
                            frontier[neighbor[0]] = f_cost
                            parent[neighbor[0]] = (cell, neighbor[1])
                    elif neighbor[0] in visited:
                        if f_cost < visited[neighbor[0]]:
                            del visited[neighbor[0]]
                            frontier[neighbor[0]] = f_cost
                            parent[neighbor[0]] = (cell, neighbor[1])
                    else:
                        frontier[neighbor[0]] = f_cost
                        parent[neighbor[0]] = (cell, neighbor[1])
            
            total_nodes += len(parent)
            if not found_goal:
                return total_nodes, None
            
            path_to_goal = self.parse_path(start, found_goal, parent)
            original_goals.remove(found_goal)

            if original_goals:
                start = found_goal
                total_path.extend(path_to_goal[:-1])
            else:
                total_path.extend(path_to_goal)
                return total_nodes, total_path