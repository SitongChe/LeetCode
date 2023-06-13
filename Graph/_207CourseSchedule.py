#https://leetcode.com/problems/course-schedule/
#time O(V+E) space O(V+E)
# topological sort
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = len(prerequisites)
        if n == 0:
            return True
        indegree = Counter()
        graph = defaultdict(list)
        for p,q in prerequisites:
            indegree[p]+=1
            graph[q].append(p)
        queue = [i for i in range(numCourses) if indegree[i]==0]
        while queue:
            cur = queue.pop(0)
            for node in graph[cur]:
                indegree[node]-=1
                if indegree[node]==0:
                    queue.append(node)
        return max(indegree.values())==0



