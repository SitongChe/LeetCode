#Problem: Implement depth-first search on a graph.

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
Order of nodes visited: [0, 1, 3, 2, 4, 5]

time O(V+E)
space O(V)

class GraphDfs(Graph):

    def dfs(self, root, visit_func):
        if not root or root.visit_state == State.visited:
            return
        root.visit_state = State.visited
        visit_func(root.key)
        for node in root.adj_nodes.values():
            self.dfs(node,visit_func)
            
