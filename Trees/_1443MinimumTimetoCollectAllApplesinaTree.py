#https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/
#time O(N), space O(logN) (height of the tree)

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(cur,parent):
            ans = 0
            for child in graph[cur]:
                if child == parent:
                    continue
                childTime = dfs(child,cur)
                if childTime or hasApple[child]:
                    ans += 2+childTime
            return ans
                

        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return dfs(0,-1)
        
