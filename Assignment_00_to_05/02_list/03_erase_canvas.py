import tkinter as tk

# Canvas grid settings
GRID_SIZE = 10
CELL_SIZE = 40
ERASER_SIZE = 50

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Eraser")

        # Create canvas
        self.canvas = tk.Canvas(root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE)
        self.canvas.pack()

        # Draw the grid of blue rectangles
        self.cells = []
        for row in range(GRID_SIZE):
            row_cells = []
            for col in range(GRID_SIZE):
                x1, y1 = col * CELL_SIZE, row * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
                row_cells.append(rect)
            self.cells.append(row_cells)

        # Create eraser rectangle
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="gray", outline="black")

        # Bind mouse events
        self.canvas.bind("<B1-Motion>", self.erase)

    def erase(self, event):
        """Move the eraser and change touched cells to white."""
        x, y = event.x, event.y
        self.canvas.coords(self.eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)

        # Erase cells that the eraser touches
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x1, y1, x2, y2 = self.canvas.coords(self.cells[row][col])
                if self.check_collision(x, y, x + ERASER_SIZE, y + ERASER_SIZE, x1, y1, x2, y2):
                    self.canvas.itemconfig(self.cells[row][col], fill="white")

    def check_collision(self, x1, y1, x2, y2, r1, r2, r3, r4):
        """Check if two rectangles overlap."""
        return not (x2 < r1 or x1 > r3 or y2 < r2 or y1 > r4)

def main():
    root = tk.Tk()
    app = EraserApp(root)
    root.mainloop()

# This provided line is required at the end of Python file to call the main() function.
if __name__ == '__main__':
    main()
