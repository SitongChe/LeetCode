#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#time O(N), space O(logN) (height of the tree)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left,right):
            if left>right:
                return None
            mid = left+(right-left)//2
            root = TreeNode(nums[mid])
            root.left = build(left,mid-1)
            root.right = build(mid+1,right)
            return root
        n = len(nums)
        if n == 0:
            return None
        return build(0,n-1)
        
