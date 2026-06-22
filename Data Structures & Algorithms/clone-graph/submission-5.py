"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_new_mapping = {}
        
        def dfs(node):
            if not node:
                return
            if node in old_new_mapping:
                return old_new_mapping[node]
            new_node = Node(node.val)
            old_new_mapping[node] = new_node

            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            return new_node
        return dfs(node)