import customtkinter as ctk
import tkinter as tk

class MyFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.maze = [
            [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0]
        ]

        self.num_rows = len(self.maze)  # 5 rows
        self.num_cols = len(self.maze[0])  # 11 columns

        # Set a fixed size for the frame
        self.fixed_width = 880
        self.fixed_height = 400
        self.configure(width=self.fixed_width, height=self.fixed_height, fg_color="#ffffff")

        # Create a canvas for drawing the maze
        self.canvas = tk.Canvas(self, bg="#FFFFFF", highlightthickness=0, width=self.fixed_width, height=self.fixed_height)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Calculate cell sizes
        self.calculate_cell_size()

        # Draw the maze
        self.draw_maze()

    def calculate_cell_size(self):
        """Calculate the width and height of each cell based on the fixed frame size and the number of rows and columns."""
        self.cell_width = self.fixed_width / self.num_cols
        self.cell_height = self.fixed_height / self.num_rows

    def draw_maze(self):
        """Draw the maze on the canvas based on the 2D array."""
        for row_index, row in enumerate(self.maze):
            for col_index, cell in enumerate(row):
                x1 = col_index * self.cell_width
                y1 = row_index * self.cell_height
                x2 = x1 + self.cell_width
                y2 = y1 + self.cell_height

                # Draw a wall or a path
                if cell == 1:  # Wall
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="gray")
                else:  # Path
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="gray")

class TestFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="#ffffff",
                       width=880,
                       height=400)

    def create_widget(self):
        pass

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Window configuration
        self.geometry("1200x800+400+150")
        self.title("Maze Solver Visualization")
        # self.fg_color("#ffffff")
        self.configure(fg_color="#ffffff")

        # Add widgets to app
        self.map_visualization = TestFrame(self)
        self.map_visualization.place(x=50, y=50)

        self.dfs_button = ctk.CTkButton(self, 
                                        command=self.button_click,
                                        text="Depth-First Search",
                                        corner_radius=50,
                                        width=134)
        self.dfs_button.place(relx=0.8, rely=0.1)

    def button_click(self):
        print("button click")


if __name__ == "__main__":
    app = App()
    app.mainloop()
