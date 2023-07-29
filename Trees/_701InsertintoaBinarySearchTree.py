#https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
#time O(logN) space O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        cur = root
        prev = root
        while cur:
            prev = cur
            if cur.val<val:
                cur = cur.right
            else:
                cur = cur.left
        if prev.val>val:
            prev.left = TreeNode(val)
        else:
            prev.right = TreeNode(val)
        return root
