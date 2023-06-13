#https://leetcode.com/problems/clone-graph/
#time O(V+E) space O(V)
#bfs dfs
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        visited = {None:None}
        def dfs(root):
            if root in visited:
                return visited[root]
            copy = Node(root.val)
            visited[root]=copy
            for n in root.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        return dfs(node)
            
                    



