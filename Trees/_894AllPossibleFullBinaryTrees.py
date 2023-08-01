#https://leetcode.com/problems/all-possible-full-binary-trees/description/
#time O(n*2^(n-1)), space O(n*2^(n-1))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(n):
            if n in mp:
                return mp[n]
            total = []
            for i in range(1,n,2):
                l = dfs(i)
                r = dfs(n-i-1)
                for left in l:
                    for right in r:
                        total.append(TreeNode(0,left,right))
            mp[n]=total
            return total
        mp = defaultdict(list)
        mp[1].append(TreeNode())
        return dfs(n)


