#https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/
#time O(N) space O(N)
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        if node1 == node2:
            return node1
        graph = {}
        for u,v in enumerate(edges):
            graph[u] = v
        visited = {}
        cur = node1
        step = 0
        while cur!=-1 and cur not in visited:
            visited[cur]=step
            step+=1
            cur = graph[cur]
                
        visited2 = set()
        cur = node2
        minStep = inf
        ans = inf
        step = 0
        while cur!=-1 and cur not in visited2:
            if cur in visited:
                if max(visited[cur],step)==minStep:
                    ans = min(ans,cur)
                if max(visited[cur],step)<minStep:
                    minStep = max(visited[cur],step)
                    ans = cur
            step+=1
            visited2.add(cur)
            cur = graph[cur]
                
        return ans if minStep!=inf else -1
                




        
