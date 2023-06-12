#https://leetcode.com/problems/network-delay-time/
#time O(ElogV) space O(E+V)
#priority queue
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ans = 0
        visited = set()
        adjs = defaultdict(list)
        for u,v,w in times:
            adjs[u].append([v,w])
        minHeap = [[0,k]]
        while minHeap:
            time,cur = heapq.heappop(minHeap)
            if cur in visited:
                continue
            ans = time
            visited.add(cur)
            for v,w in adjs[cur]:
                if v not in visited:
                    heapq.heappush(minHeap,[time+w,v])
        return ans if len(visited)==n else -1
        
