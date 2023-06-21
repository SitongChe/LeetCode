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
        


                    



