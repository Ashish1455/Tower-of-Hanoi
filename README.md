# Tower of Hanoi Visualizer

## Overview

This project provides a graphical visualization of the Tower of Hanoi puzzle with support for n-tower configurations. The traditional Tower of Hanoi puzzle uses 3 towers, but this implementation allows for 3-7 towers.

## Features

- Interactive GUI built with Tkinter
- Support for 1-15 discs
- Support for 3-7 towers
- Adjustable animation speed
- Step-by-step visualization
- Play, pause, and navigation controls
- Color-coded discs for better visualization


## Files

- **main.py**: Entry point for the application
- **n_Tower_of_Hanoi.py**: Core implementation of the Tower of Hanoi algorithm and Stack data structure
- **visualizer.py**: GUI implementation for visualizing the Tower of Hanoi solution


## How to Use

1. Run `main.py` to start the application
2. Set the number of discs (1-15)
3. Set the number of towers (3-7)
4. Adjust the animation speed as needed
5. Click "Start" to initialize the visualization
6. Use the control buttons to navigate through the solution:
    - "Play" to start automatic animation
    - "Pause" to temporarily halt the animation
    - "Next" to move forward one step
    - "Prev" to move backward one step
    - "Reset" to clear the current visualization

## Algorithm

The program implements a generalized Tower of Hanoi algorithm that works with n towers. For the traditional 3-tower case, it uses the standard recursive algorithm. For more than 3 towers, it employs a more complex approach that utilizes intermediate towers efficiently.

## Requirements

- Python 3.6+
- Tkinter (usually included with Python)


## Installation

No special installation is required beyond having Python and Tkinter installed. Simply download the files and run `main.py`.

```bash
python main.py
```


## Last Updated

March 18, 2025

<div style="text-align: center">⁂</div>

[^1]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/53962354/f2eba586-8791-46e8-9324-1f67b1b2ca29/EX-1.5-n-Tower-of-Hanoi.py

[^2]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/53962354/47387cf7-c9a5-426c-b4bf-7387eb0d73a2/paste-2.txt

