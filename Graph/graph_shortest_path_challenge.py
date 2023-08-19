#Problem: Find the shortest path between two nodes in a graph.

Constraints
Is this a directional graph?
Yes
Could the graph have cycles?
Yes
Note: If the answer were no, this would be a DAG.
DAGs can be solved with a topological sort
Are the edges weighted?
Yes
Note: If the edges were not weighted, we could do a BFS
Are the edges all non-negative numbers?
Yes
Note: Graphs with negative edges can be done with Bellman-Ford
Graphs with negative cost cycles do not have a defined shortest path
Do we have to check for non-negative edges?
No
Can we assume this is a connected graph?
Yes
Can we assume the inputs are valid?
No
Can we assume we already have a graph class?
Yes
Can we assume we already have a priority queue class?
Yes
Can we assume this fits memory?
Yes


Test Cases
The constraints state we don't have to check for negative edges, so we test with the general case.
graph.add_edge('a', 'b', weight=5)
graph.add_edge('a', 'c', weight=3)
graph.add_edge('a', 'e', weight=2)
graph.add_edge('b', 'd', weight=2)
graph.add_edge('c', 'b', weight=1)
graph.add_edge('c', 'd', weight=1)
graph.add_edge('d', 'a', weight=1)
graph.add_edge('d', 'g', weight=2)
graph.add_edge('d', 'h', weight=1)
graph.add_edge('e', 'a', weight=1)
graph.add_edge('e', 'h', weight=4)
graph.add_edge('e', 'i', weight=7)
graph.add_edge('f', 'b', weight=3)
graph.add_edge('f', 'g', weight=1)
graph.add_edge('g', 'c', weight=3)
graph.add_edge('g', 'i', weight=2)
graph.add_edge('h', 'c', weight=2)
graph.add_edge('h', 'f', weight=2)
graph.add_edge('h', 'g', weight=2)
shortest_path = ShortestPath(graph)
result = shortest_path.find_shortest_path('a', 'i')
self.assertEqual(result, ['a', 'c', 'd', 'g', 'i'])
self.assertEqual(shortest_path.path_weight['i'], 8)

shortest distances:

For a general weighted graph, O(VE) time using Bellman–Ford Algorithm.
function bellmanFord(graph, source):
    initialize distances dist from source to all vertices as infinity
    dist[source] = 0

    for i from 1 to number_of_vertices - 1:
        for each edge (u, v) in graph:
            if dist[u] + weight(u, v) < dist[v]:
                dist[v] = dist[u] + weight(u, v)

    for each edge (u, v) in graph:
        if dist[u] + weight(u, v) < dist[v]:
            return "Negative cycle detected"

    return "No negative cycle found"
    
For a graph with no negative weights, O((E + V)LogV) time using Dijkstra’s algorithm.
function dijkstra(graph, source):
    create a priority queue Q
    initialize distances dist from source to all vertices as infinity
    dist[source] = 0
    insert (source, 0) into Q

    while Q is not empty:
        (u, distance) = Q.extract_min()

        if distance > dist[u]:
            continue
        
        for each neighbor v of u:
            new_distance = dist[u] + weight(u, v)
            if new_distance < dist[v]:
                dist[v] = new_distance
                Q.insert(v, new_distance)

    return dist

For a Directed Acyclic Graph (DAG), O(V+E) time using Topological Sorting.
function shortest_path_with_topological_sort(graph, start_vertex, end_vertex):
    initialize an array 'in_degree' to store the in-degree of each vertex
    initialize an empty queue 'queue'
    initialize an empty list 'result'
    initialize a dictionary 'shortest_distance' to store the shortest distance to each vertex
    initialize a dictionary 'predecessor' to store the predecessor of each vertex

    for each vertex v in graph:
        in_degree[v] = calculate_in_degree(v)
        shortest_distance[v] = infinity

    shortest_distance[start_vertex] = 0

    for each vertex v in graph:
        if in_degree[v] == 0:
            queue.enqueue(v)

    while queue is not empty:
        current_vertex = queue.dequeue()
        result.append(current_vertex)

        for each neighbor 'neighbor' of current_vertex:
            new_distance = shortest_distance[current_vertex] + edge_weight(current_vertex, neighbor)
            if new_distance < shortest_distance[neighbor]:
                shortest_distance[neighbor] = new_distance
                predecessor[neighbor] = current_vertex

            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.enqueue(neighbor)

    # Generate the shortest path from 'start_vertex' to 'end_vertex'
    shortest_path = [end_vertex]
    current = end_vertex
    while current != start_vertex:
        current = predecessor[current]
        shortest_path.append(current)
    shortest_path.reverse()

    return result, shortest_path


Space Complexity is all O(V)

For finding all shortest paths for all pairs of node, O(V^3) time, O(V^2) space using Floyd-Warshall algorithm
function floyd_warshall(graph):
    n = number of vertices in the graph
    initialize a 2D array 'dist' of size n x n with infinity values
    initialize a 2D array 'next' of size n x n with -1 values
    
    for each vertex v in graph:
        dist[v][v] = 0

    for each edge (u, v) in graph:
        dist[u][v] = weight of edge (u, v)
        next[u][v] = v

    for k from 1 to n:
        for i from 1 to n:
            for j from 1 to n:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next[i][j] = next[i][k]

    return dist, next


Complexity for array-based priority queue:
Time: O(v^2), where v is the number of vertices
This might be better than the min-heap-based variant if the graph has a lot of edges.
O(v^2) is better than O((v + v^2) log v).

Complexity for min-heap-based priority queue:
Time: O((v + e) log v), where v is the number of vertices, e is the number of edges
This might be better than the array-based variant if the graph is sparse.

import heapq
class ShortestPath(object):

    def __init__(self, graph):
        self.graph = graph
        self.path_weight = {key:float("inf") for key in self.graph.nodes.keys()}

    def find_shortest_path(self, start_node_key, end_node_key):
        self.path_weight[start_node_key]=0
        #minHeap = PriorityQueue()
        #minHeap.insert(PriorityQueueNode(self.graph.nodes[start_node_key],0))
        minHeap = [[0,self.graph.nodes[start_node_key]]]
        parents = {}
        while minHeap:
            #cur = minHeap.extract_min()
            #curDist,curNode = cur.key, cur.obj
            curDist,curNode = heapq.heappop(minHeap)
            for key,node in curNode.adj_nodes.items():
                weight = curNode.adj_weights[key]
                if self.path_weight[key]>curDist+weight:
                    self.path_weight[key]=curDist+weight
                    parents[key]=curNode.key
                    #minHeap.insert(PriorityQueueNode(node,self.path_weight[key]))
                    heapq.heappush(minHeap,[self.path_weight[key],node])
        cur = end_node_key
        ans = [cur]
        while cur in parents:
            cur = parents[cur]
            ans.append(cur)
        return ans[::-1]
