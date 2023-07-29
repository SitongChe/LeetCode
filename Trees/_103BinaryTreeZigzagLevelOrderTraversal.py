#https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#time O(N), space O(logN) (height of the tree)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = [root]
        while queue:
            size = len(queue)
            tmp = []
            for i in range(size):
                cur = queue.pop(0)
                tmp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            if len(ans)%2:
                tmp.reverse()
            ans.append(tmp)
        return ans

                


            
