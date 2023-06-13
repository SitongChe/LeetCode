#https://leetcode.com/problems/count-good-nodes-in-binary-tree/
#time O(N), space O(logN) (height of the tree)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count(root,max):
            if not root:
                return 0
            ans = 0
            if root.val>=max:
                max = root.val
                ans+=1
            ans += count(root.left,max)
            ans += count(root.right,max)
            return ans
        return count(root,root.val)
