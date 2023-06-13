#https://leetcode.com/problems/kth-largest-element-in-an-array/
#time O(n + k log n) space O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        return -nums[0]
