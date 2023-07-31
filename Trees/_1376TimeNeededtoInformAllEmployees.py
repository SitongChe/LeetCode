#https://leetcode.com/problems/time-needed-to-inform-all-employees/description/
#time O(N), space O(N)

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(len(manager)):
            graph[manager[i]].append(i)
        queue = [[headID,0]]
        ans = 0
        while queue:
            size = len(queue)
            for i in range(size):
                cur,time = queue.pop(0)
                ans = max(ans,time)
                for node in graph[cur]:
                    queue.append([node,time+informTime[cur]])
        return ans
