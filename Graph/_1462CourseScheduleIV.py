#https://leetcode.com/problems/course-schedule-iv/description/
#time O(numCourses + prerequisites + queries) space O(numCourses + prerequisites)
# topological sort
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = Counter()
        for a,b in prerequisites:
            graph[a].append(b)
            indegree[b]+=1
        queue = [i for i in range(numCourses) if indegree[i]==0]
        parent = {i:{i} for i in range(numCourses)}
        while queue:
            cur = queue.pop(0)
            for node in graph[cur]:
                parent[node]=parent[node].union(parent[cur])
                indegree[node]-=1
                if indegree[node]==0:
                    queue.append(node)
        ans = []
        for u,v in queries:
            ans.append( u in parent[v])
        return ans
            

