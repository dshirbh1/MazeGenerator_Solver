# Maze Generation and Solving
Welcome to the Maze Generation and Solving project! This project involves generating mazes using a recursive backtracking algorithm and solving them using the A* algorithm. In this README, we will provide an overview of the project, its implementation, and how to use it.

## Overview
This Python program generates mazes and finds a path through them. It includes two main parts:

### Maze Generation (Recursive Backtracking): In this part, we generate a maze with a start point and an end point. The maze generation process involves carving pathways through the maze cells. We use a recursive backtracking algorithm to achieve this.

### Maze Solving (A* Algorithm): Once the maze is generated, we find the shortest path from the start to the end point. We utilize the A* algorithm to determine the optimal route through the maze.

## How to Use
Follow these steps to set up and use the maze generation and solving program:
1. Python environment with required libraries (e.g., pygame).
2. Clone this repository to your local machine:
3. Navigate to the project directory:
4. Make sure you have pygame installed:
pip install pygame
5. Run the Program
6. Follow the prompts to set the maze parameters, including height, width, cell size, start point (X and Y), and end point (X and Y).
7. The program will display the maze generation and solving process using the pygame window.

8. You can exit the program by closing the pygame window.

## Example Usage
Here is an example of how to use the program:

#### Maze Generation:

Input Maze Height: 10
Input Maze Width: 10
Input Cell Size: 40
Input Start Point (X): 0
Input Start Point (Y): 0
Input End Point (X): 9
Input End Point (Y): 9
This will generate a 10x10 maze with a starting point at (0, 0) and an ending point at (9, 9).

#### Maze Solving:

After maze generation, the program will automatically find and display the optimal path from the start to the end point.

## Program Features
1. Maze generation using recursive backtracking.
2. Pathfinding through the maze using the A* algorithm.
3. Visualization of the maze and the path in a pygame window.
4. Customizable maze dimensions and start/end points.
