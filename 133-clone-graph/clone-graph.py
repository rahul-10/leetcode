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

        queue = deque([node])
        hash_map = {node: Node(node.val)}

        while queue:
            temp = queue.popleft()
            for neighbor in temp.neighbors:
                if neighbor not in hash_map:
                    hash_map[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                hash_map[temp].neighbors.append(hash_map[neighbor])
                
        return hash_map[node]