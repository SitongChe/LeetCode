#https://leetcode.com/problems/path-with-maximum-probability/description/
#time O(NlogN) space O(N)
#priority queue
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for (u,v),p in zip(edges,succProb):
            graph[u].append([v,p])
            graph[v].append([u,p])
        maxHeap = [[-1,start_node]]
        visited = set()
        while maxHeap:
            negP,cur = heapq.heappop(maxHeap)
            if cur not in visited:
                visited.add(cur)
                if cur == end_node:
                    return -negP
                for node,p in graph[cur]:
                    if node not in visited:
                        heapq.heappush(maxHeap,[p*negP,node])
        return 0

        
