#https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#time O(N^2), space O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(postorder)
        if n==0:
            return None
        root = TreeNode(postorder[-1])
        pivot = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[0:pivot],postorder[0:pivot])
        root.right = self.buildTree(inorder[pivot+1:],postorder[pivot:n-1])
        return root
        
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(index,left,right):
            if left>right:
                return None
            if index<0:
                return None
            root = TreeNode(postorder[index])
            pivot = mp[postorder[index]]
            root.left = build(index-(right-pivot+1),left,pivot-1)
            root.right = build(index-1,pivot+1,right)
            return root
        mp = defaultdict()
        n = len(inorder)
        for i in range(n):
            mp[inorder[i]]=i
        return build(n-1,0,n-1)
        
