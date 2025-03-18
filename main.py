import tkinter as tk
from n_Tower_of_Hanoi import Stack
from visualizer import TowerOfHanoiVisualizer

if __name__ == "__main__":
    root = tk.Tk()
    app = TowerOfHanoiVisualizer(root)
    root.mainloop()
