#https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
#time O(N), space O(logN)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            if self.prev:
                self.ans = min(self.ans, abs(root.val-self.prev.val))
            self.prev = root
            inorder(root.right)
        self.prev = None
        self.ans = inf
        inorder(root)
        return self.ans
