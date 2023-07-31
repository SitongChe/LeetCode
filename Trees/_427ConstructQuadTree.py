#https://leetcode.com/problems/construct-quad-tree/description/
#time O(N^2) space O(N^2)

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n,l,r):
            total = 0
            for i in range(n):
                for j in range(n):
                    total += grid[l+i][r+j]
            if total == n*n or total == 0:
                return Node(grid[l][r],True)
            topLeft = dfs(n//2,l,r)
            topRight = dfs(n//2,l,r+n//2)
            bottomLeft = dfs(n//2,l+n//2,r)
            bottomRight = dfs(n//2,l+n//2,r+n//2)
            return Node(0,False,topLeft,topRight,bottomLeft,bottomRight)
            
        n = len(grid)
        return dfs(n,0,0)
