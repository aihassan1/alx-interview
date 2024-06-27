Island Perimeter Project - README
This document provides an overview of the "Island Perimeter" project, including the task description, required concepts, resources, and solution implementation details.

Project Description

This project challenges you to calculate the perimeter of a single island within a grid represented by a 2D list of integers in Python.

Concepts Needed

2D Arrays (Matrices):
Accessing and iterating over elements
Navigating through adjacent cells (horizontally and vertically)
Conditional Logic:
Determining if a cell contributes to the island's perimeter
Counting Techniques:
Counting edges contributing to the perimeter
Problem-Solving Strategies:
Breaking down the problem into smaller tasks
Identifying land cells and calculating their perimeter contribution
Python Programming:
Nested loops for iterating over grid cells
Conditional statements to check adjacent cell status
Resources

Python Official Documentation: Nested Lists
GeeksforGeeks: Python Multi-dimensional Arrays
TutorialsPoint: Python Lists (https://www.tutorialspoint.com/python_data_structure/python_lists_data_structure.htm)
YouTube Tutorials: Python 2D arrays and lists
Solution Implementation

Create a function island_perimeter(grid) that takes a 2D list grid as input:

grid: List of lists of integers.
0 represents water
1 represents land
The function should return the perimeter of the island in the grid.
Implement logic to iterate over the grid and identify land cells.

For each land cell, check its adjacent cells (up, down, left, right) and count the edges bordering water. These edges contribute to the perimeter.

Return the total count of perimeter edges.

Additional Notes

The code should adhere to PEP 8 style guidelines (version 1.7).
No external modules are allowed for import.
Include a README.md file with project details.
Example Usage (Provided in 0-main.py):

Python
grid = [
[0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[0, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0]
]

island_perimeter = **import**('0-island_perimeter').island_perimeter

print(island_perimeter(grid)) # Output: 12
