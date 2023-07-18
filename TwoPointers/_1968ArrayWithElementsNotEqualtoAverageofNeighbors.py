#https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/description/
#time O(nlogn), space O(n)
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        l = 0
        r = n-1
        ans = []
        while l<=r:
            ans.append(nums[l])
            l+=1

            if (l<=r):
                ans.append(nums[r])
                r-=1
        return ans

