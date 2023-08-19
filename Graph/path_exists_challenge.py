#Problem: Determine whether there is a path between two nodes in a graph.

Constraints
Is the graph directed?
Yes
Can we assume we already have Graph and Node classes?
Yes
Can we assume this is a connected graph?
Yes
Can we assume the inputs are valid?
Yes
Can we assume this fits memory?
Yes

Test Cases
Input:
add_edge(source, destination, weight)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 4, 3)
graph.add_edge(0, 5, 2)
graph.add_edge(1, 3, 5)
graph.add_edge(1, 4, 4)
graph.add_edge(2, 1, 6)
graph.add_edge(3, 2, 7)
graph.add_edge(3, 4, 8)
Result:
search_path(start=0, end=2) -> True
search_path(start=0, end=0) -> True
search_path(start=4, end=5) -> False

time O(V+E)
space O(V)

from collections import defaultdict

class GraphPathExists(Graph):
    visited = defaultdict(set)
    def dfs(self,start,visited):
        if start.key not in visited:
            visited.add(start.key)
            for node in start.adj_nodes.values():
                self.dfs(node,visited)
                
    def bfs(self,start,visited):
        queue = [start]
        while queue:
            cur = queue.pop(0)
            if cur.key not in visited:
                visited.add(cur.key)
                for node in cur.adj_nodes.values():
                    queue.append(node)

    def path_exists(self, start, end):
        if start is None or end is None:
            return False
        if start.key in self.visited.keys():
            print(str(start.key) + " using short cut")
            return end.key in self.visited[start.key]
        self.bfs(start,self.visited[start.key])
        return end.key in self.visited[start.key]
