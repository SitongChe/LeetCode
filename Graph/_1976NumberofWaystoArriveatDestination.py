#https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description/
#time O(ElogV) space O(V)
#priority queue
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        ans = 0
        graph = defaultdict(list)
        for u,v,time in roads:
            graph[u].append([v,time])
            graph[v].append([u,time])

        times = [inf]*n
        ways = [0] * n
        ways[0] = 1
        times[0]=0
        heap = [[0,0]]
        mod = 10**9+7
        while heap:
            time,cur = heapq.heappop(heap)
            for node,edgeTime in graph[cur]:
                if edgeTime + time < times[node]:
                    times[node]=edgeTime + time
                    ways[node] = ways[cur]
                    heapq.heappush(heap,[time+edgeTime,node])
                elif edgeTime + time == times[node]:
                    ways[node] = (ways[cur]+ways[node]) % mod
        return ways[n-1] % mod

