# Salesman Variations

Variation of the traveling salesman problem.

# Basic Usage

```paths.py```

Finds the best (shortest) path (not loop) through randomly placed nodes.
Algorithm is brute force, so keep number of nodes to < 9 to keep runtime under 1 second.
In addition plotting the nodes and the best path, the program outputs a histogram
showing the distribution of lengths of all possible paths.

```rand_hub.py```

Randomly splits the nodes into two groups (of roughly equal size) with one shared node,
then finds the best path for each of the two groups independently.
Keep number of nodes to < 16 to keep runtime under 1 second.

```multi_paths.py```

Finds the best path using two lines. Rules: The two lines must share exactly one point.
All points must be on a line. The best path is the one with the shortest total length.
Note this take much longer to compute than the other files. Keep number of nodes < 7
for runtime under 1 second. Results may look quite different, partially dependent on
number of nodes. For instance, sometimes a single line is the best path. With more
nodes, this is less likely to be the case.

# Requirements

Python 3.6.7

matplotlib 2.1.1
