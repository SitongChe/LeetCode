#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
#time O(n), space O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = n-1
        while l<r:
            sum = numbers[l]+numbers[r]
            if sum == target:
                return [l+1,r+1]
            if sum<target:
                l+=1
            else:
                r-=1
        return []
            
