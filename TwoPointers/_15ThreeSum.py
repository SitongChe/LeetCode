#https://leetcode.com/problems/3sum/
#time O(n^2), space O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            if i-1>=0 and nums[i]==nums[i-1]:
                continue
            if nums[i]>0:
                break
            l = i+1
            r = n-1
            while l<r:
                sum = nums[i]+nums[l]+nums[r]
                if sum == 0:
                    ans.append([nums[i],nums[l],nums[r]])
                    while l+1<r and nums[l]==nums[l+1]:
                        l+=1
                    l+=1
                    r-=1
                elif sum<0:
                    l+=1
                else:
                    r-=1
        return ans
        
                
