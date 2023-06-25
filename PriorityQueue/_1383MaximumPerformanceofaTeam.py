#https://leetcode.com/problems/maximum-performance-of-a-team/description/
#time O(nlog n) space O(k)
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eng = [[eff,spd] for spd,eff in zip(speed,efficiency)]
        eng.sort(reverse = True)
        minHeap = []
        ans = 0
        sumSpeed = 0
        for i in range(n):
            eff = eng[i][0]
            if len(minHeap)>=k:
                sumSpeed-=heapq.heappop(minHeap)
            sumSpeed+=eng[i][1]
            heapq.heappush(minHeap,eng[i][1])
            ans = max(ans, sumSpeed*eff)
        return ans%(10**9+7)
