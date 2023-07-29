#https://leetcode.com/problems/balanced-binary-tree/
#time O(N), space O(logN) (height of the tree)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            l = height(root.left)
            r = height(root.right)
            if l == -1 or r == -1 or abs(r-l)>1:
                return -1
            return max(r,l)+1
        if not root:
            return True
        return height(root)!=-1
