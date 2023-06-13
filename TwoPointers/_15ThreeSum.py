#https://leetcode.com/problems/3sum/
#time O(n^2), space O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        if n ==0:
            return []
        ans = []
        for i in range(n):
            if nums[i]>0:
                return ans
            if(i-1>=0 and nums[i]==nums[i-1]):
                continue
            j = i+1
            k = n-1
            while j<k:
                sum = nums[i]+nums[j]+nums[k]
                if sum==0:
                    ans.append([nums[i],nums[j],nums[k]])
                    while(j+1<k and nums[j]==nums[j+1]):
                        j+=1
                    j+=1
                    k-=1
                elif sum<0:
                    j+=1
                else:
                    k-=1
            
        return ans

        
                
