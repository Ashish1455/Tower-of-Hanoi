import tkinter as tk
from tkinter import ttk
import threading
import time
from n_Tower_of_Hanoi import Stack, solve_hanoi

class TowerOfHanoiVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Tower of Hanoi Visualizer")
        self.root.geometry("1200x700")
        self.setup_ui()
        self.towers = []
        self.animation_speed = 0.5
        self.moves = []
        self.current_move = 0
        self.auto_play = False
        self.paused = False
        self.animation_thread = None

    def setup_ui(self):
        # Input frame
        input_frame = ttk.Frame(self.root, padding="10")
        input_frame.pack(fill=tk.X)

        ttk.Label(input_frame, text="Number of Discs:").grid(row=0, column=0, padx=5, pady=5)
        self.disc_var = tk.IntVar(value=3)
        ttk.Spinbox(input_frame, from_=1, to=15, textvariable=self.disc_var, width=5).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Number of Towers:").grid(row=0, column=2, padx=5, pady=5)
        self.tower_var = tk.IntVar(value=3)
        ttk.Spinbox(input_frame, from_=3, to=7, textvariable=self.tower_var, width=5).grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(input_frame, text="Animation Speed:").grid(row=0, column=4, padx=5, pady=5)
        self.speed_var = tk.DoubleVar(value=0.5)
        ttk.Scale(input_frame, from_=0.1, to=2.0, orient=tk.HORIZONTAL, variable=self.speed_var, length=100).grid(row=0, column=5, padx=5, pady=5)

        ttk.Button(input_frame, text="Start", command=self.start_visualization).grid(row=0, column=6, padx=5, pady=5)
        ttk.Button(input_frame, text="Reset", command=self.reset).grid(row=0, column=7, padx=5, pady=5)

        # Control frame
        control_frame = ttk.Frame(self.root, padding="10")
        control_frame.pack(fill=tk.X)

        ttk.Button(control_frame, text="<< Prev", command=self.prev_move).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Next >>", command=self.next_move).pack(side=tk.LEFT, padx=5)

        # Auto play button
        self.play_button = ttk.Button(control_frame, text="▶ Play", command=self.toggle_auto_play)
        self.play_button.pack(side=tk.LEFT, padx=5)


        self.move_label = ttk.Label(control_frame, text="Move: 0/0")
        self.move_label.pack(side=tk.LEFT, padx=20)

        # Canvas for visualization
        self.canvas = tk.Canvas(self.root, bg="white", height=400)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def start_visualization(self):
        # Get user inputs and validate them
        num_discs = self.disc_var.get()
        num_towers = self.tower_var.get()

        # Validate disc range (1-15)
        if num_discs < 1:
            num_discs = 1
            self.disc_var.set(1)
        elif num_discs > 15:
            num_discs = 15
            self.disc_var.set(15)

        # Validate tower range (3-7)
        if num_towers < 3:
            num_towers = 3
            self.tower_var.set(3)
        elif num_towers > 7:
            num_towers = 7
            self.tower_var.set(7)

        # Check if towers and discs make sense together
        if num_towers == 2 and num_discs > 1:
            num_discs = 1
            self.disc_var.set(1)

        self.animation_speed = self.speed_var.get()
        self.reset()
        self.initialize_towers(num_discs, num_towers)
        self.calculate_moves(num_discs, num_towers)
        self.draw_towers()

    def reset(self):
        self.stop_animation()
        self.towers = []
        self.moves = []
        self.current_move = 0
        self.canvas.delete("all")
        self.move_label.config(text="Move: 0/0")
        self.play_button.config(text="▶ Play")
        self.auto_play = False

    def initialize_towers(self, num_discs, num_towers):
        self.towers = []
        for i in range(num_towers):
            temp = Stack[int]()
            self.towers.append(temp)
        
        for i in range(num_discs, 0, -1):
            self.towers[0].push(i)

    def record_state(self, description):
        state = []
        for tower in self.towers:
            state.append(tower.get_items().copy())
        self.moves.append((state, description))

    def calculate_moves(self, num_discs, num_towers):
        # Record the initial state
        self.record_state("Initial state")
        
        # Create a custom move recorder function to pass to solve_hanoi
        def move_recorder(from_tower, to_tower):
            disc = from_tower.pop()
            to_tower.push(disc)
            
            # Find the indices of the towers
            from_idx = self.towers.index(from_tower)
            to_idx = self.towers.index(to_tower)
            
            self.record_state(f"Move disc from Tower {from_idx+1} to Tower {to_idx+1}")
        
        # Use the solve_hanoi function from n_Tower_of_Hanoi.py
        solve_hanoi(self.towers, 0, num_towers-1, num_discs, num_towers, move_recorder)
        
        # Update the move label
        self.move_label.config(text=f"Move: {self.current_move}/{len(self.moves)-1}")

    def draw_towers(self):
        self.canvas.delete("all")

        # Get the current state
        if self.current_move < len(self.moves):
            state, description = self.moves[self.current_move]
        else:
            return

        # Draw the description
        self.canvas.create_text(400, 30, text=description, font=("Arial", 12))

        # Calculate dimensions
        num_towers = len(state)
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        tower_width = 10
        tower_height = 330
        tower_spacing = canvas_width / (num_towers + 1)
        base_y = canvas_height - 100
        max_disc_width = tower_spacing * 0.8

        # Draw the base
        self.canvas.create_rectangle(50, base_y, canvas_width-50, base_y+10, fill="brown")

        # Draw each tower and its discs
        for i in range(num_towers):
            # Tower position
            tower_x = (i + 1) * tower_spacing
            
            # Draw the tower
            self.canvas.create_rectangle(tower_x - tower_width/2, base_y - tower_height,
                                        tower_x + tower_width/2, base_y, fill="gray")
            
            # Draw the discs
            discs = state[i]
            for j, disc_size in enumerate(discs):
                # Calculate disc dimensions
                disc_width = max_disc_width * (disc_size / self.disc_var.get())
                disc_height = 20
                disc_y = base_y - (j + 1) * disc_height
                
                self.canvas.create_rectangle(tower_x - disc_width/2, disc_y - disc_height,
                                            tower_x + disc_width/2, disc_y,
                                            fill=self.get_disc_color(disc_size))
                
                # Add disc number
                self.canvas.create_text(tower_x, disc_y - disc_height/2, text=str(disc_size), fill="white")
        
        # Draw tower numbers
        for i in range(num_towers):
            tower_x = (i + 1) * tower_spacing
            self.canvas.create_text(tower_x, base_y + 30, text=f"Tower {i+1}", font=("Arial", 10))

    def get_disc_color(self, size):
        # Generate a color based on the disc size
        colors = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#9400D3",
                "#FF1493", "#00FFFF", "#FF00FF"]
        return colors[(size - 1) % len(colors)]

    def next_move(self):
        if self.current_move < len(self.moves) - 1:
            self.current_move += 1
            self.move_label.config(text=f"Move: {self.current_move}/{len(self.moves)-1}")
            self.draw_towers()

    def prev_move(self):
        if self.current_move > 0:
            self.current_move -= 1
            self.move_label.config(text=f"Move: {self.current_move}/{len(self.moves)-1}")
            self.draw_towers()

    def toggle_auto_play(self):
        if self.auto_play:
            self.stop_animation()
        else:
            self.auto_play = True
            self.paused = False
            self.play_button.config(text="⏸ Pause")
            
            # Start animation in a separate thread
            self.animation_thread = threading.Thread(target=self.animate_moves)
            self.animation_thread.daemon = True
            self.animation_thread.start()

    def stop_animation(self):
        self.auto_play = False
        self.paused = False
        self.play_button.config(text="▶ Play")
        
        # Wait for animation thread to finish
        if self.animation_thread and self.animation_thread.is_alive():
            self.animation_thread.join(0.1)

    def animate_moves(self):
        while self.auto_play and self.current_move < len(self.moves) - 1:
            if not self.paused:
                # Use after() to update UI from the main thread
                self.root.after(0, self.next_move)
                time.sleep(1 / self.speed_var.get())
            else:
                time.sleep(0.1)  # Sleep while paused
        
        # If we reached the end, reset the play button
        if self.current_move >= len(self.moves) - 1:
            self.root.after(0, lambda: self.play_button.config(text="▶ Play"))
            self.root.after(0, lambda: self.pause_button.config(state=tk.DISABLED))
            self.auto_play = False
