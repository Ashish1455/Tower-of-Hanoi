# Tower of Hanoi (Multi-Tower Implementation)

This project is a Python implementation of the Tower of Hanoi puzzle that supports a customizable number of towers. It uses a recursive algorithm to solve the puzzle while printing the state of each tower after every move.

## Overview

The Tower of Hanoi is a classic mathematical puzzle where the objective is to move a set of disks from one tower (or rod) to another. This implementation generalizes the puzzle by allowing more than the standard three towers.

The program uses:
- **Generic Stack Class**: A custom `Stack` class implemented with Python's type hints.
- **Recursive Algorithms**: Two functions, `hanoi` and `hanoi3`, manage the recursive movement of disks:
  - `hanoi`: Handles the initial distribution of disks across multiple towers.
  - `hanoi3`: Implements the standard three-tower recursive solution for the remaining disks.

## Requirements

- Python 3.x

No additional packages are required.

# Tower of Hanoi Solver

## How to Run

### 1. Open and Run the File

Open the `hanoi.py` file directly in your code editor or terminal. Then run the file using:

```sh
python hanoi.py
```

### 2. Follow the Prompts

The program will ask for:

- **Number of Disks:** The total disks to move.
- **Number of Towers:** The total towers to be used in the puzzle.
  
Enter the required numbers and watch the puzzle solve step-by-step as it prints the state of the towers.

---

## Code Structure

### **Stack Class**
A generic stack data structure to manage the disks.

### **Recursive Functions**
- **`hanoi`**: Distributes disks among the towers and prepares for the recursive solution.
- **`hanoi3`**: Implements the classic three-tower recursive algorithm for moving disks.

---

## Example
When running the script, you might see an output like:

```sh
[5, 4, 3, 2, 1] [] []
...
```
Each step prints the state of all towers until the puzzle is solved.

---

## Future Enhancements
- **Graphical Visualization**: Integrate a GUI to visually show the moves.
- **Input Validation**: Add error handling for non-integer or invalid inputs.
- **Algorithm Optimization**: Explore enhancements for performance with additional towers.

---

## License
This project is licensed under the **MIT License**.

---

## Author
**Ashish1455**
