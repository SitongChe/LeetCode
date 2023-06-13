#https://leetcode.com/problems/binary-tree-maximum-path-sum/
#time O(N), space O(logN) (height of the tree)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxSingle(root):
            if not root:
                return 0
            l = max(0,maxSingle(root.left))
            r = max(0,maxSingle(root.right))
            self.ans = max(self.ans,l+r+root.val)
            return max(l,r)+root.val
        self.ans = -inf
        maxSingle(root)
        return self.ans


