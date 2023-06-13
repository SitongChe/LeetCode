#https://leetcode.com/problems/course-schedule-ii/
#time O(V+E) space O(V+E)
# topological sort
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = len(prerequisites)
        ans = []
        indegree = Counter()
        graph = defaultdict(list)
        for p,q in prerequisites:
            indegree[p]+=1
            graph[q].append(p)
        queue = [i for i in range(numCourses) if indegree[i]==0]
        while queue:
            cur = queue.pop(0)
            ans.append(cur)
            for node in graph[cur]:
                indegree[node]-=1
                if indegree[node]==0:
                    queue.append(node)
        if len(ans)==numCourses:
            return ans
        return []
        
