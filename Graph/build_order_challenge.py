#Problem: Find a build order given a list of projects and dependencies.

Constraints
Is it possible to have a cyclic graph as the input?
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
projects: a, b, c, d, e, f, g
dependencies: (d, g), (f, c), (f, b), (f, a), (c, a), (b, a), (a, e), (b, e)
output: d, f, c, b, g, a, e
Note: Edge direction is down
    f     d
   /|\    |
  c | b   g
   \|/|
    a |
    |/
    e
Test a graph with a cycle, output should be None

time O(V+E)
space O(V+E)

class BuildOrder(object):

    def __init__(self, dependencies):
        self.graph = Graph()
        for d in dependencies:
            self.graph.add_edge(d.node_key_before,d.node_key_after)

    def find_build_order(self):
        queue = [node for key,node in self.graph.nodes.items() if node.incoming_edges == 0]
        ans = []
        while queue:
            cur = queue.pop(0)
            if cur.visit_state != State.visited:
                cur.visit_state = State.visited
                ans.append(cur)
                # We'll need to iterate on copies since we'll need
                # to change the dictionaries during iteration with
                # the remove_neighbor call
                for node in list(cur.adj_nodes.values()):
                    cur.remove_neighbor(node)
                    if node.incoming_edges==0:
                        queue.append(node)
        for key,node in self.graph.nodes.items():
            if node.incoming_edges != 0:
                return None
        return ans 
