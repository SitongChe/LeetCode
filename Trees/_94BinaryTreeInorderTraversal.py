#https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#time O(N), space O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [[root,False]]
        ans = []
        while stack:
            cur,visited = stack.pop()
            if cur:
                if visited:
                    ans.append(cur.val)
                else:
                    stack.append([cur.right,False])
                    stack.append([cur,True])
                    stack.append([cur.left,False])
        return ans
        
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        ans += self.inorderTraversal(root.left)
        ans.append(root.val)
        ans += self.inorderTraversal(root.right)
        return ans
