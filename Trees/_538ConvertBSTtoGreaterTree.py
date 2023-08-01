#https://leetcode.com/problems/convert-bst-to-greater-tree/description/
#time O(N), space O(logN) (height of the tree)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(root):
            if not root:
                return None
            inorder(root.right)
            root.val += self.prevTotal
            self.prevTotal = root.val
            inorder(root.left)
            return root
        self.prevTotal = 0
        return inorder(root)
