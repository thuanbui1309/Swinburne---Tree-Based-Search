import customtkinter as ctk
import tkinter as tk
import copy

class MyFrame(ctk.CTkFrame):
    def __init__(self, master, solver, frame_size):
        super().__init__(master)
        self.configure(fg_color="#000000",
                       width=frame_size,
                       height=frame_size)

        self.solver = solver
        print(type(solver.map))
        self.map = copy.deepcopy(solver.map)

        # for line in self.map:
            # print(line)
        self.start = solver.start
        self.goals = solver.goals
        self.frame_size = frame_size

        self.transfer_map()
        
        self.original_map = copy.deepcopy(self.map)
        print("Map")
        for line in self.map:
            print(line)

        print("ORIGINAL")
        for line in self.original_map:
            print(line)

        self.calculate_cell_size()
        self.draw_background()
        self.draw_map()

        print()
        for line in self.map:
            print(line)

        print()
        for line in solver.map:
            print(line)

    def transfer_map(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):

                if self.map[i][j] == 0:
                    if j == self.start[0] and i == self.start[1]:
                        self.map[i][j] = "red"
                    elif tuple((j, i)) in self.goals:
                        self.map[i][j] = "green"
                    else:
                        self.map[i][j] = "white"

                elif self.map[i][j] == 1:
                    self.map[i][j] = "black"

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
                                  fg_color="#3F88C5")
        self.background.place(x=self.start_x, y=self.start_y)

    def draw_map(self):
        for row_index, row in enumerate(self.map):
            for col_index, cell in enumerate(row):
                x = (col_index + 1) * self.cell_size / 10 + col_index * self.cell_size
                y = (row_index + 1) * self.cell_size / 10 + row_index * self.cell_size

                node = ctk.CTkFrame(self.background,
                                    width=self.cell_size,
                                    height=self.cell_size,
                                    corner_radius=0)
                if cell == "black":
                    node.configure(fg_color="#000000")
                elif cell == "red":
                    node.configure(fg_color="#D00000")
                elif cell == "green":
                    node.configure(fg_color="#1DB954")
                elif cell == "white":
                    node.configure(fg_color="#ffffff")

                node.place(x=x, y=y)

    def clear_map(self):
        for widget in self.background.winfo_children():
            widget.destroy()
        self.draw_map()

    def map_refresh(self):
        for line in self.original_map:
            print(line)
        self.map = copy.deepcopy(self.original_map)
        self.draw_map()

class MapSolverVisualization(ctk.CTk):
    def __init__(self, mapSolver):
        super().__init__()
        self.geometry("1072x832+464+134")
        self.title("Map Solver Visualization")
        self.configure(fg_color="#000000")  
        self.solver = mapSolver
        self.create_widget()

    def create_widget(self):                    
        self.map_visualization = MyFrame(self, self.solver, 732)
        self.map_visualization.place(x=50, y=50)

        self.dfs_button = ctk.CTkButton(self,
                                        hover_color="#ffffff", 
                                        command=lambda: self.button_click("dfs"),
                                        text="Depth-First Search",
                                        corner_radius=50,
                                        fg_color="#1DB954",
                                        text_color="#000000")
        self.dfs_button.place(x=822, y=252)

        self.bfs_button = ctk.CTkButton(self,
                                        hover_color="#ffffff",
                                        fg_color="#1DB954",
                                        text_color="#000000", 
                                        command=lambda: self.button_click("bfs"),
                                        text="Breadth-First Search",
                                        corner_radius=50)
        self.bfs_button.place(x=822, y=302)

        self.gbfs_button = ctk.CTkButton(self,
                                        hover_color="#ffffff",
                                        fg_color="#1DB954",
                                        text_color="#000000", 
                                        command=lambda: self.button_click("gbfs"),
                                        text="Greedy-Best First Search",
                                        corner_radius=50)
        self.gbfs_button.place(x=822, y=352)

        self.astar = ctk.CTkButton(self,
                                   hover_color="#ffffff",
                                   fg_color="#1DB954",
                                   text_color="#000000", 
                                   command=lambda: self.button_click("astar"),
                                   text="A* Search",
                                   corner_radius=50)
        self.astar.place(x=822, y=402)

        self.cus1 = ctk.CTkButton(self,
                                  hover_color="#ffffff",
                                  fg_color="#1DB954",
                                  text_color="#000000", 
                                  command=lambda: self.button_click("cus1"),
                                  text="Iterative Deepening Search",
                                  corner_radius=50)
        self.cus1.place(x=822, y=452)

        self.cus2 = ctk.CTkButton(self,
                                  hover_color="#ffffff",
                                  fg_color="#1DB954",
                                  text_color="#000000", 
                                  command=lambda: self.button_click("cus2"),
                                  text="Iterative Deepening A* Search",
                                  corner_radius=50)
        self.cus2.place(x=822, y=502)

        self.cus3 = ctk.CTkButton(self,
                                  hover_color="#ffffff",
                                  fg_color="#1DB954",
                                  text_color="#000000", 
                                  command=lambda: self.button_click("all"),
                                  text="All Goal Search",
                                  corner_radius=50)
        self.cus3.place(x=822, y=552)

    def button_click(self, search_type: str):
        print("Button clicked")
        self.map_visualization.map_refresh()

        if search_type == "dfs":
            self.solver.depth_first_search(viz=self)
        elif search_type == "bfs":
            self.solver.breadth_first_search(viz=self)
        elif search_type == "gbfs":
            self.solver.greedy_best_first_search(viz=self)
        elif search_type == "astar":
            self.solver.astar(viz=self)
        elif search_type == "cus1":
            self.solver.iterative_deepening_search(viz=self)
        elif search_type == "cus2":
            self.solver.ida_star(viz=self)
        elif search_type == "all":
            self.solver.astar_multi_goals(viz=self)

    def update_map(self, cell):
        # Update only the specific cell that needs to change
        self.map_visualization.clear_map()
        self.map_visualization.map[cell[1]][cell[0]] = "green"
        self.map_visualization.draw_map()