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
        def findKSum(start,end,k,target,tmp):
            if end-start<k or nums[start]*k>target or nums[end-1]*k<target:
                return
            if k==2:
                l = start
                r = end-1
                while l<r:
                    cur = nums[l]+nums[r]
                    if cur==target:
                        ans.append(tmp.copy()+[nums[l],nums[r]])
                        while l<r and nums[l+1]==nums[l]:
                            l+=1
                        l+=1
                        r-=1
                    elif cur<target:
                        l+=1
                    else:
                        r-=1
            else:
                for i in range(start,end):
                    if i>start and nums[i]==nums[i-1]:
                        continue
                    findKSum(i+1,end,k-1,target-nums[i],tmp+[nums[i]])
        ans = []
        nums.sort()
        findKSum(0,len(nums),4,target,[])
        return ans
        
