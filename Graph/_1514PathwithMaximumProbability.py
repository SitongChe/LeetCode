#https://leetcode.com/problems/path-with-maximum-probability/description/
#time O(NlogN) space O(N)
#priority queue
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append([edges[i][1],succProb[i]])
            graph[edges[i][1]].append([edges[i][0],succProb[i]])
        visited = set()
        heap = [[-1,start]]
        while heap:
            p,cur = heapq.heappop(heap)
            visited.add(cur)
            if cur == end:
                return -p
            for node,prob in graph[cur]:
                if node not in visited:
                    heapq.heappush(heap,[p*prob,node])
        return 0


