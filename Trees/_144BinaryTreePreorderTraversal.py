#https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#time O(N), space O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
                    stack.append([cur.left,False])
                    stack.append([cur,True])
        return ans
        
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        ans.append(root.val)
        ans += self.preorderTraversal(root.left)
        ans += self.preorderTraversal(root.right)
        return ans

