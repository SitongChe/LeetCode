#https://leetcode.com/problems/find-bottom-left-tree-value/description/
#time O(n), space O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [root]
        ans = 0
        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.pop(0)
                if i == 0:
                    ans = cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return ans
                
