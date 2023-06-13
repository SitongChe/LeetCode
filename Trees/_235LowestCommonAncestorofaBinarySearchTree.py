#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
#time O(logN) in best case, O(N) in worst case, space O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        cur = root
        while cur:
            if cur.val<min(p.val,q.val):
                cur = cur.right
            elif cur.val>max(p.val,q.val):
                cur = cur.left
            else:
                return cur
