#https://leetcode.com/problems/course-schedule-iv/description/
#time O(numCourses + prerequisites + queries) space O(numCourses + prerequisites)
# topological sort
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        inorder = Counter()
        parent = defaultdict(set)
        for u,v in prerequisites:
            graph[u].append(v)
            parent[v].add(u)
            inorder[v]+=1
        queue = [i for i in range(numCourses) if inorder[i]==0]
        while queue:
            cur = queue.pop(0)
            for node in graph[cur]:
                inorder[node]-=1
                parent[node] = parent[node].union(parent[cur])
                if inorder[node]==0:
                    queue.append(node)
        return [u in parent[v] for u,v in queries]
        
