#https://leetcode.com/problems/lru-cache/
#time O(1), space O(capacity)

class Node:
    def __init__(self,key,value):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value
    
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        
    def insertToRight(self,node):
        prev = self.right.prev
        next = self.right
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insertToRight(self.cache[key])
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key,value)
        self.insertToRight(node)
        self.cache[key]=node
        if len(self.cache.keys())>self.size:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


