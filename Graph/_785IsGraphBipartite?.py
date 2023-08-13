#https://leetcode.com/problems/is-graph-bipartite/description/
#time O(E+V) space O(V)
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        edges = defaultdict(list)
        for i,nodes in enumerate(graph):
            for node in nodes:
                edges[i].append(node)
        def bfs(i):
            queue=[i]
            visited[i]=1
            while queue:
                cur = queue.pop(0)
                side = visited[cur]
                for node in edges[cur]:
                    if node in visited:
                        if visited[node]==side:
                            return False
                        else:
                            continue
                    visited[node]=-1*side
                    queue.append(node)
            return True
        visited = {}
        for node in edges.keys():
            if node not in visited:
                if bfs(node)==False:
                    return False
        return True

