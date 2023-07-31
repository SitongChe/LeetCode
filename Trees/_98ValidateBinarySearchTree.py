#https://leetcode.com/problems/same-tree/
#time O(N), space O(logN) (height of the tree)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = -inf
        self.ans = True
        def inorder(root):
            if not root:
                return True
            inorder(root.left)
            if root.val <= self.prev:
                self.ans=False
                return
            self.prev = root.val
            inorder(root.right)
        inorder(root)
        return self.ans
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [[root,False]]
        prev = None
        while stack:
            cur,visited = stack.pop()
            if cur:
                if visited:
                    if prev and prev.val>=cur.val:
                        return False
                    prev = cur
                else:
                    stack.append([cur.right,False])
                    stack.append([cur,True])
                    stack.append([cur.left,False])
        return True



