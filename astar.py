#!/usr/bin/env python
# -*- coding: utf-8 -*- 

class AStar:
  def __init__(self, start, stop):

    # Fetching starting and stopping node
    self.start = start
    self.stop = stop

    # Open set - unexplored nodes
    self.openset = [self.start]

    # Closed set - explored nodes
    self.closedset = []

    # Initializing starting point
    self.start.g = 0

    # Evaluating distance from the ending point
    self.start.h = self.start.distance(self.stop)

  def search(self):
    while len(self.openset) > 0:

      # Looking for node with minimum distance from start and minimum distance from stop
      x = self.__openset_min_f()

      # Finish lime
      if x == self.stop:
        return self.__reconstruct_path(x)

      # Moving Node from open set to closed set
      self.openset.remove(x)
      self.closedset.append(x)

      # Test all nodes if they are near to the x
      for y in x.near:
        if y == None:
          continue
        if y in self.closedset:
          continue

        g_score = x.g + x.distance(y)

        # Y is a new node for the openset
        if y not in self.openset:
          # count_flag = count_flag + 1
          self.openset.append(y)
          improving = True
        # Y was in open set, with smaller g value - this means that current route is faster
        elif g_score < y.g:
          improving = True
        #  G score is higher and current path is not any better than previous one
        else:
          improving = False
        
        if improving == True:
          # Next move
          y.prev = x
          # Updating g_score
          y.g = g_score
          # Updating heuristic distance from stop
          y.h = y.distance(self.stop)

    return []

  def __openset_min_f(self):
    ret = self.openset[0]

    for i in range(1, len(self.openset)):
      if ret.f() > self.openset[i].f():
        ret = self.openset[i]
    
    return ret

  def __reconstruct_path(self, curr):
    if curr.prev != None:
      return self.__reconstruct_path(curr.prev) + [curr]
    else:
      return []