#https://leetcode.com/problems/maximum-width-of-binary-tree/description/
#time O(N), space O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [[root,1]]
        prevNum = 0
        ans = 0
        while queue:
            size = len(queue)
            for i in range(size):
                cur,num = queue.pop(0)
                if i == 0:
                    prevNum = num
                ans = max(ans,num-prevNum+1)
                if cur.left:
                    queue.append([cur.left,2*num])
                if cur.right:
                    queue.append([cur.right,2*num+1])
        return ans

            
