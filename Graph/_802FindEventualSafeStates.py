#https://leetcode.com/problems/find-eventual-safe-states/description/
#time O(V * log(V)) space O(V + E)
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        outdegree = {}
        for i in range(len(graph)):
            for node in graph[i]:
                edges[node].append(i)
            outdegree[i] = len(graph[i])
        queue = [i for i in outdegree.keys() if outdegree[i]==0]
        ans = []
        while queue:
            cur = queue.pop(0)
            ans.append(cur)
            for node in edges[cur]:
                outdegree[node]-=1
                if outdegree[node]==0:
                    queue.append(node)
        return sorted(ans)

        

        

        
