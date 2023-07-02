#https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description/
#time O(N) space O(N)
#priority queue
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def dfs(cur):
            for node in graph[cur]:
                if node not in visited:
                    if (node,cur) not in edges:
                        self.change+=1
                    visited.add(node)
                    dfs(node)

        edges=set()
        visited = set()
        self.change = 0
        visited.add(0)
        graph = defaultdict(list)
        for a,b in connections:
            graph[a].append(b)
            graph[b].append(a)
            edges.add((a,b))
        dfs(0)
        return self.change
        

