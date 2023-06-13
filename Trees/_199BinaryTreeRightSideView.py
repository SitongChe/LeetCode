#https://leetcode.com/problems/binary-tree-right-side-view/
#time O(N), space O(M), where M is the maximum number of nodes at any level in the binary tree. In the worst case, when the binary tree is a complete binary tree, the maximum number of nodes at any level is approximately N/2. Therefore, the space complexity is O(N/2) ≈ O(N) in the worst case. 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        ans = []
        while queue:
            n = len(queue)
            for i in range(n):
                cur = queue.pop(0)
                if i == n-1:
                    ans.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return ans
