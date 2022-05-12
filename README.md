# Salesman Variations

Variation of the traveling salesman problem.

# Basic Usage

'''paths.py'''

Finds the best (shortest) path (not loop) through randomly placed nodes.
Algorithm is brute force, so keep number of nodes to < 9 to keep runtime under 1 second.
In addition plotting the nodes and the best path, the program outputs a histogram
showing the distribution of lengths of all possible paths.

'''multi_paths.py'''

Randomly splits the nodes into two groups (of roughly equal size) with one shared node,
then finds the best path for each of the two groups independently.
Keep number of nodes to < 16 to keep runtime under 1 second.

# Requirements

Python 3.6.7

matplotlib 2.1.1
