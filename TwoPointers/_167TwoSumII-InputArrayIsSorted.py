#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
#time O(n), space O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        if n == 0:
            return []
        i = 0
        j = n-1
        while i<j:
            sum = numbers[i]+numbers[j]
            if sum<target:
                i+=1
            elif sum>target:
                j-=1
            else:
                return [i+1,j+1]
        return []
