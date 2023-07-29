#https://leetcode.com/problems/symmetric-tree/description/
#time O(N), space O(logN) (height of the tree)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSame(p,q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return isSame(p.right,q.left) and isSame(p.left,q.right)
        if not root:
            return True
        return isSame(root.left,root.right)
            
