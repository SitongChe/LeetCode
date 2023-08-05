#https://leetcode.com/problems/single-threaded-cpu/description/
#time O(NlogN) space O(N)
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        unavailable = [[task[0],task[1],index] for index,task in enumerate(tasks)]
        heapq.heapify(unavailable)
        available = []
        time = 0
        ans = []
        while available or unavailable:
            if not available:
                time = max(time,unavailable[0][0])
            while unavailable and unavailable[0][0]<=time:
                enqueueTime,processingTime,index = heapq.heappop(unavailable)
                heapq.heappush(available,[processingTime,index])
            processingTime,index = heapq.heappop(available)
            ans.append(index)
            time += processingTime
        return ans
