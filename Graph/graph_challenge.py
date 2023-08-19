#Problem: Implement a graph.

Constraints
Is the graph directed?
Implement both
Do the edges have weights?
Yes
Can the graph have cycles?
Yes
If we try to add a node that already exists, do we just do nothing?
Yes
If we try to delete a node that doesn't exist, do we just do nothing?
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
graph.add_edge(0, 5, 2)
graph.add_edge(1, 2, 3)
graph.add_edge(2, 3, 4)
graph.add_edge(3, 4, 5)
graph.add_edge(3, 5, 6)
graph.add_edge(4, 0, 7)
graph.add_edge(5, 4, 8)
graph.add_edge(5, 2, 9)
Result:
source and destination nodes within graph are connected with specified weight.
Note:
The Graph class will be used as a building block for more complex graph challenges.


time O(1)
space O(1) for all operations

from enum import Enum  # Python 2 users: Run pip install enum34


class State(Enum):

    unvisited = 0
    visiting = 1
    visited = 2


class Node:

    def __init__(self, key):
        self.key = key
        self.visit_state = State.unvisited
        self.incoming_edges = 0
        self.adj_nodes = {}  # Key = key, val = Node
        self.adj_weights = {}  # Key = key, val = weight

    def __repr__(self):
        return str(self.key)

    def __lt__(self, other):
        return self.key < other.key

    def add_neighbor(self, neighbor, weight=0):
        if neighbor is None or weight is None:
            raise TypeError
        if neighbor.key in self.adj_nodes.keys():
            return
        neighbor.incoming_edges+=1
        self.adj_nodes[neighbor.key]=neighbor
        self.adj_weights[neighbor.key]=weight
        
    def remove_neighbor(self, neighbor):
        if neighbor is None:
            raise TypeError
        if neighbor.key not in self.adj_nodes.keys():
            raise KeyError
        neighbor.incoming_edges-=1
        del self.adj_nodes[neighbor.key]
        del self.adj_weights[neighbor.key]


class Graph:

    def __init__(self):
        self.nodes = {}  # Key = key, val = Node

    def add_node(self, id):
        if id is None:
            raise TypeError
        self.nodes[id]=Node(id)

    def add_edge(self, source, dest, weight=0):
        if source is None or dest is None:
            raise TypeError
        if source not in self.nodes.keys():
            self.add_node(source)
        if dest not in self.nodes.keys():
            self.add_node(dest)
        self.nodes[source].add_neighbor(self.nodes[dest],weight)


    def add_undirected_edge(self, source, dest, weight=0):
        self.add_edge(source,dest,weight)
        self.add_edge(dest,source,weight)
