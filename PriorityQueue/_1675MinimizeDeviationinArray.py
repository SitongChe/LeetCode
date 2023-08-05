#https://leetcode.com/problems/design-twitter/
#time O(nlogM*longN) m is largest num, space O(n)
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        minHeap = []
        maxNum = 0
        for num in nums:
            nMax = num
            while num%2==0:
                num //= 2
            minHeap.append([num,max(num*2,nMax)])
            maxNum = max(maxNum, num)
        heapq.heapify(minHeap)
        ans = inf
        while len(minHeap)==len(nums):
            num,nMax = heapq.heappop(minHeap)
            ans = min(ans,maxNum-num)
            if nMax>num:
                heapq.heappush(minHeap,[num*2,nMax])
                maxNum = max(maxNum,num*2)
        return ans


