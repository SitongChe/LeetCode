#https://leetcode.com/problems/process-tasks-using-servers/description/
#time O((m + n) log n) space O(N)
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available = [[weight,i] for i,weight in enumerate(servers)]
        heapq.heapify(available)
        unavailable = []
        time = 0
        ans = []
        for j,task in enumerate(tasks):
            time = max(time,j)
            if not available:
                time = max(time,unavailable[0][0])
            while unavailable and unavailable[0][0]<=time:
                finishedTime,weight,i= heapq.heappop(unavailable)
                heapq.heappush(available,[weight,i])
            weight,i = heapq.heappop(available)
            heapq.heappush(unavailable,[time+task,weight,i])
            ans.append(i)
        return ans
