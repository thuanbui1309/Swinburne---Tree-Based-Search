import ast

def parse_grid(filename) -> tuple[list, list, dict]:
    """
    Function that parses input data file into coordinate in a gird

    Args:
        filename: Directory to input file
    Return:
        start: A list contains coordinate of starting point
        goals: A list contains coordinate of ALL goal points
        map_grid: An adjacency map contain points and its valid moves
    """

    with open(filename, 'r') as file:
        # Create map based on given coordinate
        grid_size = ast.literal_eval(file.readline())
        grid = [[0 for _ in range(grid_size[1])] for _ in range(grid_size[0])]

        # Mark the position of starting point
        start = ast.literal_eval(file.readline())

        # Mark goal target
        goals = file.readline().split(' | ')

        # Mark walls
        for line in file:
            line = ast.literal_eval(line)
            for i in range(line[2]):
                for j in range(line[3]):
                    grid[line[1] + j][line[0] + i] = 1

        map_grid = parse_adjacency_list(grid)

    return start, goals, map_grid

def parse_adjacency_list(grid: list) -> dict:
    """
    - Function that turns a 2D array to an adjacency list
    - This list stores each cell and possible moves (or neighbor) of this point
    - A valid move is move that:
        1. Not go out the map
        2. Not go to a wall
    - A wall has no possible move
    - Possible moves will follow order: UP, LEFT, DOWN, RIGHT

    Args:
        grid: 2D list stores coordinates
    Return:
        adjacency_map: Dictionary(map) contains cell and its possible moves
    """

    adjacency_map = {}

    for i in range(len(grid)):
        for j in range(len(grid[i])):

            # Only care if a cell is not a wall
            if (grid[i][j] != 1):
            
                neighbor = []

                # Try Move Up
                up_row = i - 1
                if (up_row >= 0 and grid[up_row][j] != 1):
                    neighbor.append((j, up_row))
                
                # Try Move Left
                left_column = j - 1
                if (left_column >= 0 and grid[i][left_column] != 1):
                    neighbor.append((left_column, i))

                # Try Move Down
                down_row = i + 1
                if (down_row <= len(grid) - 1 and grid[down_row][j] != 1):
                    neighbor.append((j, down_row))
                
                # Try Move Left
                right_column = j + 1
                if (right_column <= len(grid[i]) - 1 and grid[i][right_column] != 1):
                    neighbor.append((right_column, i))

                adjacency_map[(j, i)] = neighbor

    return adjacency_map