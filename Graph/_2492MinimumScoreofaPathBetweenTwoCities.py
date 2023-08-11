#https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/
#time O(V + E) space O(V + E) 
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a,b,dist in roads:
            graph[a].append([b,dist])
            graph[b].append([a,dist])
        queue = [1]
        ans = inf
        visited = set()
        visited.add(1)
        while queue:
            cur = queue.pop(0)
            for node,dist in graph[cur]:
                ans = min(ans,dist)
                if node not in visited:
                    visited.add(node)
                    queue.append(node)
        return ans

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a,b,dist in roads:
            graph[a].append([b,dist])
            graph[b].append([a,dist])
        self.ans = inf
        visited = set()
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for node,dist in graph[i]:
                self.ans = min(self.ans, dist)
                dfs(node)
        dfs(1)
        return self.ans






        
