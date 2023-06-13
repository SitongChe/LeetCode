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
        if not root:
            return True
        def height(root):
            if not root:
                return 0
            l = height(root.left)
            if l == -1:
                return -1
            r = height(root.right)
            if r==-1 or abs(l-r)>1:
                return -1
            return max(l,r)+1
        if height(root)==-1:
            return False
        return True
