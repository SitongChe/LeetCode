#https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#time O(N), space O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans=[]
        stack=[[root,False]]
        while stack:
            cur,visited = stack.pop()
            if cur:
                if visited:
                    ans.append(cur.val)
                else:
                    stack.append([cur,True])
                    stack.append([cur.right,False])
                    stack.append([cur.left,False])
        return ans
        
        
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans=[]
        ans += self.postorderTraversal(root.left)
        ans += self.postorderTraversal(root.right)
        ans.append(root.val)
        return ans

