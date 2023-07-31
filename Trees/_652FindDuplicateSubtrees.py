#https://leetcode.com/problems/find-duplicate-subtrees/description/
#time O(N), space O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def dfs(root):
            if not root:
                return "null"
            s = ",".join([str(root.val),dfs(root.left),dfs(root.right)])
            if len(subTreeSet[s])==1:
                ans.append(root)
            subTreeSet[s].append(root)
            return s
        subTreeSet = defaultdict(list)
        ans = []
        dfs(root)
        return ans
