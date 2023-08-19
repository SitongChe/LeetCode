#Problem: Find the shortest path between two nodes in a graph.

Constraints
Is the graph directed?
Yes
Is the graph weighted?
No
Can we assume we already have Graph and Node classes?
Yes
Are the inputs two Nodes?
Yes
Is the output a list of Node keys that make up the shortest path?
Yes
If there is no path, should we return None?
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
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(0, 5)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 1)
graph.add_edge(3, 2)
graph.add_edge(3, 4)
Result:
search_path(start=0, end=2) -> [0, 1, 3, 2]
search_path(start=0, end=0) -> [0]
search_path(start=4, end=5) -> None


class GraphShortestPath(Graph):

Complexity:
Time: O(V + E), where V = number of vertices and E = number of edges
Space: O(V)
    def shortest_path_1(self, source_key, dest_key):
        if source_key is None or dest_key is None:
            raise TypeError
        if source_key not in self.nodes.keys() or dest_key not in self.nodes.keys():
            return None
        
        parents = {}
        queue = [self.nodes[source_key]]
        visited = set()
        visited.add(source_key)
        while queue:
            cur = queue.pop(0)
            for node in cur.adj_nodes.values():
                if node.key not in visited:
                    visited.add(node.key)
                    parents[node.key]=cur.key
                    queue.append(node)
        if dest_key not in visited:
            return None

        cur = dest_key
        ans = [cur]
        while cur in parents:
            cur = parents[cur]
            ans.append(cur)
        return ans[::-1]
 
 
Complexity:
Time: O(V^3)
Space: O(V)
    dists = None
    paths = None
    def Floyd_Warshall(self):
        n = len(self.nodes)
        self.dists=[[float("inf")]*n for _ in range(n)]
        self.paths=[[-1]*n for _ in range(n)]
        for node in self.nodes.values():
            self.dists[node.key][node.key]=0
            for nei in node.adj_nodes.values():
                self.dists[node.key][nei.key]=1
                self.paths[node.key][nei.key]=nei.key
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if self.dists[i][j]>self.dists[i][k]+self.dists[k][j]:
                        self.dists[i][j]=self.dists[i][k]+self.dists[k][j]
                        self.paths[i][j]=self.paths[i][k]
        
    def shortest_path(self, source_key, dest_key):
        if not self.paths:
            self.Floyd_Warshall()
        if self.dists[source_key][dest_key]==float("inf"):
            return None
        cur = source_key
        ans = []
        while cur != -1:
            ans.append(cur)
            cur = self.paths[cur][dest_key]
        return ans
