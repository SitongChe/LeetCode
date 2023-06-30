#https://leetcode.com/problems/network-delay-time/
#time O(ElogV) space O(E+V)
#priority queue dijistra
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ans = 0
        visited = set()
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append([v,w])
        heap = [[0,k]]
        while heap:
            time, cur = heapq.heappop(heap)
            if cur in visited:
                continue
            visited.add(cur)
            ans = time
            for u,w in graph[cur]:
                if u not in visited:
                    heapq.heappush(heap,[w+time,u])
        return ans if len(visited)==n else -1
        
        
