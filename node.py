#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import numpy as np

class Node:
  def __init__(self, r, c):

    self.r = r
    self.c = c

    self.g = 0.0
    self.h = 0.0

    self.prev = None
    self.near = []

  # Total heuristic distance
  def f(self):
    return self.g + self.h

  # Evaluated distance betwee two nodes
  def distance(self, n):
    return (
      (self.r - n.r) ** 2 +
      (self.c - n.c) ** 2
    ) ** (0.5)
