#https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
#time O(N), space O(logN) (height of the tree)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0:
            return None
        root = TreeNode(preorder[0])
        pivot = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:pivot+1],inorder[0:pivot])
        root.right = self.buildTree(preorder[pivot+1:],inorder[pivot+1:])
        return root
