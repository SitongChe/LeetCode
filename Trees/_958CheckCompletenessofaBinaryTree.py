#https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/
#time O(N) space O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = [root]
        while queue:
            cur = queue.pop(0)
            if cur:
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                while queue:
                    if queue.pop(0):
                        return False
        return True
