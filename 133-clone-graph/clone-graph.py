"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        queue = deque()
        queue.append(node)
        node2 = Node(node.val)
        hash_map = {node: node2}

        while queue:
            temp = queue.popleft()
            
            for neighbor in temp.neighbors:
                if neighbor not in hash_map:
                    new = Node(neighbor.val)
                    hash_map[neighbor] = new
                    hash_map[temp].neighbors.append(new)
                    queue.append(neighbor)
                else:
                    hash_map[temp].neighbors.append(hash_map[neighbor])
                
        return node2