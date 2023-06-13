#https://leetcode.com/problems/binary-tree-level-order-traversal/
#time O(N), space  O(M), where M is the maximum number of nodes at any level in the binary tree. In the worst case, when the binary tree is a complete binary tree, the maximum number of nodes at any level is approximately N/2. Therefore, the space complexity is O(N/2) ≈ O(N) in the worst case. 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = [root]
        while queue:
            n = len(queue)
            tmp = []
            for i in range(n):
                cur = queue.pop(0)
                tmp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            ans.append(tmp)
        return ans

