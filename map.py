import customtkinter as ctk
import tkinter as tk
import copy

START_COLOR = "#D00000"
GOAL_COLOR = "#1DB954"
OBSTACLE_COLOR = "#000000"
EMPTY_COLOR = "#ffffff"
PATH_COLOR = "#FFBA08"
FINAL_PATH_COLOR = "#1DB954"
FRAME_BG_COLOR = "#000000"
WINDOW_BG_COLOR = "#000000"
MAZE_BG_COLOR = "#3F88C5"
BUTTON_BG_COLOR = "#1DB954"
BUTTON_TEXT_COLOR = "#000000"

WINDOW_HEIGHT = 832
WINDOW_WIDTH = 1072
WINDOW_X = 464
WINDOW_Y = 134
FRAME_SIZE = 732
FRAME_X = 50
FRAME_Y = 50
BUTTON_START_X = 822
BUTTON_Y = 252

class MyFrame(ctk.CTkFrame):
    def __init__(self, master, solver, frame_size):
        super().__init__(master)
        self.configure(fg_color=FRAME_BG_COLOR,
                       width=frame_size,
                       height=frame_size)

        self.solver = solver
        self.map = copy.deepcopy(solver.map)
        self.start = solver.start
        self.goals = copy.deepcopy(solver.goals)
        self.frame_size = frame_size

        self.transfer_map()
        self.original_map = copy.deepcopy(self.map)
        self.calculate_cell_size()
        self.draw_background()
        self.draw_map()

    def transfer_map(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):

                if self.map[i][j] == 0:
                    if j == self.start[0] and i == self.start[1]:
                        self.map[i][j] = START_COLOR
                    elif tuple((j, i)) in self.goals:
                        self.map[i][j] = GOAL_COLOR
                    else:
                        self.map[i][j] = EMPTY_COLOR

                elif self.map[i][j] == 1:
                    self.map[i][j] = OBSTACLE_COLOR

    def calculate_cell_size(self):
        self.cell_size = None
        self.start_x = None
        self.start_y = None
        self.map_width = None
        self.map_height = None

        map_column = len(self.map[0])
        map_row = len(self.map)

        if (map_row < map_column):
            self.cell_size = self.frame_size / ((map_column + ((map_column+1) / 10)))
            self.map_width = self.frame_size
            self.map_height = self.cell_size * (map_row + (map_row + 1) / 10)
            self.start_x = 0
            self.start_y = (self.frame_size - self.map_height) / 2
        elif (map_column >= map_row):
            self.cell_size = self.frame_size / ((map_row + ((map_row+1) / 10)))
            self.map_height = self.frame_size
            self.map_width = self.cell_size * (map_column + (map_column + 1) / 10)
            self.start_x = (self.frame_size - self.map_width) / 2
            self.start_y = 0

    def draw_background(self):
        self.background = ctk.CTkFrame(self,
                                  width=self.map_width,
                                  height=self.map_height,
                                  fg_color=MAZE_BG_COLOR)
        self.background.place(x=self.start_x, y=self.start_y)

    def draw_map(self):
        for row_index, row in enumerate(self.map):
            for col_index, cell in enumerate(row):
                x = (col_index + 1) * self.cell_size / 10 + col_index * self.cell_size
                y = (row_index + 1) * self.cell_size / 10 + row_index * self.cell_size

                node = ctk.CTkFrame(self.background,
                                    width=self.cell_size,
                                    height=self.cell_size,
                                    corner_radius=0,
                                    fg_color=cell)

                node.place(x=x, y=y)

    def clear_map(self):
        for widget in self.background.winfo_children():
            widget.destroy()
        self.draw_map()

    def refresh_map(self):
        # for widget in self.background.winfo_children():
            # widget.destroy()
        self.map = copy.deepcopy(self.original_map)
        self.draw_map()

