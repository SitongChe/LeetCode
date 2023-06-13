#https://leetcode.com/problems/minimum-interval-to-include-each-query/
#time O((n + q) log n) space O(N)
#priority queue
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ans = []
        n = len(queries)
        minHeap = []
        ans = {}
        i = 0
        intervals.sort()
        for q in sorted(queries):
            while i<len(intervals) and intervals[i][0]<=q:
                heapq.heappush(minHeap,[intervals[i][1]-intervals[i][0]+1,intervals[i][1]])
                i+=1
            while minHeap and minHeap[0][1]<q:
                heapq.heappop(minHeap)
            ans[q]=minHeap[0][0] if minHeap else -1
        return [ans[q] for q in queries]
