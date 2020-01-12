#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from node import Node
import numpy as np

class Graph:
  def __init__(self, d, start = "A", stop = "B", obst = "#", empty = " ", out = "*"):

    self.a = start
    self.b = stop
    self.o = obst
    self.s = empty
    self.p = out

    # Parsing file content into matrix of chars
    self.str = []
    for idx, val in enumerate(d):
      self.str.append(list(d[idx].rstrip()))

    self.rows = len(self.str)
    self.cols = len(self.str[0])

    # Creating empty matrix
    self.maze = [[0 for i in range(self.cols)] for j in range(self.rows)]

    # Finding cordinates of start and stop
    start_location = [(index, row.index('A')) for index, row in enumerate(self.str) if 'A' in row]
    stop_location = [(index, row.index('B')) for index, row in enumerate(self.str) if 'B' in row]

    # Creating Nodes for start and stop
    self.start = Node(start_location[0][0], start_location[0][1])
    self.stop = Node(stop_location[0][0], stop_location[0][1])

    # Filling empty spaces + start and stop with nodes
    for x, row in enumerate(self.str):
      for y, val in enumerate(row):
        if val == self.a:
          self.maze[x][y] = self.start
        if val == self.b:
          self.maze[x][y] = self.stop
        if val == self.o:
          self.maze[x][y] = None
        if val == self.s:
          self.maze[x][y] = Node(x, y)

    # Find neighbour nodes - possible path
    for x, row in enumerate(self.maze):
      for y, val in enumerate(row):
        if val == None:
          continue
        neighbours = [[x + 1, y], [x, y + 1], [x - 1, y], [x, y - 1]]

        for n in neighbours:
          val.near.append(self.maze[n[0]][n[1]])

  # Convert array of Nodes to array od chars
  def to_s(self, path = []):
    result = self.str
    if path:
      for n in path[:-1]:
        result[n.r][n.c] = self.p

    return(result)