#Problem: Given an array, find the two indices that sum to a specific value.

Constraints
Is there exactly one solution?
Yes
Is there always a solution?
Yes
Is the array an array of ints?
Yes
Is the array sorted? No
Are negative values possible?
Yes
Can we assume the inputs are valid?
No
Can we assume this fits memory?
Yes

Test Cases
None input -> TypeError
[] -> ValueError
[1, 3, 2, -7, 5], 7 -> [2, 4]



class Solution(object):

Complexity:
Time: O(n)
Space: O(n)
    def two_sum_1(self, nums, val):
        if nums is None or val is None:
            raise TypeError
        if not nums:
            raise ValueError
        visited = {}
        for i,num in enumerate(nums):
            if val-num in visited:
                return [visited[val-num],i]
            visited[num]=i

Complexity:
Time: O(nlogn)
Space: O(1)
    def two_sum(self, nums, val):
        if nums is None or val is None:
            raise TypeError
        if not nums:
            raise ValueError
        nums.sort()
        i = 0
        j = len(nums)-1
        while i<j:
            cur = nums[i]+nums[j]
            if cur>val:
                j-=1
            elif cur<val:
                i+=1
            else:
                return [i,j]
