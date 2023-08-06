#https://leetcode.com/problems/permutations/
#time O(N!) space O(N)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def traceback():
            if len(tmp) == n:
                ans.append(tmp.copy())
                return
            for num in nums:
                if num in tmp:
                    continue
                tmp.append(num)
                traceback()
                tmp.pop()
        ans = []
        tmp = []
        n = len(nums)
        traceback()
        return ans
        
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def traceback(index):
            if index==n:
                ans.append(nums.copy())
                return
            for i in range(index,n):
                nums[i],nums[index]=nums[index],nums[i]
                traceback(index+1)
                nums[i],nums[index]=nums[index],nums[i]
        n = len(nums)
        ans = []
        traceback(0)
        return ans



                    



