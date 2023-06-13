#https://leetcode.com/problems/two-sum/
#time O(N),space O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = defaultdict()
        for i in range(len(nums)):
            index = map.get(target-nums[i],-1)
            if index!=-1:
                return [i,index]
            map[nums[i]]=i
        return [-1,-1]


