#https://leetcode.com/problems/process-tasks-using-servers/description/
#time O((m + n) log n) space O(N)
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        n = len(servers)
        m = len(tasks)
        available = [(weight,i) for i,weight in enumerate(servers)]
        unavailable = []
        heapq.heapify(available)
        ans = [0]*m
        curTime = 0
        
        for i in range(m):
            curTime = max(curTime, i)
            if not available:
                curTime = unavailable[0][0]
            while unavailable and unavailable[0][0]<=curTime:
                time, index, weight = heapq.heappop(unavailable)
                heapq.heappush(available,(weight,index))
            weight, serverIndex = heapq.heappop(available)
            heapq.heappush(unavailable,(curTime+tasks[i],serverIndex,weight))
            ans[i]=serverIndex

        return ans
