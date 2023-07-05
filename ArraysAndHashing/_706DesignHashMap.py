#https://leetcode.com/problems/design-hashmap/description/
#time O(n log n) ,space  O(1)
class ListNode:
    def __init__(self, key=-1, value=-1, next=None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for i in range(1000)]

    def hashKey(self, key):
        return key%len(self.map)

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hashKey(key)]
        while cur.next:
            if cur.next.key==key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = ListNode(key,value)
          

    def get(self, key: int) -> int:
        cur = self.map[self.hashKey(key)]
        while cur.next:
            if cur.next.key==key:
                return cur.next.value
            cur = cur.next
        return -1
        
    def remove(self, key: int) -> None:
        cur = self.map[self.hashKey(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        
