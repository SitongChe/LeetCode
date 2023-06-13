#https://leetcode.com/problems/same-tree/
#time O(N), space O(logN) (height of the tree)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = -inf
        self.ans = True
        def inorder(root):
            if not root:
                return True
            inorder(root.left)
            if root.val <= self.prev:
                self.ans=False
                return
            self.prev = root.val
            inorder(root.right)
        inorder(root)
        return self.ans

