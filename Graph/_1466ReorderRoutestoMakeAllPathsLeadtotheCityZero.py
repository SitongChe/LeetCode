#https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description/
#time O(N) space O(N)
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def dfs(root):
            ans = 0
            for node in graph[root]:
                if node not in visited:
                    visited.add(node)
                    if (node,root) not in edges:
                        edges.add((node,root))
                        ans += 1
                    ans+=dfs(node)
            return ans
        graph = defaultdict(list)
        edges = set()
        visited = set()
        visited.add(0)
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
            edges.add((u,v))
        return dfs(0)

        
