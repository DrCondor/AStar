#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Loading classes from other files
from graph import Graph
from astar import AStar

# Loading txt file with maze
maze_file = open('maze.txt', 'r+')
maze = maze_file.readlines()
maze_file.close()

# Parsing maze to matrix of nodes
graph = Graph(maze)

# Generating AStar object
astar = AStar(graph.start, graph.stop)

# Searching for path
path = astar.search()

# Printing path
for element in graph.to_s(path):
        print ''.join(element)