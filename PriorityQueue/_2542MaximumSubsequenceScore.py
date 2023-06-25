#https://leetcode.com/problems/maximum-subsequence-score/description/
#time O(nlog n) space O(k)
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = [[num2,num1] for num2, num1 in zip(nums2,nums1)]
        nums.sort(reverse = True)
        minHeap = []
        ans = 0
        sum = 0
        for i in range(len(nums)):
            num2 = nums[i][0]
            if len(minHeap)==k:
                sum-=heapq.heappop(minHeap)
            sum += nums[i][1]
            heapq.heappush(minHeap,nums[i][1])
            if len(minHeap)==k:
                ans = max(ans,sum*num2)
        return ans
            
