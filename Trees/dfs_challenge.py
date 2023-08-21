#Problem: Implement depth-first traversals (in-order, pre-order, post-order) on a binary tree.

Constraints
Can we assume we already have a Node class with an insert method?
Yes
What should we do with each node when we process it?
Call an input method visit_func on the node
Can we assume this fits in memory?
Yes

Test Cases
In-Order Traversal
5, 2, 8, 1, 3 -> 1, 2, 3, 5, 8
1, 2, 3, 4, 5 -> 1, 2, 3, 4, 5
Pre-Order Traversal
5, 2, 8, 1, 3 -> 5, 2, 1, 3, 8
1, 2, 3, 4, 5 -> 1, 2, 3, 4, 5
Post-Order Traversal
5, 2, 8, 1, 3 -> 1, 3, 2, 8, 5
1, 2, 3, 4, 5 -> 5, 4, 3, 2, 1


Complexity:
Time: O(n)
Space: O(m), where m is the recursion depth, or O(1) if using an iterative approach

class BstDfs(Bst):

    def in_order_traversal_1(self, node, visit_func):
        if not node:
            return
        self.in_order_traversal(node.left,visit_func)
        visit_func(node.data)
        self.in_order_traversal(node.right,visit_func)

    def in_order_traversal(self, node, visit_func):
        if not node:
            return
        stack = [[node,False]]
        while stack:
            cur,visited = stack.pop()
            if cur:
                if visited:
                    visit_func(cur.data)
                else:
                    stack.append([cur.right,False])
                    stack.append([cur,True])
                    stack.append([cur.left,False])
        
    def pre_order_traversal_1(self, node, visit_func):
        if not node:
            return
        visit_func(node.data)
        self.pre_order_traversal(node.left,visit_func)
        self.pre_order_traversal(node.right,visit_func)
        
    def pre_order_traversal(self, node, visit_func):
        if not node:
            return
        stack = [[node,False]]
        while stack:
            cur,visited = stack.pop()
            if cur:
                if visited:
                    visit_func(cur.data)
                else:
                    stack.append([cur.right,False])
                    stack.append([cur.left,False])
                    stack.append([cur,True])

    def post_order_traversal_1(self,node, visit_func):
        if not node:
            return
        self.post_order_traversal(node.left,visit_func)
        self.post_order_traversal(node.right,visit_func)
        visit_func(node.data)
        
    def post_order_traversal(self, node, visit_func):
        if not node:
            return
        stack = [[node,False]]
        while stack:
            cur,visited = stack.pop()
            if cur:
                if visited:
                    visit_func(cur.data)
                else:
                    stack.append([cur,True])
                    stack.append([cur.right,False])
                    stack.append([cur.left,False])
