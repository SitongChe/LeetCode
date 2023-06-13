#https://leetcode.com/problems/same-tree/
#time O(N*M), space O(logM+logN) (height of the tree)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        def isSame(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and isSame(p.left,q.left) and isSame(p.right,q.right)
        return isSame(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
        
#time O(N+M), space O(M+N)
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def treeToString(node):
            if not node:
                return '#'
            return str(node.val) + ',' + treeToString(node.left) + ',' + treeToString(node.right)

        mainTreeString = treeToString(root)
        subTreeString = treeToString(subRoot)

        return ','+subTreeString in mainTreeString or  subTreeString+',' in mainTreeString or subTreeString==mainTreeString
