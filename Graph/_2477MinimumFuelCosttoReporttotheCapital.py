#https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/description/
#time O(V + E) space O(V + E) 
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        for a,b in roads:
            graph[a].append(b)
            graph[b].append(a)
        def dfs(cur,parent):
            total = 1
            for node in graph[cur]:
                if node == parent:
                    continue
                passengers = dfs(node,cur)
                total += passengers
                self.ans += ceil(passengers/seats)
            return total
        self.ans = 0
        dfs(0,0)
        return self.ans
