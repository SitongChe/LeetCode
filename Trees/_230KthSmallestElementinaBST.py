#https://leetcode.com/problems/kth-smallest-element-in-a-bst/
#time O(N), space O(logN) (height of the tree)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        stack = [(root,False)]
        while stack:
            node,visited = stack.pop()
            if node:
                if visited:
                    k-=1
                    if k == 0:
                        return node.val
                else:
                    stack.append((node.right,False))
                    stack.append((node,True))
                    stack.append((node.left,False))

