#https://leetcode.com/problems/detonate-the-maximum-bombs/description/
#time O(N^2) space O(N^2)
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        #bombs.sort(lambda key=x:x[2],reverse=True)
        graph = defaultdict(list)
        n = len(bombs)
        for i in range(n):
            x,y,r = bombs[i]
            for j in range(i+1,n):
                xx,yy,rr=bombs[j]
                d = (xx-x)**2+(yy-y)**2
                if d<=r**2:
                    graph[i].append(j)
                if d<=rr**2:
                    graph[j].append(i)
        def dfs(i):
            if i in visited:
                return 0
            visited.add(i)
            for node in graph[i]:
                dfs(node)
            return len(visited)
        
        ans = 0
        for i in range(n):
            visited = set()
            ans = max(ans,dfs(i))
        return ans