class MapSolverVisualization(ctk.CTk):
    def __init__(self, mapSolver):
        super().__init__()
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_X}+{WINDOW_Y}")
        self.title("Map Solver Visualization")
        self.configure(fg_color=WINDOW_BG_COLOR)  
        self.solver = mapSolver
        self.create_widget()

    def create_widget(self):                    
        self.map_visualization = MyFrame(self, self.solver, FRAME_SIZE)
        self.map_visualization.place(x=FRAME_X, y=FRAME_Y)

        self.dfs_button = ctk.CTkButton(self,
                                        hover_color="#ffffff", 
                                        command=lambda: self.button_click("dfs"),
                                        text="Depth-First Search",
                                        corner_radius=50,
                                        fg_color=BUTTON_BG_COLOR,
                                        text_color=BUTTON_TEXT_COLOR)
        self.dfs_button.place(x=822, y=252)

        self.bfs_button = ctk.CTkButton(self,
                                        hover_color="#ffffff",
                                        fg_color=BUTTON_BG_COLOR,
                                        text_color=BUTTON_TEXT_COLOR, 
                                        command=lambda: self.button_click("bfs"),
                                        text="Breadth-First Search",
                                        corner_radius=50)
        self.bfs_button.place(x=822, y=302)

        self.gbfs_button = ctk.CTkButton(self,
                                        hover_color="#ffffff",
                                        fg_color=BUTTON_BG_COLOR,
                                        text_color=BUTTON_TEXT_COLOR, 
                                        command=lambda: self.button_click("gbfs"),
                                        text="Greedy-Best First Search",
                                        corner_radius=50)
        self.gbfs_button.place(x=822, y=352)

        self.astar = ctk.CTkButton(self,
                                   hover_color="#ffffff",
                                   fg_color=BUTTON_BG_COLOR,
                                   text_color=BUTTON_TEXT_COLOR, 
                                   command=lambda: self.button_click("astar"),
                                   text="A* Search",
                                   corner_radius=50)
        self.astar.place(x=822, y=402)

        self.cus1 = ctk.CTkButton(self,
                                  hover_color="#ffffff",
                                  fg_color=BUTTON_BG_COLOR,
                                  text_color=BUTTON_TEXT_COLOR, 
                                  command=lambda: self.button_click("cus1"),
                                  text="Iterative Deepening Search",
                                  corner_radius=50)
        self.cus1.place(x=822, y=452)

        self.cus2 = ctk.CTkButton(self,
                                  hover_color="#ffffff",
                                  fg_color=BUTTON_BG_COLOR,
                                  text_color=BUTTON_TEXT_COLOR, 
                                  command=lambda: self.button_click("cus2"),
                                  text="Iterative Deepening A* Search",
                                  corner_radius=50)
        self.cus2.place(x=822, y=502)

        self.cus3 = ctk.CTkButton(self,
                                  hover_color="#ffffff",
                                  fg_color=BUTTON_BG_COLOR,
                                  text_color=BUTTON_TEXT_COLOR, 
                                  command=lambda: self.button_click("all"),
                                  text="All Goal Search",
                                  corner_radius=50)
        self.cus3.place(x=822, y=552)

    def button_click(self, search_type: str):
        print("Button clicked")
        self.map_visualization.clear_map()
        self.map_visualization.refresh_map()

        print(self.map_visualization.goals)

        if search_type == "dfs":
            print("DFS")
            self.solver.depth_first_search(viz=self)
        elif search_type == "bfs":
            print("BFS")
            self.solver.breadth_first_search(viz=self)
        elif search_type == "gbfs":
            print("GBFS")
            self.solver.greedy_best_first_search(viz=self)
        elif search_type == "astar":
            print("A*")
            self.solver.astar(viz=self)
        elif search_type == "cus1":
            print("CUS1")
            self.solver.iterative_deepening_search(viz=self)
        elif search_type == "cus2":
            print("CUS2")
            self.solver.ida_star(viz=self)
        elif search_type == "all":
            print("All")
            self.solver.astar_multi_goals(viz=self)

    def update_map(self, cell, color=PATH_COLOR):
        if cell != self.solver.start and cell not in self.solver.goals:
            self.map_visualization.clear_map()
            self.map_visualization.map[cell[1]][cell[0]] = color
            self.map_visualization.draw_map()

    def show_path(self, path):
        path_coordinates = [cell for cell, _ in path[:-1]]

        for cell in path_coordinates:
            # print(cell)
            self.update_map(cell, color=FINAL_PATH_COLOR)
            self.update_idletasks()
            self.after(300)

    def reset_map(self):
        self.map_visualization.refresh_map()