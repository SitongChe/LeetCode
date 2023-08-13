#https://leetcode.com/problems/largest-color-value-in-a-directed-graph/description/
#time O((E+V)*26) space O(V)
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        def dfs(i):
            if i in path:
                return inf
            if i in visited:
                return 0
            visited.add(i)
            path.add(i)
            colorIndex=ord(colors[i])-ord('a')
            count[i][colorIndex]=1
            if i in graph:
                for node in graph[i]:
                    if dfs(node)==inf:
                        return inf
                    for c in range(26):
                        count[i][c]=max(count[i][c],(1 if c == colorIndex else 0)+count[node][c])
            path.remove(i)
            return max(count[i])
        n = len(colors)
        count = {i:[0]*26 for i in range(n)}
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
        visited = set()
        path = set()
        ans = 0
        for i in range(len(colors)):
            ans = max(dfs(i),ans)
        return ans if ans != inf else -1



