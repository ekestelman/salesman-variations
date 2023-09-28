# Salesman Variations

Variation of the traveling salesman problem where two salesman must meet at one node.

## Basic Usage

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

## Screenshots

### Lone Salesman

In the figures below, the left plot shows randomly placed nodes and the shortest path connecting them. The right plot shows a histogram of all possible path lengths. The _x_-axis shows path length. The _y_-axis shows number of possible paths within a bin.

The possible path lengths for a single salesman traversing 8 nodes can produce strange distributions.

![](https://github.com/ekestelman/salesman-variations/blob/main/Salesman%20Images/path-dist-polymodal.png?raw=true)

When traversing 11 nodes, the distribution of possible paths looks more normal.

![](https://github.com/ekestelman/salesman-variations/blob/main/Salesman%20Images/path-dist-polymodal.png?raw=true)

### Two Salesmen

Sometimes a second salesman helps only a little.

![](https://github.com/ekestelman/salesman-variations/blob/main/Salesman%20Images/paths-7.png?raw=true)
![](https://github.com/ekestelman/salesman-variations/blob/main/Salesman%20Images/paths-8c.png?raw=true)

Sometimes having a second salesman makes no difference. A lone salesman could have accomplished these two examples.

![](https://github.com/ekestelman/salesman-variations/blob/main/Salesman%20Images/paths-8.png?raw=true)
![](https://github.com/ekestelman/salesman-variations/blob/main/Salesman%20Images/paths-8b.png?raw=true)

This salesman was a big help.

![](https://github.com/ekestelman/salesman-variations/blob/main/Salesman%20Images/two_lines_salesman.png?raw=true)

## Requirements

Python 3.6.7

matplotlib 2.1.1
