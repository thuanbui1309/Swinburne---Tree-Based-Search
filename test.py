import customtkinter as ctk

# Lớp Maze để tạo và vẽ mê cung
class Maze:
    def __init__(self, maze_data, canvas, cell_size=50):
        self.maze_data = maze_data
        self.canvas = canvas
        self.cell_size = cell_size
        self.draw_maze()

    # Vẽ mê cung dựa trên ma trận 2D
    def draw_maze(self):
        for i in range(len(self.maze_data)):
            for j in range(len(self.maze_data[0])):
                x0, y0 = j * self.cell_size, i * self.cell_size
                x1, y1 = x0 + self.cell_size, y0 + self.cell_size
                if self.maze_data[i][j] == 1:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill="black")
                else:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill="white")

    # Kiểm tra xem vị trí có phải là tường không
    def is_wall(self, x, y):
        return self.maze_data[y][x] == 1


# Lớp Player để quản lý di chuyển của người chơi
class Player:
    def __init__(self, maze, canvas, start_x, start_y, cell_size=50):
        self.maze = maze
        self.canvas = canvas
        self.cell_size = cell_size
        self.x = start_x
        self.y = start_y
        self.player = self.canvas.create_oval(self.x * self.cell_size, self.y * self.cell_size,
                                              (self.x + 1) * self.cell_size, (self.y + 1) * self.cell_size, fill="red")

    # Hàm di chuyển người chơi
    def move(self, direction):
        new_x, new_y = self.x, self.y
        if direction == 'Up':
            new_y -= 1
        elif direction == 'Down':
            new_y += 1
        elif direction == 'Left':
            new_x -= 1
        elif direction == 'Right':
            new_x += 1

        # Chỉ di chuyển nếu vị trí mới không phải là tường
        if not self.maze.is_wall(new_x, new_y):
            self.x, self.y = new_x, new_y
            self.update_position()

    # Cập nhật vị trí người chơi trên canvas
    def update_position(self):
        self.canvas.coords(self.player, self.x * self.cell_size, self.y * self.cell_size,
                           (self.x + 1) * self.cell_size, (self.y + 1) * self.cell_size)


# Lớp MazeApp để quản lý giao diện và logic tổng thể
class MazeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Visualization OOP")

        # Tạo Canvas
        self.canvas = ctk.CTkCanvas(self.root, width=400, height=400)
        self.canvas.grid(row=0, column=0)

        # Dữ liệu mê cung
        self.maze_data = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 1],
            [1, 0, 1, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
        ]

        # Tạo đối tượng Maze và Player
        self.maze = Maze(self.maze_data, self.canvas)
        self.player = Player(self.maze, self.canvas, start_x=1, start_y=1)

        # Bắt sự kiện bàn phím
        self.root.bind("<KeyPress>", self.on_key_press)

    # Hàm xử lý sự kiện khi nhấn phím
    def on_key_press(self, event):
        direction = event.keysym
        if direction in ['Up', 'Down', 'Left', 'Right']:
            self.player.move(direction)

# Chạy ứng dụng
if __name__ == "__main__":
    app = ctk.CTk()
    MazeApp(app)
    app.mainloop()
    