#https://leetcode.com/problems/permutations/
#time O(N!) space O(N)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def traceback(index):
            if index==n-1:
                ans.append(nums.copy())
                return
            for i in range(index,n):
                nums[i],nums[index]=nums[index],nums[i]
                traceback(index+1)
                nums[i],nums[index]=nums[index],nums[i]
        traceback(0)
        return ans



                    



