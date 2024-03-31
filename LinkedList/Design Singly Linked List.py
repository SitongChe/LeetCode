#https://neetcode.io/problems/singlyLinkedList
class ListNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        cur = self.head.next
        i = 0
        while cur:
            if i == index:
                return cur.val
            i+=1
            cur = cur.next
        return -1
        

    def insertHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head.next
        self.head.next = node
        if self.head == self.tail:
            self.tail = node
        

    def insertTail(self, val: int) -> None:
        node = ListNode(val)
        self.tail.next = node
        self.tail = node
        

    def remove(self, index: int) -> bool:
        cur = self.head
        for i in range(index):
            if cur:
                cur = cur.next
            else:
                return False
        if cur and cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            return True
        return False
        
        

    def getValues(self) -> List[int]:
        cur = self.head.next
        ans = []
        while cur:
            ans.append(cur.val)
            cur = cur.next
        return ans
