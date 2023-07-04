#https://leetcode.com/problems/4sum/description/
#time O(n^3), space O(1)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            if i-1>=0 and nums[i-1]==nums[i]:
                continue
            for j in range(i+1,n):
                if j-1>=i+1 and nums[j-1]==nums[j]:
                    continue
                l = j+1
                r = n-1
                while l<r:
                    sum = nums[i]+nums[j]+nums[l]+nums[r]
                    if sum == target:
                        ans.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                    elif sum<target:
                        l+=1
                    else:
                        r-=1
        return ans
        

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findNSum(nums,target,N,result,results):
            if len(nums)<N or N<2 or target<nums[0]*N or target>nums[-1]*N:
                return
            if N == 2:
                l=0
                r=len(nums)-1
                while l<r:
                    sum = nums[l]+nums[r]
                    if sum == target:
                        results.append(result+[nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                    elif sum<target:
                        l+=1
                    else:
                        r-=1
            else:
                for i in range(len(nums)-N+1):
                    if i-1>=0 and nums[i-1]==nums[i]:
                        continue
                    findNSum(nums[i+1:],target-nums[i],N-1,result+[nums[i]],results)
        results = []
        nums.sort()
        findNSum(nums,target,4,[],results)
        return results
