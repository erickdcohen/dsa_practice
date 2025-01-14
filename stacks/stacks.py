"""
Implements stacks class
"""

from collections import deque

class Stack:
    def __init__(self, *elements):
        self._elements = deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while(len(self)) > 0:
              yield self.dequeue()

    def dequeue(self):
        return self._elements.pop()
